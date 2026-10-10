# Data

The data files are not stored in this repository because they are larger than GitHub's 100 MB file limit. Everything in this folder except this README is ignored by git.

## 1. Download the raw data

The project uses the **Dubai Police Traffic Incidents** dataset, published on **Data.Dubai** (formerly Dubai Pulse) under the Open classification.

1. Go to Data.Dubai and search for "Traffic Incidents" (publisher: Dubai Police). The original Dubai Pulse page was https://www.dubaipulse.gov.ae/data/dp-traffic/dp_traffic_incidents-open
2. Download the full CSV export. You may need to sign in or accept the terms of use first.
3. Save it in `data/raw/`.

The export used for this project is `traffic_incidents_2026-10-09_04-37-34_0001.csv`, downloaded on 9 Oct 2026:

| Property | Value |
|---|---|
| Records | 757,305 |
| Period | 13 Aug 2018 to 7 Oct 2026 |
| Size | about 109 MB, CSV, UTF-8 |
| Columns | `acci_id`, `acci_name`, `acci_time`, `acci_x`, `acci_y`, `load_timestamp` |

A newer export will contain more recent records, so the row counts will differ slightly from those in `docs/preprocessing_log.md`.

## 2. Regenerate the clean file

From the repository root:

```bash
pip install -r requirements.txt
python src/preprocess.py data/raw/traffic_incidents_2026-10-09_04-37-34_0001.csv data/processed
```

This writes:

- `data/processed/dubai_collisions_clean.csv`: 442,690 collisions and 24 columns (about 101 MB).
- `data/processed/preprocessing_log.md`: the rows removed at each step. A copy of the log from the original run is kept in `docs/preprocessing_log.md`.

## Expected layout

```
data/
├── README.md
├── raw/
│   └── traffic_incidents_2026-10-09_04-37-34_0001.csv
└── processed/
    ├── dubai_collisions_clean.csv
    └── preprocessing_log.md
```

## Columns in the clean file

| Column | Meaning |
|---|---|
| `acci_id` | Dubai Police incident ID |
| `datetime` | Date and time of the incident |
| `lat`, `lon` | Coordinates, with swapped rows corrected |
| `x_m`, `y_m` | Local coordinates in metres, for distance-based clustering |
| `grid_500m` | 500 m grid-cell ID |
| `in_hatta` | True if the incident is in the Hatta exclave |
| `type_ar` | Original Arabic incident type, without the severity suffix |
| `collision_type` | English collision group (13 groups) |
| `severity_3` | Original severity: Minor, Moderate or Severe |
| `severity`, `is_serious` | Binary target: Minor (0) or Serious (1) |
| `year`, `month`, `day_of_week`, `hour`, `time_of_day` | Temporal features |
| `is_weekend` | Weekend flag that follows the UAE's 2022 weekend change |
| `is_rush_hour`, `season`, `covid_period` | Further temporal flags |
| `incomplete_month` | True for months where the data feed was incomplete |
| `coords_swapped` | True if the coordinates were swapped and fixed |
