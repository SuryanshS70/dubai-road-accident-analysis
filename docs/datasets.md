# Datasets for Road Accident Hotspot Analysis in Dubai

Researched 9 Oct 2026. "Checked" means the page was opened and read on that date. Dubai Pulse and the UAE open data portal (opendata.fcsc.gov.ae) block automated downloads, so file contents were not opened directly. Record counts come from two published studies that used the same file.

## 1. Accident and incident data

| # | Dataset | Link | Location | Time | Type | Severity | Date range | Size | Format | License | Access | Checked |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A1 | **Dubai Police Traffic Incidents** (`dp_traffic_incidents-open`) | https://www.dubaipulse.gov.ae/data/dp-traffic/dp_traffic_incidents-open | Yes: `acci_x` = latitude, `acci_y` = longitude | Yes: `acci_time` (datetime) | Yes: `acci_name`, an Arabic category such as collision, rollover, pedestrian, motorcycle or hit-and-run | Embedded in `acci_name` as Low/High (has to be parsed from the Arabic text) | Rolling recent window (see note). The page was last updated 06 Dec 2025. | 7.27 MB CSV. One study got about 71k incidents (33.6k collisions) for 5 Nov 2024 to 2 Jun 2025. | CSV, plus an API version | Not specified on the page (Dubai Pulse "Open" classification) | Free download from Dubai Pulse. The page also says you may need to accept the terms or submit a request (confirmed "within 14 days"). The API needs a key and secret sent by email. | Yes |
| A2 | Dubai Police Traffic Incidents API (`dp_traffic_incidents-open-api`) | https://www.dubaipulse.gov.ae/data/dp-traffic/dp_traffic_incidents-open-api | Same fields as A1 | | | | Real-time | n/a | REST API (OAuth bearer token) | Not specified | Key and secret by email after a grant | Yes |
| A3 | Dubai Police Accidents Summary 2011–2016 | https://opendata.fcsc.gov.ae/@dubai-police/accidents-summary | No (aggregate) | Yearly | Summary counts | Likely deaths and injuries (columns not shown on the page) | 2011–2016 | Small | CSV / JSON API | CC BY 4.0 | Free API: `https://opendata.fcsc.gov.ae/api/dataset/accidents-summary` | Yes |
| A4 | Dubai Police casualties by age | https://opendata.fcsc.gov.ae/@dubai-police/statistical-breakdown-of-casualties-by-age | No | 2016 | – | Casualties | 2016 | Small | JSON API | CC BY-SA 4.0 | Free API | Yes |
| A5 | MoI Traffic accidents by emirate and cause | https://opendata.fcsc.gov.ae/@ministry-interior/traffic-accidents-emirate-and-cause-accident | Emirate level only | Year | Cause | – | 2018 | Small | JSON API | CC BY 4.0 | Free API | Yes |
| A6 | MoI Traffic accidents by type of vehicle and emirate | https://opendata.fcsc.gov.ae/@ministry-interior/traffic-accidents-type-vehicle-causing-accident-and-emirate | Emirate level | Year | Vehicle type | – | 2001–2005 and 2007 (no 2004) | Small | JSON API | CC BY 4.0 | Free API | Yes |
| A7 | MoI accidents by nationality, gender and cause | https://opendata.fcsc.gov.ae/@ministry-interior/causers-traffic-accidents-nationality-gender-and-cause-accidents | Country | Year | Cause | – | 2001–2005 (no 2004) | Small | JSON API | CC BY 4.0 | Free API | Yes |
| A8 | MoI Traffic Accidents 2017 (old Bayanat portal) | http://data.bayanat.ae/en_GB/dataset/traffic-accidents | Location text | Yes | Yes | Yes. Also weather, seatbelt use and intoxication. | 2017 | Unknown | CSV | Bayanat open license | **Could not verify.** The old Bayanat site blocks automated access and may be retired (Bayanat moved to opendata.fcsc.gov.ae). Middlesex Dubai has a mirror at www.bit.ly/mdxtrafficdata1. | No |
| A9 | NYU Spatial Data Repository: UAE accidents by emirate, 2005 (series of layers) | https://geo.nyu.edu/catalog/nyu-2451-42165 | Emirate polygons | 2005 | Accident type, driver gender | – | 2005 | Small | Shapefile / GeoJSON | Academic use only | Free download. The repository closes 7 Sep 2026 and records move to NYU UltraViolet. | Yes |
| A10 | RTA Statistical Reports 2011–2016 | https://rta.ae/wps/portal/rta/ae/home/open-data?lang=en | No | Yearly | Some | Deaths/injuries tables | 2011–2016 | PDFs | PDF | RTA | Free download | Yes |

**Update, 9 Oct 2026: the earlier 'rolling window' guess was wrong.** The full export from Data.Dubai (`traffic_incidents_2026-10-09_04-37-34_0001.csv`) covers 13 Aug 2018 to 7 Oct 2026, with 757,305 records. The clean version is `dubai_collisions_clean.csv` (442,690 collisions) in this folder.

Earlier work on A1 that is useful as a reference (and as evidence the data works for this):
- arXiv 2601.12548, *Traffic Collisions: Temporal Patterns and Severity-Weighted Hotspot Analysis* (Dubai, 71,375 incidents, Getis-Ord Gi*, chi-square on severity): https://arxiv.org/html/2601.12548v1
- GitHub: Crash Hotspot Detection in Dubai using DBSCAN (MIT license, notebook included, CSV not included): https://github.com/Najma-Abdulkarim-Nor/Crash-Hotspot-Detection-in-Dubai-Using-Spatial-Clustering-and-Road-Level-Analysis

Kaggle: no Dubai-specific accident dataset was found. Kaggle search results could not be read automatically, and no Dubai mirror showed up in web search.

## 2. Supporting data for enrichment

| # | Dataset | Link | What it adds | Date range / updated | Size | Format | License | Access | Checked |
|---|---|---|---|---|---|---|---|---|---|
| S1 | OpenStreetMap GCC extract (Geofabrik) | https://download.geofabrik.de/asia/gcc-states.html | Road network (road class, speed, lanes), junctions, hospitals (`amenity=hospital`), ambulance stations (`emergency=ambulance_station`), fuel stations, etc. Crop to Dubai. | Daily (data up to 8 Oct 2026) | 242 MB PBF, 480 MB shapefile | PBF / Shapefile / GeoPackage | ODbL 1.0 | Free. For Dubai only, use OSMnx (`ox.graph_from_place("Dubai")`) or Overpass instead. | Yes |
| S2 | Dubai Police speed and radar limits by street | https://www.dubaipulse.gov.ae/data/dp-traffic/dp_speed_and_radar_limits-open | Street name, lane count, speed limit and radar limit (Arabic), to join with the nearest road | Updated 15 Sep 2022 | Small | CSV | Not specified | Dubai Pulse download | Yes |
| S3 | Dubai Municipality community boundaries (`dm_community-open`) | https://www.dubaipulse.gov.ae/data/dm-location/dm_community-open | Polygons of Dubai's communities (Arabic and English names), for counting accidents per area | Updated 20 Jun 2021 | 1.8 MB | KML | Not specified | Dubai Pulse download or request | Yes |
| S4 | DLD community lookup (`dld_lkp_areas-open`) | https://www.dubaipulse.gov.ae/data/dld-transactions/dld_lkp_areas-open | Community IDs and names (Arabic/English) and municipality code | Updated 3 Oct 2025 | 0.02 MB | CSV | Not specified | Dubai Pulse | Yes |
| S5 | DSC population by community | https://www.dubaipulse.gov.ae/data/dsc-statistics/dsc_population_by_community-open | Population for accident-rate normalisation | Unknown | Small | CSV | Not specified | Dubai Pulse | Found by search only (page blocks automated reading) |
| S6 | DHA active health facilities (`dha_sheryan_facility_detail-open`) | https://www.dubaipulse.gov.ae/data/dha-location/dha_sheryan_facility_detail-open | Hospital and clinic list, for distance from hotspots to the nearest hospital. Whether it has coordinates is unconfirmed. If not, use OSM hospitals (S1). | Updated 5 Dec 2025 | Unknown | CSV (and API) | Not specified | Dubai Pulse | Listing page checked, dataset page blocks automated reading |
| S7 | Ambulance stations | No open dataset. DCAS on Dubai Pulse lists no datasets: https://www.dubaipulse.gov.ae/organisation/dcas | Ambulance points | – | – | – | – | Use OSM `emergency=ambulance_station` (S1), and fill gaps by hand from DCAS news (for example, new points in Jebel Ali, Al Quoz, International City and Al Qusais) | Yes |
| S8 | Open-Meteo Historical Weather API | https://open-meteo.com/en/docs/historical-weather-api | Hourly rain, temperature, humidity, wind and gusts (no visibility). Join on accident hour, for "conditions" analysis such as rain days. | 1940 to present | – | JSON/CSV via URL | Free for non-commercial use, no key needed | Free | Yes |
| S9 | Meteostat, Dubai International (OMDB, WMO 41194) | https://meteostat.net/en/station/41194 | Station hourly observations (temperature, rain, wind, pressure) | Hourly 1983 to Oct 2026 | – | CSV export, Python library `meteostat` | Data from NOAA/DWD (Meteostat bulk data is CC BY-NC 4.0) | Free | Yes |
| S10 | NOAA ISD Global Hourly, station 41194099999 | https://www.ncei.noaa.gov/access/search/data-search/global-hourly?stations=41194099999 | Hourly METAR including **visibility** (useful for fog) | Decades | – | CSV | US public domain | Free | Page loads, but contents not readable automatically |

## 3. Recommended starting point

1. **Download A1 (Dubai Police Traffic Incidents) first.** It is the only source with point coordinates, timestamp, incident type and severity, and the hotspot analysis needs all of them. The download window seems to roll, so grab it now.
2. Translate and parse `acci_name` (Arabic) into `collision_type` and `severity` (Low/High). Filter to collisions and drop points outside Dubai.
3. Enrich with S3 (communities), S1 (roads and hospitals via OSMnx) and S8 (hourly weather).
4. Use A3 and A10 only for long-term context in the introduction or EDA.

## 4. Topic check against the banned list

**Verdict: allowed.** "Road Accident Hotspot Analysis in Dubai" is not on the list.

How it compares with the closest entries:
- **Crime pattern Analysis and hotspot prediction.** This is the only real overlap, and the overlap is the word "hotspot" and the clustering method. The subject is different: road traffic collisions are a road-safety and emergency-response problem, not crime. Most collisions involve no offence. The risk is that a grader skims the title, sees "hotspot", and matches it to the crime topic.
- **Crime Rate Prediction.** Different subject and task.
- **Smart Traffic Signal Control using RL** and **Traffic Sign Recognition.** Same broad traffic area, but those are control and computer-vision tasks. This project uses no signals, no images and no RL.
- **Driver Drowsiness Detection** (three variants). Driver monitoring with computer vision, so unrelated.
- **Flight Delay Prediction** and **Predicting Air Quality Index.** Unrelated.

Framing that keeps the topic clearly separate:
1. Put "collision" and "emergency response" in the title, and drop "prediction" next to "hotspot". For example: **"Spatio-Temporal Mining of Road Traffic Collisions in Dubai for Emergency Response Planning"** or **"Road Collision Hotspots and Severity Patterns in Dubai: A Data Mining Approach to Ambulance Placement"**.
2. Make two things central that a crime project would not have:
   - **Severity classification**: predict Low or High severity from time, collision type, road class and weather.
   - **Emergency-response coverage**: measure each hotspot's distance to the nearest hospital or ambulance point, and suggest better placements, for example with k-means or p-median on cluster centroids.
3. Use road-safety terms: collision, road segment, severity and response coverage, rather than incident, offence or patrol.
4. The list says it "will grow", so get the instructor's OK on the final title in writing.
