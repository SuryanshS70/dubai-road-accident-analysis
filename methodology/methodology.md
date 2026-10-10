# Overall Methodology: Road Accident Hotspot Analysis in Dubai

The project follows the standard data mining process (CRISP-DM): data understanding, preprocessing, exploratory analysis, modelling (clustering and classification), evaluation, and interpretation for emergency response.

```
Raw Dubai Police incidents (757,305 records)
        │
        ▼
Mandatory preprocessing ──► clean collision table (442,690 records)
        │
        ├──► Exploratory analysis (time, type, severity, maps)
        ├──► Hotspot clustering (DBSCAN / HDBSCAN, K-means baseline)
        ├──► Severity classification (Minor vs Serious)
        └──► Emergency-response analysis (hotspots vs hospitals and ambulance points)
                    │
                    ▼
        Evaluation, interpretation and recommendations
```

## 1. Data source

**Dubai Police Traffic Incidents**, published on Data.Dubai (formerly Dubai Pulse) under the Open classification. The export used is `traffic_incidents_2026-10-09_04-37-34_0001.csv`, downloaded 9 Oct 2026.

| Property | Value |
|---|---|
| Records | 757,305 |
| Period | 13 Aug 2018 to 7 Oct 2026 |
| Columns | `acci_id` (incident ID), `acci_name` (Arabic category with severity suffix), `acci_time` (date and time), `acci_x`, `acci_y` (coordinates), `load_timestamp` (time loaded to the portal) |
| Format | CSV, UTF-8, 109 MB |

The file is an emergency-call log. It covers every incident Dubai Police attended, not only collisions.

## 2. Mandatory preprocessing

The script `src/preprocess.py` implements all of these steps. `src/category_map.py` holds the category translation. Row counts are from the actual run.

| Step | What is done and why | Rows removed | Rows left |
|---|---|---:|---:|
| 1. Load | Read with explicit types. `acci_id` is read as text so the long IDs are not rounded. | 0 | 757,305 |
| 2a. Exact duplicates | Identical rows exported twice are dropped. | 869 | 756,436 |
| 2b. Repeated IDs | The same incident sometimes appears again with a refined GPS fix. Only the most recently loaded version is kept. | 3,259 | 753,177 |
| 3. Parse category | `acci_name` is split into the incident type and its severity suffix: بسيط = Minor, متوسط = Moderate, بليغ = Severe. 189 distinct Arabic types are mapped to 13 English collision groups (and 9 non-collision groups). | – | – |
| 4. Keep collisions only | Breakdowns, double parking, congestion, road hazards, traffic violations, jaywalking, cancelled events and 30 corrupted (unreadable) records are removed. Without this step, about 41% of the "accidents" would not be accidents. | 309,443 | 443,734 |
| 5. Fix and validate coordinates | The documented order is `acci_x` = latitude and `acci_y` = longitude, but from late 2025 onward most rows have them swapped. Each row is checked against Dubai's bounding box (including the Hatta exclave) and swapped back where needed (35,540 rows). Missing, zero and out-of-Dubai points are dropped. | 1,011 | 442,723 |
| 6. Validate time | Unparseable timestamps, and times after the record's load time, are dropped. | 33 | 442,690 |
| 7. Severity target | Moderate occurs only in 2018–2020, so it is merged with Severe into one **Serious** class. The target becomes binary: Minor (378,739) vs Serious (57,163, 13.1%). 6,788 collisions have no severity label. They stay in the clustering data but are left out of classification. | – | – |
| 8. Temporal features | Year, month, day of week, hour, time-of-day band, rush hour, season (summer is May–Sep), and a COVID-period flag (Mar 2020 to Jun 2021). The weekend flag follows the UAE weekend change: Fri–Sat before 1 Jan 2022, Sat–Sun after. | – | – |
| 9. Data-quality flags | Months where the feed is clearly incomplete (under 60% of the rolling median) are flagged: 2018-10, 2021-03, 2023-01, 2025-10, 2026-04. 2026-10 is also flagged, but only because that month is partial. These months are excluded from trend and seasonality analysis. | – | – |
| 10. Spatial features | Latitude and longitude are converted to local metres (`x_m`, `y_m`) so distance-based algorithms work in real units. Each record also gets a 500 m grid-cell ID for density counts. | – | – |

Final output: `data/processed/dubai_collisions_clean.csv` (442,690 collisions, 24 columns). Full counts are in `docs/preprocessing_log.md`.

**Optional enrichment** (joined on location and hour, where the team has time):
- **Weather:** hourly rain, wind and temperature from the Open-Meteo historical API, joined on the incident hour. Rain is rare in Dubai but strongly linked to collision spikes.
- **Road network:** OpenStreetMap roads via OSMnx. Each collision is snapped to its nearest road to get road class, speed limit and lanes, and whether it happened at a junction.
- **Areas:** Dubai Municipality community boundaries, to name hotspots and compute rates per community.
- **Emergency resources:** hospitals and ambulance stations from OpenStreetMap.

## 3. Exploratory data analysis

- Distribution of collision types and severity, and the share of Serious collisions per type. Two-wheeler and pedestrian collisions are about 47–50% Serious, while fixed-object collisions are under 2%.
- Temporal patterns: hour × day-of-week heatmap, monthly trend, weekend vs weekday, rush hour, summer vs winter, and the COVID dip.
- Spatial overview: point density map (kernel density) and counts per 500 m grid cell.
- Chi-square tests of independence between severity and temporal or type variables, with Cramér's V as the effect size.

## 4. Hotspot detection (clustering)

**Main method: DBSCAN** on `x_m` and `y_m`. It finds clusters of any shape, does not need the number of clusters in advance, and labels isolated collisions as noise, which suits accident points.
- Parameters: `eps` of about 150–300 m, chosen with the k-distance elbow plot. `min_samples` is scaled to the period analysed.
- To keep the run time manageable, run it per year, or on Serious collisions only, or on grid-cell centroids weighted by count.

**Comparison methods:**
- **HDBSCAN**, which handles clusters of varying density (dense downtown vs sparse highways).
- **K-means**, as a partitioning baseline, with k chosen by the elbow method and silhouette score.

**Hotspot ranking:** each cluster gets a severity-weighted score (Minor = 1, Serious = 3), plus its peak hours and dominant collision type.

**Validation:**
- Silhouette score and Davies–Bouldin index for K-means.
- DBCV, or the share of points that are noise, for density-based methods.
- Temporal stability: whether the same hotspots reappear in different years.
- Optional statistical confirmation with Getis-Ord Gi* on the 500 m grid.

## 5. Severity classification

- **Target:** `is_serious` (Minor = 0, Serious = 1).
- **Features:** collision type, hour, time of day, day of week, weekend, rush hour, month, season, year, hotspot cluster ID (from section 4), grid-cell density, and optionally rain, road class and distance to the nearest hospital.
- **Models:** Decision Tree (interpretable rules), Naive Bayes, Logistic Regression and Random Forest. Optionally Gradient Boosting.
- **Class imbalance (13% Serious):** class weights or SMOTE, applied to the training data only.
- **Split:** train on 2018–2024 and test on 2025–2026, so the model is tested on future data. Stratified 5-fold cross-validation on the training set is used for tuning.
- **Metrics:** recall, precision and F1 for the Serious class, ROC-AUC and PR-AUC, and the confusion matrix. Accuracy alone is misleading at 87% Minor.
- **Interpretation:** feature importance from the Random Forest, and the top rules from the Decision Tree.

## 6. Emergency-response analysis

- For each high-ranking hotspot, compute the distance to the nearest hospital and ambulance station (from OpenStreetMap).
- Identify hotspots with many Serious collisions that are far from existing resources.
- Suggest candidate standby points for first responders with weighted K-means on Serious collision locations (weights = severity), and compare them with existing stations. Peak hours per hotspot show when the standby points matter most.

## 7. Tools

Python, with pandas and NumPy for preprocessing; scikit-learn for K-means, DBSCAN and the classifiers; `hdbscan`; imbalanced-learn for SMOTE; OSMnx and GeoPandas for road and facility data; and Folium or Matplotlib for maps.

## 8. Limitations

- Severity has only two usable levels, and there are no injury counts, causes, driver or vehicle details.
- The coordinates are where police recorded the incident, which can be off by tens of metres.
- The data has some ingestion gaps (flagged months), and category names changed over time. Dubai Police switched to a new set of category names in 2021. The older names, used from 2018 to early 2021, do not separate motorcycles from bicycles, so the two are grouped together as two-wheelers.
- The data shows correlation only, so hotspots show where collisions concentrate, not why.
