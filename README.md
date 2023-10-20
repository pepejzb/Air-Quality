# Barcelona City Air Quality

## Objective
The objective of this project is to visualize the different air quality states, differentiated by the present pollutant. Additionally, pollutants will be analyzed according to their concentration levels in each district of the city of Barcelona. Natural factors that may have an influence, such as the area of green spaces and the number of trees per hectare, will be included in the analysis.
An attempt will be made to create a predictive model to determine whether the air quality is acceptable or not.

### About the data
This project basically relies on 3 sources of information: Air pollutant measurements (API), tree census (3 datasets in CSV format), and green areas (1 dataset in CSV format). Data related to the districts that were studied have also been downloaded through web scraping.

Apart from data analysis and machine learning modeling, files have also been directly incorporated into Tableau to precisely visualize the situation of the city of Barcelona in comparison to other cities in Spain and the European Union.

Additionally, information from the Ministry of Health is included (edcm_2022.pdf), which contains data on mortality in Spain and the most frequent causes. This aims to raise awareness of the impact that air quality has on people's health.

Furthermore, there is information that was directly included in the visualization (https://isglobalranking.org/es/ranking/espana#air), corresponding to the analysis of two pollutants (NO2 and PM2.5), which are the most influential and commonly measured in each European city.

# Procedures
### Measurements
This script contains information downloaded through an API. This implies that both the information and the analysis result can be updated. It can also be expanded, as for the sake of simplicity, the data extraction was limited to 300,000 records, which corresponds to over 2 years of air quality records in the autonomous community of Catalonia.

The dataset generated from this extraction has been condensed to the districts located within the city of Barcelona.
The measurement points cover all districts except Nou Barris and Sant Andreu, where there are no meters. To address this, I've used the nearest measurement point located in Santa Coloma de Gramanet as the measurement point for both of these districts. Therefore, these two districts share one measurement point.

As a result, we have a dataset that includes categorical variables, the date of measurement, and hourly measurement results. After giving it a uniform structure that can be complemented with additional information, categorical variables related to 'Green Area' and 'Tree Demographics' will be added. Both of these will be categorized and differentiated by district.

### Green Spaces
https://opendata-ajuntament.barcelona.cat/data/es/dataset/espais-verds-publics

In this script, two sources of data have been utilized: a GPKG file named 'Public Green Spaces.gpkg', and web scraping from Wikipedia to obtain the area information by district.

After performing some cleaning on both data sources and adjusting the dataframes, they were unified, using the districts as the primary key. Then, I standardized the units of measurement to make them manageable and scalable, as thinking in square kilometers within the city could be challenging. To achieve this, I converted them to hectares, which directly represent a block and become a more understandable measure for the reader.

### Trees by district
Street trees
https://opendata-ajuntament.barcelona.cat/data/es/dataset/arbrat-viari

Park trees 
https://opendata-ajuntament.barcelona.cat/data/es/dataset/arbrat-parcs

Zone trees
https://opendata-ajuntament.barcelona.cat/data/es/dataset/arbrat-zona

This dataset corresponds to the combination of three data sources representing all the surveyed trees in Barcelona. Since the structure in the CSV files is the same, I have created a function that adjusts and cleans the downloaded datasets so they can be easily used together. All you need to do is download them each quarter, which is when the information is updated

### Results
Having performed a logistic regression predictive model, different results were obtained when comparing unbalanced data and then balanced data. The selected model yielded the following outcomes:

This indicates that the predictions were nearly 93% accurate, considering the correct predictions over all possible predictions. The model's precision exceeded 90%, implying significant reliability. With these two results, the recall naturally followed suit with a high value.

- Accuracy: 0.9264348074996422
- Precision: 0.9052689052689052
- Recall: 0.9520528280218202
- F1 Score: 0.9280716484746712

# Conclusions

As a supplementary analysis, considering the data available on the web, additional manual measurement points could be included. For this analysis, in order to avoid errors and/or biases inherent to the meter, they were not taken into account. Furthermore, the frequency of manual measurement is considerably lower than that of automatic measurements.

I consider that the analysis was accurate and the result was conclusive, which would allow for the implementation of the predictive model for acceptable or unacceptable air quality in the city of Barcelona. I also believe that the high accuracy of the model was due to the homogeneity of the data, its low variability, and the volume.

### Analysis proposals
With reference to the data provided on the distribution and species of trees, I believe that an interesting analysis could also be conducted on phytodepuration (the process by which a tree absorbs air pollutants).

The questions that could arise in future studies using the same datasets would be:

Prediction of the presence/absence of a pollutant.
Modeling of the pollutant concentration.