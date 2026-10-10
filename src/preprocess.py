"""Mandatory preprocessing for the Dubai road collision hotspot project.

Input : raw Dubai Police traffic incidents CSV (Dubai Pulse / Data.Dubai export)
Output: a clean, collisions-only table ready for EDA, clustering and classification,
        plus a log of how many rows each step removed.

Usage : python3 preprocess.py <raw.csv> <out_dir>
Needs : pandas, numpy
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).parent))
from category_map import map_category  # noqa: E402

SEVERITY = {'بسيط': 'Minor', 'متوسط': 'Moderate', 'بليغ': 'Severe'}

# Dubai lies roughly in this box; Hatta is a separate exclave to the east.
MAIN_BOX = dict(lat=(24.60, 25.36), lon=(54.85, 55.70))
HATTA_BOX = dict(lat=(24.70, 24.90), lon=(55.95, 56.25))

# UAE weekend moved from Fri-Sat to Sat-Sun on 1 Jan 2022.
WEEKEND_SWITCH = pd.Timestamp('2022-01-01')

log = []


def step(df, name):
    prev = log[-1][2] if log else len(df)
    log.append((name, prev - len(df), len(df)))
    print(f'{name:<55} removed {prev - len(df):>8,}  remaining {len(df):>8,}')
    return df


def in_box(lat, lon, box):
    return lat.between(*box['lat']) & lon.between(*box['lon'])


def main(raw_path, out_dir):
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    # 1. Load with explicit types (IDs as text so they are not rounded).
    df = pd.read_csv(raw_path, dtype={'acci_id': str, 'acci_name': str})
    df = step(df, '1. Loaded raw file')

    # 2. Duplicates: exact copies, then repeated incident IDs (the same incident
    #    re-exported with a refined GPS fix). Keep the most recently loaded version.
    df = df.drop_duplicates()
    df = step(df, '2a. Dropped exact duplicate rows')
    df['load_timestamp'] = pd.to_datetime(df['load_timestamp'], errors='coerce')
    df = df.sort_values('load_timestamp').drop_duplicates('acci_id', keep='last')
    df = step(df, '2b. Kept latest record per acci_id')

    # 3. Split the Arabic category into incident type and severity suffix.
    parts = df['acci_name'].str.extract(r'^(.*?)\s*-\s*(بسيط|بليغ|متوسط)\s*$')
    df['type_ar'] = parts[0].fillna(df['acci_name']).str.strip()
    df['severity_3'] = parts[1].map(SEVERITY)
    mapped = df['type_ar'].map(lambda b: map_category(b))
    df['collision_type'] = mapped.str[0]
    df['is_collision'] = mapped.str[1]

    # 4. Keep only road traffic collisions (drop breakdowns, parking, congestion,
    #    hazards, violations, cancelled and unreadable records).
    excluded = df.loc[~df['is_collision'], 'collision_type'].value_counts()
    df = df[df['is_collision']].copy()
    df = step(df, '4. Kept traffic collisions only')

    # 5. Coordinates. The documented order is acci_x = latitude, acci_y = longitude,
    #    but from late 2025 most rows are swapped. Detect per row and fix.
    x, y = df['acci_x'], df['acci_y']
    normal = (in_box(x, y, MAIN_BOX) | in_box(x, y, HATTA_BOX))
    swapped = ~normal & (in_box(y, x, MAIN_BOX) | in_box(y, x, HATTA_BOX))
    df['lat'] = np.where(swapped, y, x)
    df['lon'] = np.where(swapped, x, y)
    df['coords_swapped'] = swapped
    print(f'    rows with swapped coordinates fixed: {swapped.sum():,}')
    df = df[normal | swapped].copy()
    df = step(df, '5. Dropped missing, zero or out-of-Dubai coordinates')
    df['in_hatta'] = in_box(df['lat'], df['lon'], HATTA_BOX)

    # 6. Time parsing and validation.
    df['datetime'] = pd.to_datetime(df['acci_time'], errors='coerce')
    df = df[df['datetime'].notna() & (df['datetime'] <= df['load_timestamp'])]
    df = step(df, '6. Dropped unparseable or future timestamps')

    # 7. Severity target. "Moderate" only appears in 2018-2020, so it is merged
    #    with "Severe" into one Serious class for a consistent binary target.
    df['severity'] = df['severity_3'].map({'Minor': 'Minor', 'Moderate': 'Serious', 'Severe': 'Serious'})
    df['is_serious'] = (df['severity'] == 'Serious').astype('Int8')
    df.loc[df['severity'].isna(), 'is_serious'] = pd.NA

    # 8. Temporal features.
    t = df['datetime']
    df['year'] = t.dt.year
    df['month'] = t.dt.month
    df['day_of_week'] = t.dt.day_name()
    df['hour'] = t.dt.hour
    df['time_of_day'] = pd.cut(df['hour'], bins=[-1, 5, 11, 16, 20, 23],
                               labels=['Night (0-5)', 'Morning (6-11)', 'Afternoon (12-16)',
                                       'Evening (17-20)', 'Late evening (21-23)'])
    dow = t.dt.dayofweek  # Mon=0
    old_weekend = dow.isin([4, 5])   # Fri, Sat
    new_weekend = dow.isin([5, 6])   # Sat, Sun
    df['is_weekend'] = np.where(t < WEEKEND_SWITCH, old_weekend, new_weekend)
    df['is_rush_hour'] = df['hour'].isin([7, 8, 17, 18, 19])
    df['season'] = np.where(df['month'].isin([5, 6, 7, 8, 9]), 'Summer', 'Winter')
    df['covid_period'] = t.between('2020-03-15', '2021-06-30')

    # 9. Flag months where the feed was clearly incomplete (under 60% of the
    #    rolling 5-month median), so analyses can exclude or reweight them.
    monthly = t.dt.to_period('M').value_counts().sort_index()
    ref = monthly.rolling(5, center=True, min_periods=3).median()
    low = monthly[monthly < 0.6 * ref].index
    df['incomplete_month'] = t.dt.to_period('M').isin(low)

    # 10. Spatial features: local metric coordinates (equirectangular around
    #     Dubai, accurate to well under 1% at this scale) and a 500 m grid cell.
    lat0, lon0 = 25.0, 55.2
    df['x_m'] = (df['lon'] - lon0) * 111_320 * np.cos(np.radians(lat0))
    df['y_m'] = (df['lat'] - lat0) * 110_574
    df['grid_500m'] = ((df['x_m'] // 500).astype(int).astype(str) + '_'
                       + (df['y_m'] // 500).astype(int).astype(str))

    cols = ['acci_id', 'datetime', 'lat', 'lon', 'x_m', 'y_m', 'grid_500m', 'in_hatta',
            'type_ar', 'collision_type', 'severity_3', 'severity', 'is_serious',
            'year', 'month', 'day_of_week', 'hour', 'time_of_day', 'is_weekend',
            'is_rush_hour', 'season', 'covid_period', 'incomplete_month', 'coords_swapped']
    df = df[cols].sort_values('datetime')
    df.to_csv(out_dir / 'dubai_collisions_clean.csv', index=False)

    with open(out_dir / 'preprocessing_log.md', 'w') as f:
        f.write('# Preprocessing log\n\n| Step | Rows removed | Rows remaining |\n|---|---:|---:|\n')
        for name, removed, remaining in log:
            f.write(f'| {name} | {removed:,} | {remaining:,} |\n')
        f.write(f'\nCoordinates swapped and fixed: {int(df["coords_swapped"].sum()):,}\n')
        f.write('\n## Non-collision records excluded in step 4\n\n| Category | Rows |\n|---|---:|\n')
        for k, v in excluded.items():
            f.write(f'| {k} | {v:,} |\n')
        f.write('\n## Collision types kept\n\n| Type | Rows | % Serious |\n|---|---:|---:|\n')
        g = df.groupby('collision_type')['is_serious'].agg(['size', 'mean']).sort_values('size', ascending=False)
        for k, r in g.iterrows():
            f.write(f'| {k} | {int(r["size"]):,} | {100 * r["mean"]:.1f} |\n')
        f.write('\n## Severity\n\n| Class | Rows |\n|---|---:|\n')
        for k, v in df['severity'].value_counts(dropna=False).items():
            f.write(f'| {k} | {v:,} |\n')
        f.write('\n## Months flagged as incomplete\n\n')
        f.write(', '.join(str(p) for p in low) + '\n')
        f.write(f'\nDate range: {df["datetime"].min()} to {df["datetime"].max()}\n')
    print('done')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
