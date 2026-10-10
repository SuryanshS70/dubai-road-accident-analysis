# Literature review: reference draft (not the report section)

> A reference aid for the team member writing the literature review. It is not the final section of the report. Checked on 9 Oct 2026 against the original sources. The list of changes and the two items to confirm are at the end of this file.

## 1. Road Traffic Accidents in Dubai and the UAE

Road traffic accidents remain a significant urban safety concern in Dubai. Dubai Police publishes summary accident statistics for 2011–2016 [1], and the Ministry of Interior reports accidents by emirate and cause for 2018 [2]. The Dubai Police Traffic Incidents dataset provides incident-level records with timestamps and coordinates from August 2018 to October 2026, enabling longitudinal spatial and temporal analysis [3].

## 2. Spatial Hotspot Detection

Alsaleh et al. [4] analysed Dubai traffic collisions recorded between November 2024 and June 2025. They used chi-square tests with Cramér's V for temporal associations with severity, a severity-weighted Getis–Ord Gi* hotspot analysis, and inverse distance weighting (IDW) interpolation. Alblooshi et al. [5] applied DBSCAN clustering and severity-weighted risk scoring to a 16-day window of Dubai incident data to identify collision hotspots. Alkaabi [6] identified traffic accident hotspots in Abu Dhabi using GIS-based Getis–Ord Gi* analysis, and applied logistic regression to a survey of drivers involved in accidents.

Established spatial analysis techniques include kernel density estimation (KDE) [7], Getis–Ord spatial statistics [8], [9], DBSCAN [10] and HDBSCAN [11]. K-means [12] provides a clustering baseline. Cluster quality can be evaluated using silhouette scores [13], the Davies–Bouldin index [14] and density-based clustering validation (DBCV) [15].

## 3. Accident Severity Classification

Classification and regression trees (CART) [16] and random forests [17] are established supervised classification methods that can be applied to accident-severity prediction. Class imbalance can be addressed using the Synthetic Minority Over-sampling Technique (SMOTE) [18].

In the Dubai Police data, severity is recorded as part of the Arabic incident category (minor, moderate or severe), and the data also contains non-collision incidents such as vehicle breakdowns. Collision records and their severity labels must therefore be extracted before classification [3].

## 4. Road Networks and Emergency Response

OpenStreetMap road-network data [19] and OSMnx [20] support network-based accessibility and routing analysis. Dubai Police speed-limit data [21], Dubai Municipality community boundaries [22] and historical weather records [23], [24] provide supplementary geographic and environmental information.

## 5. Research Gap

Existing UAE research mainly examines accident patterns, hotspot identification and driver behaviour [4]–[6]. Prior Dubai studies cover short periods: about seven months in [4] and 16 days in [5]. This project extends previous work through:

1. Longitudinal analysis of Dubai traffic incidents from 2018 to 2026.
2. Spatial clustering combined with accident-severity classification.
3. Road-network analysis for potential emergency-response placement and accessibility assessment.

The project follows the CRISP-DM framework [25], with the machine-learning implementation supported by scikit-learn [26].

## References

### A. UAE Traffic Studies and Datasets

[1] Dubai Police, "Accidents summary for years 2011 to 2016," UAE Open Data Portal. [Online]. Available: https://opendata.fcsc.gov.ae/@dubai-police/accidents-summary

[2] Ministry of Interior, "Traffic accidents according to the emirate and cause of the accident," UAE Open Data Portal, 2018. [Online]. Available: https://opendata.fcsc.gov.ae/@ministry-interior/traffic-accidents-emirate-and-cause-accident

[3] Dubai Police, "Traffic incidents," Data.Dubai (formerly Dubai Pulse), dataset `dp_traffic_incidents-open`. [Online]. Available: https://www.dubaipulse.gov.ae/data/dp-traffic/dp_traffic_incidents-open. Accessed: Oct. 9, 2026.

[4] N. Alsaleh, N. Falis, T. Alsaleh, and F. Ba Fakih, "Traffic collisions: Temporal patterns and severity-weighted hotspot analysis," arXiv preprint arXiv:2601.12548, 2026, doi: 10.48550/arXiv.2601.12548.

[5] M. Alblooshi, N. Nour, and K. Elgazzar, "[confirm exact title on IEEE Xplore]," in *Proc. 2026 IEEE Int. Conf. Smart Mobility (SM)*, Al Alamein City, Egypt, 2026, doi: 10.1109/SM69703.2026.11614141.

[6] K. Alkaabi, "Identification of hotspot areas for traffic accidents and analyzing drivers' behaviors and road accidents," *Transportation Research Interdisciplinary Perspectives*, vol. 22, Art. no. 100929, 2023, doi: 10.1016/j.trip.2023.100929.

### B. Spatial Analysis and Clustering

[7] B. W. Silverman, *Density Estimation for Statistics and Data Analysis*. London, U.K.: Chapman and Hall, 1986.

[8] A. Getis and J. K. Ord, "The analysis of spatial association by use of distance statistics," *Geographical Analysis*, vol. 24, no. 3, pp. 189–206, 1992, doi: 10.1111/j.1538-4632.1992.tb00261.x.

[9] J. K. Ord and A. Getis, "Local spatial autocorrelation statistics: Distributional issues and an application," *Geographical Analysis*, vol. 27, no. 4, pp. 286–306, 1995, doi: 10.1111/j.1538-4632.1995.tb00912.x.

[10] M. Ester, H.-P. Kriegel, J. Sander, and X. Xu, "A density-based algorithm for discovering clusters in large spatial databases with noise," in *Proc. 2nd Int. Conf. Knowledge Discovery and Data Mining (KDD-96)*. AAAI Press, 1996, pp. 226–231.

[11] R. J. G. B. Campello, D. Moulavi, and J. Sander, "Density-based clustering based on hierarchical density estimates," in *Advances in Knowledge Discovery and Data Mining (PAKDD 2013)*, Lecture Notes in Computer Science, vol. 7819. Berlin, Heidelberg: Springer, 2013, pp. 160–172, doi: 10.1007/978-3-642-37456-2_14.

[12] J. MacQueen, "Some methods for classification and analysis of multivariate observations," in *Proc. 5th Berkeley Symp. Mathematical Statistics and Probability*, vol. 1. University of California Press, 1967, pp. 281–297.

[13] P. J. Rousseeuw, "Silhouettes: A graphical aid to the interpretation and validation of cluster analysis," *Journal of Computational and Applied Mathematics*, vol. 20, pp. 53–65, 1987, doi: 10.1016/0377-0427(87)90125-7.

[14] D. L. Davies and D. W. Bouldin, "A cluster separation measure," *IEEE Transactions on Pattern Analysis and Machine Intelligence*, vol. PAMI-1, no. 2, pp. 224–227, 1979, doi: 10.1109/TPAMI.1979.4766909.

[15] D. Moulavi, P. A. Jaskowiak, R. J. G. B. Campello, A. Zimek, and J. Sander, "Density-based clustering validation," in *Proc. 2014 SIAM Int. Conf. Data Mining (SDM)*, 2014, pp. 839–847, doi: 10.1137/1.9781611973440.96.

### C. Classification Methods

[16] L. Breiman, J. H. Friedman, R. A. Olshen, and C. J. Stone, *Classification and Regression Trees*. Wadsworth, 1984.

[17] L. Breiman, "Random forests," *Machine Learning*, vol. 45, no. 1, pp. 5–32, 2001, doi: 10.1023/A:1010933404324.

[18] N. V. Chawla, K. W. Bowyer, L. O. Hall, and W. P. Kegelmeyer, "SMOTE: Synthetic minority over-sampling technique," *Journal of Artificial Intelligence Research*, vol. 16, pp. 321–357, 2002, doi: 10.1613/jair.953.

### D. Supporting Geospatial and Environmental Data

[19] OpenStreetMap contributors, "GCC States OpenStreetMap extract," Geofabrik GmbH, ODbL 1.0. [Online]. Available: https://download.geofabrik.de/asia/gcc-states.html. Accessed: Oct. 9, 2026.

[20] G. Boeing, "OSMnx: New methods for acquiring, constructing, analyzing, and visualizing complex street networks," *Computers, Environment and Urban Systems*, vol. 65, pp. 126–139, 2017, doi: 10.1016/j.compenvurbsys.2017.05.004.

[21] Dubai Police, "Drivers guide to speed and radar limits on selected streets," Dubai Pulse (now Data.Dubai), dataset `dp_speed_and_radar_limits-open`. [Online]. Available: https://www.dubaipulse.gov.ae/data/dp-traffic/dp_speed_and_radar_limits-open

[22] Dubai Municipality, "Community boundaries," Dubai Pulse (now Data.Dubai), dataset `dm_community-open`. [Online]. Available: https://www.dubaipulse.gov.ae/data/dm-location/dm_community-open

[23] Open-Meteo, "Historical Weather API." [Online]. Available: https://open-meteo.com/en/docs/historical-weather-api. Accessed: Oct. 9, 2026.

[24] H. Hersbach *et al.*, "The ERA5 global reanalysis," *Quarterly Journal of the Royal Meteorological Society*, vol. 146, no. 730, pp. 1999–2049, 2020, doi: 10.1002/qj.3803.

### E. Data Mining Framework and Software

[25] P. Chapman, J. Clinton, R. Kerber, T. Khabaza, T. Reinartz, C. Shearer, and R. Wirth, *CRISP-DM 1.0: Step-by-Step Data Mining Guide*. CRISP-DM Consortium, 2000.

[26] F. Pedregosa *et al.*, "Scikit-learn: Machine learning in Python," *Journal of Machine Learning Research*, vol. 12, pp. 2825–2830, 2011.

---

## Changes made to the original draft

**Text**
1. **Section 1, [2]:** added "for 2018". The Ministry of Interior dataset covers that year only.
2. **Section 1, [3]:** "2018–2026" is correct (13 Aug 2018 to 7 Oct 2026, counted from the file). I made it "from August 2018 to October 2026" and noted that the records have timestamps and coordinates.
3. **Section 2, [4]:** "temporal association analysis" is now the actual methods: chi-square with Cramér's V, and a severity-weighted Gi*. I also added the study period.
4. **Section 2, [5]:** added that it used a 16-day window of data.
5. **Section 2, [6]:** the draft said logistic regression was applied to the accidents. Alkaabi applied it to a survey of drivers, and the hotspots came from Getis–Ord Gi*.
6. **Section 3:** "provide established methods for supervised accident-severity classification" implied that [16] and [17] are about accidents. They are general methods, so the sentence now says they "can be applied to" accident severity. The uncited sentence about severity labels now states what the data actually contains and cites [3].
7. **Section 5:** added how short the earlier Dubai studies' periods were, which supports the "longitudinal" gap.

**References**
8. **[1]:** the title now matches the portal ("Accidents summary for years 2011 to 2016").
9. **[2]:** the title now matches the portal.
10. **[3]:** the link is to the Dubai Pulse page, so the entry now reads "Data.Dubai (formerly Dubai Pulse)". The draft said Data.Dubai only.
11. **[5]:** the DOI 10.1109/SM69703.2026.11614141 resolves to IEEE Xplore document 11614141, so the paper exists, but its page could not be read from here. The draft's title, "Crash hotspot detection in Dubai using DBSCAN and severity weighting", does not match the authors' repository title ("Crash Hotspot Detection in Dubai Using Spatial Clustering and Road-Level Analysis"). The repository README gives the second author as "Najma Nour", not "N. A. Nour". **Open the DOI link and copy the exact title and author names.**
12. **[10]:** added the publisher, AAAI Press.
13. **[11]:** added PAKDD 2013, the Lecture Notes in Computer Science series name, and the publisher.
14. **[12]:** added the publisher, University of California Press.
15. **[14], [17] and [18]:** added the missing DOIs. [26] has no DOI, because JMLR does not issue them, so it is correct as it is.
16. **[16]:** removed "Belmont, CA". The edition and place could not be confirmed: one catalogue lists Monterey, CA (Wadsworth & Brooks/Cole). Use "Wadsworth, 1984" unless you check the copy you cite.
17. **[21]:** the title now matches the dataset's real name, and the entry says Dubai Pulse, to match the link.
18. **[22]:** the entry now says Dubai Pulse, to match the link.
19. **[19] and [23]:** added access dates.
20. **[25]:** the publisher is the CRISP-DM Consortium (NCR, DaimlerChrysler, SPSS, OHRA), not SPSS Inc., as stated in the guide itself. I also listed all seven authors.

**Still to confirm by hand**
- **[5]:** the exact title and author names on IEEE Xplore (see item 11).
- **[10], [12], [7] and [16]:** these were confirmed only against a secondary reference list, because the primary pages blocked automated access. Glance at each before submitting.
