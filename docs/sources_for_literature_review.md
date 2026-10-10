# Sources for the literature review (verified)

## Verification note

Checked on 9 Oct 2026. Every entry below was compared with an original record:
- the paper's own page (arXiv, the publisher, or the university portal),
- the publisher's metadata through the Crossref DOI registry, or
- the dataset's own portal page.

Authors, year, title, venue, volume, issue, pages and DOI were all checked, as were the figures quoted from each study.

Status labels:
- **Verified (primary).** Confirmed on the original or publisher record.
- **Verified (secondary).** The primary page could not be opened from here, so the citation was confirmed against a reliable reference list instead (named in the entry). Open the primary link once before submitting.
- **Not independently verified.** Stated in the source itself, but not confirmable elsewhere.

Changes from the earlier version of this list:
- Source 2: the authors were wrong. It was listed as "N. Abdulkarim Nor", which is only the GitHub username.
- Source 3: the author, volume, article number and DOI were added.
- The CRISP-DM guide: the publisher was wrong. It is the CRISP-DM Consortium, not SPSS.
- Pages and DOIs were added throughout.

## A. Prior studies on road accidents in Dubai and the UAE

**1. Alsaleh, N., Falis, N., Alsaleh, T., & Ba Fakih, F. (2026). Traffic collisions: Temporal patterns and severity-weighted hotspot analysis. arXiv:2601.12548 [cs.CE]. https://arxiv.org/abs/2601.12548** (Verified, primary)
- This is a preprint (v1, 18 Jan 2026) with no journal publication listed, so cite it as a preprint.
- Data: Dubai Police traffic incidents from Dubai Pulse, 5 Nov 2024 to 2 Jun 2025. There were 71,375 incidents, of which 33,604 (about 47%) were collisions.
- Severity has two levels: Low (weight 1) and High (weight 2).
- Methods: chi-square tests with Cramér's V, a severity-weighted Getis-Ord Gi* hotspot analysis, and IDW interpolation.
- Relevance: the closest prior work, with the same data source and city. This project differs in four ways:
  - it covers Aug 2018 to Oct 2026 instead of 7 months;
  - it uses DBSCAN clustering;
  - it adds a severity classifier;
  - it adds emergency-response analysis.

**2. Alblooshi, M., Nour, N., & Elgazzar, K. (2026). Crash hotspot detection in Dubai using spatial clustering and road-level analysis [Source code and paper, GitHub repository, MIT License]. https://github.com/Najma-Abdulkarim-Nor/Crash-Hotspot-Detection-in-Dubai-Using-Spatial-Clustering-and-Road-Level-Analysis** (Repository verified, primary. Conference paper not independently verified.)
- The README says the paper appears at the 2026 IEEE International Conference on Smart Mobility (SM2026), 11–13 May 2026, Al Alamein City, Egypt. The paper's DOI, 10.1109/SM69703.2026.11614141, resolves to IEEE Xplore document 11614141, but that page could not be read from here. Copy the exact title and authors from IEEE Xplore before citing it.
- Data: Dubai Police traffic incidents, 14–30 March 2026 (a 16-day window).
  - The record count is not consistent: the demo says 5,256 incidents, while the README says "~5,000". Quote 5,256, or say "about 5,000".
- Methods: DBSCAN with haversine distance (ε = 200 m, minPts = 4), producing 302 clusters. Also keyword-based severity weights (minor = 1, moderate = 2, severe = 3) and 2-hour peak windows.
- Relevance: shows DBSCAN works on this data. The authors note a lack of detailed road-network data, which this project can address with OpenStreetMap.

**3. Alkaabi, K. (2023). Identification of hotspot areas for traffic accidents and analyzing drivers' behaviors and road accidents. *Transportation Research Interdisciplinary Perspectives, 22*, 100929. https://doi.org/10.1016/j.trip.2023.100929** (Verified, primary: UAE University research portal)
- Data: 2014 crash data for Abu Dhabi city, plus a 2017 questionnaire of 1,072 drivers involved in road accidents.
- Methods: GIS spatial autocorrelation using Getis-Ord Gi* to identify and rank hotspots (concentrated near the central business district), and logistic regression on the survey responses.
- Relevance: a UAE precedent for GIS-based hotspot analysis.

## B. Datasets

**4. Dubai Police. (2026). *Traffic Incidents* [Data set]. Data.Dubai (formerly Dubai Pulse).** Data file used: `traffic_incidents_2026-10-09_04-37-34_0001.csv`, downloaded by the team on 9 Oct 2026. It holds 757,305 records from 13 Aug 2018 to 7 Oct 2026, counted directly from the file. (Verified, primary)
- Cite Data.Dubai and the download date, since that is where the file came from. Give the exact Data.Dubai page address: it appears in the browser address bar on the dataset page (search "Traffic Incidents", publisher Dubai Police). That address could not be opened from here, because this project's network blocks the site.
- The older Dubai Pulse page for the same dataset was opened and checked: https://www.dubaipulse.gov.ae/data/dp-traffic/dp_traffic_incidents-open. It lists the fields `acci_id`, `acci_time`, `acci_name`, `acci_x` and `acci_y`, created 13 Aug 2018.

**5. Dubai Police. (2022). *Accidents summary* (2011–2016) [Data set]. UAE Open Data portal. CC BY 4.0. https://opendata.fcsc.gov.ae/@dubai-police/accidents-summary** (Verified, primary. Columns not shown on the page.)

**6. Dubai Police. (2022). *Statistical breakdown of casualties – by age* (2016) [Data set]. UAE Open Data portal. CC BY-SA 4.0. https://opendata.fcsc.gov.ae/@dubai-police/statistical-breakdown-of-casualties-by-age** (Verified, primary)

**7. Ministry of Interior. (2022). *Traffic accidents according to the emirate and cause of the accident* (2018) [Data set]. UAE Open Data portal. CC BY 4.0. https://opendata.fcsc.gov.ae/@ministry-interior/traffic-accidents-emirate-and-cause-accident** (Verified, primary)

**8. Ministry of Interior. (2022). *Traffic accidents according to the type of vehicle causing accident and the emirate* (2001–2005 and 2007; no 2004) [Data set]. UAE Open Data portal. CC BY 4.0. https://opendata.fcsc.gov.ae/@ministry-interior/traffic-accidents-type-vehicle-causing-accident-and-emirate** (Verified, primary)

**9. Ministry of Interior. (2022). *Number of traffic accidents categorized by the nationality, gender and cause of the accident* (2001–2005; no 2004) [Data set]. UAE Open Data portal. CC BY 4.0. https://opendata.fcsc.gov.ae/@ministry-interior/causers-traffic-accidents-nationality-gender-and-cause-accidents** (Verified, primary)

**10. Dubai Data and Statistics Establishment. Data sets on Data.Dubai.
https://data.dubai/en/l/469979

**11. Roads and Transport Authority (RTA). *Statistical reports* 2011–2016 [PDF reports]. https://rta.ae/wps/portal/rta/ae/home/open-data?lang=en** (Verified, primary) The open-data page lists four reports: 2011, 2012, 2013, and a combined 2014–2016 report.

**12. NYU Spatial Data Repository. (2018). *Type of traffic accidents in each emirate of the United Arab Emirates, 2005* [Shapefile]. https://geo.nyu.edu/catalog/nyu-2451-42165** (Verified, primary) The record says it is for academic use only. The repository was due to be discontinued on 7 Sep 2026, with records moving to NYU UltraViolet, but the link still worked on 9 Oct 2026.

**13. Middlesex University Dubai. *25 UAE datasets* [PDF list of teaching datasets]. https://api.mdx.ac.ae/uploads/25_uae_datasets_amazing_e4a1182519.pdf** (Verified, primary) It lists the Dubai Police traffic incidents dataset (its D8). Its author and year were not checked, so take them from the PDF itself if it is cited.

## C. Supporting data sources

**14. OpenStreetMap contributors. (2026). *GCC States extract* [Data set]. Geofabrik GmbH. ODbL 1.0. https://download.geofabrik.de/asia/gcc-states.html** (Verified, primary)

**15. Dubai Police. *Drivers guide to speed and radar limits on selected streets* [Data set]. Dubai Pulse. https://www.dubaipulse.gov.ae/data/dp-traffic/dp_speed_and_radar_limits-open** (Verified, primary) Last updated 15 Sep 2022.

**16. Dubai Municipality. *Community boundaries* (`dm_community-open`) [KML data set]. Dubai Pulse. https://www.dubaipulse.gov.ae/data/dm-location/dm_community-open** (Verified, primary)

**17. Open-Meteo. *Historical Weather API*. https://open-meteo.com/en/docs/historical-weather-api** (Verified, primary) It is based on ERA5 (see Hersbach et al., 2020, below).

**18. Meteostat. *Dubai International Airport weather station (WMO 41194)*. https://meteostat.net/en/station/41194** (Verified, primary) The page credits NOAA, Deutscher Wetterdienst and Environment Canada as its data sources.

## D. Method references

All of these were confirmed through Crossref DOI metadata, the publisher's page, or the official journal page, except where marked.

| Method | Reference | Status |
|---|---|---|
| CRISP-DM | Chapman, P., Clinton, J., Kerber, R., Khabaza, T., Reinartz, T., Shearer, C., & Wirth, R. (2000). *CRISP-DM 1.0: Step-by-step data mining guide.* CRISP-DM Consortium (NCR, DaimlerChrysler, SPSS, OHRA). | Verified, primary (the guide's own PDF). The earlier list wrongly gave the publisher as SPSS. |
| DBSCAN | Ester, M., Kriegel, H.-P., Sander, J., & Xu, X. (1996). A density-based algorithm for discovering clusters in large spatial databases with noise. In E. Simoudis, J. Han, & U. M. Fayyad (Eds.), *Proceedings of the Second International Conference on Knowledge Discovery and Data Mining (KDD-96)* (pp. 226–231). AAAI Press. | Verified, secondary (Wikipedia reference list). The AAAI page refused the request (rate limit). |
| HDBSCAN | Campello, R. J. G. B., Moulavi, D., & Sander, J. (2013). Density-based clustering based on hierarchical density estimates. In J. Pei et al. (Eds.), *Advances in Knowledge Discovery and Data Mining (PAKDD 2013)*, Lecture Notes in Computer Science, vol. 7819 (pp. 160–172). Springer. https://doi.org/10.1007/978-3-642-37456-2_14 | Verified, primary |
| K-means | MacQueen, J. (1967). Some methods for classification and analysis of multivariate observations. In *Proceedings of the Fifth Berkeley Symposium on Mathematical Statistics and Probability*, Vol. 1 (pp. 281–297). University of California Press. | Verified, secondary (Wikipedia reference list, MR 0214227). Project Euclid blocked automated access. |
| Silhouette | Rousseeuw, P. J. (1987). Silhouettes: A graphical aid to the interpretation and validation of cluster analysis. *Journal of Computational and Applied Mathematics, 20*, 53–65. https://doi.org/10.1016/0377-0427(87)90125-7 | Verified, primary |
| Davies–Bouldin index | Davies, D. L., & Bouldin, D. W. (1979). A cluster separation measure. *IEEE Transactions on Pattern Analysis and Machine Intelligence, PAMI-1*(2), 224–227. https://doi.org/10.1109/TPAMI.1979.4766909 | Verified, primary |
| DBCV | Moulavi, D., Jaskowiak, P. A., Campello, R. J. G. B., Zimek, A., & Sander, J. (2014). Density-based clustering validation. In *Proceedings of the 2014 SIAM International Conference on Data Mining* (pp. 839–847). https://doi.org/10.1137/1.9781611973440.96 | Verified, primary |
| Getis-Ord Gi* | Getis, A., & Ord, J. K. (1992). The analysis of spatial association by use of distance statistics. *Geographical Analysis, 24*(3), 189–206. https://doi.org/10.1111/j.1538-4632.1992.tb00261.x | Verified, primary |
| Getis-Ord Gi* (local form) | Ord, J. K., & Getis, A. (1995). Local spatial autocorrelation statistics: Distributional issues and an application. *Geographical Analysis, 27*(4), 286–306. https://doi.org/10.1111/j.1538-4632.1995.tb00912.x | Verified, primary |
| Kernel density estimation | Silverman, B. W. (1986). *Density estimation for statistics and data analysis.* Chapman & Hall. | Verified, secondary (Wikipedia reference list). Crossref has only the 2018 Routledge reissue (https://doi.org/10.1201/9781315140919). |
| Decision trees (CART) | Breiman, L., Friedman, J. H., Olshen, R. A., & Stone, C. J. (1984). *Classification and regression trees.* Wadsworth. | Verified, secondary (Wikipedia reference list). Crossref has only the 2017 Chapman & Hall/CRC reissue (https://doi.org/10.1201/9781315139470). |
| Random Forest | Breiman, L. (2001). Random forests. *Machine Learning, 45*(1), 5–32. https://doi.org/10.1023/A:1010933404324 | Verified, primary |
| SMOTE | Chawla, N. V., Bowyer, K. W., Hall, L. O., & Kegelmeyer, W. P. (2002). SMOTE: Synthetic minority over-sampling technique. *Journal of Artificial Intelligence Research, 16*, 321–357. https://doi.org/10.1613/jair.953 | Verified, primary |
| Cramér's V | Cramér, H. (1946). *Mathematical methods of statistics.* Princeton University Press. https://doi.org/10.1515/9781400883868 | Verified, primary |
| scikit-learn | Pedregosa, F., Varoquaux, G., Gramfort, A., et al. (2011). Scikit-learn: Machine learning in Python. *Journal of Machine Learning Research, 12*, 2825–2830. | Verified, primary (JMLR page; 16 authors) |
| OSMnx | Boeing, G. (2017). OSMnx: New methods for acquiring, constructing, analyzing, and visualizing complex street networks. *Computers, Environment and Urban Systems, 65*, 126–139. https://doi.org/10.1016/j.compenvurbsys.2017.05.004 | Verified, primary (arXiv record and the package's own citation). OSMnx's author now also points to a newer paper: Boeing, G. (2025). Modeling and analyzing urban networks and amenities with OSMnx. *Geographical Analysis, 57*(4), 567–577. https://doi.org/10.1111/gean.70009 |
| ERA5 | Hersbach, H., et al. (2020). The ERA5 global reanalysis. *Quarterly Journal of the Royal Meteorological Society, 146*(730), 1999–2049. https://doi.org/10.1002/qj.3803 | Verified, primary (43 authors) |

## Suggested structure for the literature review

1. Road traffic accidents as an urban safety problem in the UAE and Dubai. Use sources 5–11.
2. Spatial hotspot methods: KDE, Getis-Ord Gi* and density-based clustering. Cite sources 1–3 and section D.
3. Crash severity classification: decision trees, random forests, and handling class imbalance (SMOTE).
4. Prior Dubai and UAE work (sources 1–3) and the gap this project fills: an 8-year span, clustering combined with severity classification, and emergency-response placement.
