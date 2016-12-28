## Role of Temporal Diversity in Inferring Social Ties Based on Spatio-Temporal Data

### Abstract
*The last two decades have seen a tremendous surge in research on social networks and their implications. The studies includes inferring social relationships, which in turn have been used for target advertising, recommendations, search customization etc. However, the offline experiences of human, the conversations with people and face-to-face interactions that govern our lives interactions have received lesser attention. We introduce DAIICT Spatio-Temporal Network (DSSN), a spatiotemporal dataset of 0.7 million data points of continuous location data logged at an interval of every 2 minutes by mobile phones of 46 subjects. Our research is focused at inferring relationship strength between students based on the spatiotemporal data and comparing the results with the self-reported data. In that pursuit we  introduce Temporal Diversity, which we show to be superior in its contribution to predicting relationship strength than its counterparts. We also explore the evolving nature of Temporal Diversity with time. Our rich dataset opens various other avenues of research that require fine-grained location data with bounded movement of participants within a limited geographical area. The advantage of having a bounded geographical area such as a university campus is that it provides us with a microcosm of the real world, where each such geographic zone has an internal context and function and a high percentage of mobility is governed by schedules and time-tables. The bounded geographical region in addition to the age homogeneous population gives us a minute look into the active internal socialization of students in a university.*

---

The link to our research paper is : [https://arxiv.org/abs/1611.03298](https://arxiv.org/abs/1611.03298). The paper is accepted at ACM IKDD Conference on Data Science, 2017.

### DSSN: Dataset

The dataset introduced in this paper is DSSN (DAIICT Spatio-Temporal Network), a link to the same is: [https://github.com/deshanadesai/Geospat/blob/master/Dataset.csv.tar.gz](https://github.com/deshanadesai/Geospat/blob/master/Dataset.csv.tar.gz)
The link cannot be viewed raw but you can download the file. The self reported survey complementing this dataset is available at: [Coming Soon]()

For each user, the timestamp, latitude and longitude, elevation, accuracy, satellites, network provider is recorded at a regular interval of 1 minute. The total number of data points reported in this dataset are 6,59,268 (this data is publicly available and used for the following analysis in the paper). The total number of subjects using the application to record data are 74, however with cleaning based on quality checks, we reduce the number to 46. The data recorded varies in accuracy with an average accuracy of 36.0 meters.

The subjects from this study consisted of students pursuing B-Tech ICT at DAIICT (Dhirubhai Ambani Institute of Information and Communication Technology), a university located in Gujarat, India. It has a residential campus which spans 60 acres and houses approximately 1,500 students. The subjects volunteered to become part of the experiment.

The data was collected from the subjects between the months of March and May, 2016. For this paper’s analyses, we used a subset of the data collected during the month of April, 2016. Out of the 46 subjects previously mentioned, that participated in the study, 36 completed the survey conducted in July, 2016. 

The data was collected from the Android-based mobile phones of the subjects. The subjects installed the [GPS-Logger app](https://play.google.com/store/apps/details?id=com.crearo.gpslogger) which is available on playstore. The application exploits the GPS capabilities of the mobile phones to log co-ordinates and runs as a background process at all times.

We conducted an online survey for the subjects who participated in the DSSN data collection. The survey is detailed and focuses on questions to report strength of friendship and estimated average proximity with each subject. It also includes general questions regarding the subjects’ social behaviour, participation in various activities, anxiety levels, academic performance etc.

For more details, please visit the paper. Thank You.

### Demo

More statistics and visualizations on the dataset coming soon!

Please feel free to contact us in case of any queries.
