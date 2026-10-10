# Road Accident Hotspot Analysis in Dubai

A data mining course project. It uses Dubai Police incident records to find where and when road collisions concentrate in Dubai, to predict how serious a collision is likely to be, and to turn those findings into recommendations for emergency response.

**Team:** Ramsha Ansari, Suryansh Sharma and Taha

## Goal

Dubai Police publishes a log of every traffic incident it attends, with a timestamp, coordinates, an incident type and a severity level. This project cleans that log into a collisions-only dataset and then:

- uses clustering (DBSCAN and HDBSCAN, with K-means as a baseline) to detect collision hotspots and rank them by severity;
- uses classification (Decision Tree, Naive Bayes, Logistic Regression and Random Forest) to predict whether a collision is Minor or Serious from its time, type and location;
- compares the high-risk hotspots with the locations of hospitals and ambulance stations, to suggest where and when first responders should be on standby.

The full plan is in [methodology/methodology.md](methodology/methodology.md).

## Repository layout

```
.
├── methodology/
│   └── methodology.md          Overall methodology (CRISP-DM), from data to evaluation
├── src/
│   ├── preprocess.py           Mandatory preprocessing: raw CSV to clean collision table
│   └── category_map.py         Maps Arabic incident categories to English collision groups
├── docs/
│   ├── literature_review.md    Literature review (corrected and checked against sources)
│   ├── sources_for_literature_review.md   Verified reference list
│   ├── datasets.md             Survey of candidate datasets
│   └── preprocessing_log.md    Row counts from the preprocessing run
├── data/
│   └── README.md               How to download the raw data and regenerate the clean file
└── requirements.txt
```

## Data

The source is the **Dubai Police Traffic Incidents** dataset from Data.Dubai (formerly Dubai Pulse). The export used covers 13 Aug 2018 to 7 Oct 2026, with 757,305 records. After preprocessing, 442,690 collisions remain.

The CSV files are not in this repository because they exceed GitHub's file size limit. See [data/README.md](data/README.md) for how to download them.

## Reproducing the preprocessing

Requires Python 3.9 or later.

```bash
git clone https://github.com/SuryanshS70/dubai-road-accident-analysis.git
cd dubai-road-accident-analysis
pip install -r requirements.txt

# Put the raw export in data/raw/ (see data/README.md), then:
python src/preprocess.py data/raw/traffic_incidents_2026-10-09_04-37-34_0001.csv data/processed
```

The script removes duplicates, drops non-collision call-outs (breakdowns, parking, congestion and similar), fixes swapped coordinates, validates timestamps, builds the binary severity target, and adds temporal and spatial features. It prints the rows removed at each step and writes `data/processed/dubai_collisions_clean.csv` and `data/processed/preprocessing_log.md`.

| Step | Rows removed | Rows remaining |
|---|---:|---:|
| Loaded raw file | 0 | 757,305 |
| Dropped exact duplicate rows | 869 | 756,436 |
| Kept latest record per incident ID | 3,259 | 753,177 |
| Kept traffic collisions only | 309,443 | 443,734 |
| Dropped missing or out-of-Dubai coordinates | 1,011 | 442,723 |
| Dropped unparseable or future timestamps | 33 | 442,690 |

Full details are in [docs/preprocessing_log.md](docs/preprocessing_log.md).
