# California Housing Project

This lab shows the importance of location in the pricing of housing in California, showing that location along can account for 75% of the variation in housing prices. 
- The **first model** considers the house's simple geographic region and accounts for **20%** of the variation in housing price.
- The **second model** considers the house's distance to large cities and accounts for **25%** of variation.
- The **final model** considers the price of nearby homes and accounts for **75%** of the variation.

This data features of 20,000 blocks of housing in California.  Using this data, we will determine whether location alone can account for variations in housing prices.

|    |   MedInc |   HouseAge |   AveRooms |   AveBedrms |   Population |   AveOccup |   Latitude |   Longitude |   housing_price |
|---:|---------:|-----------:|-----------:|------------:|-------------:|-----------:|-----------:|------------:|----------------:|
|  0 |   8.3252 |         41 |    6.98413 |     1.02381 |          322 |    2.55556 |      37.88 |     -122.23 |           4.526 |
|  1 |   8.3014 |         21 |    6.23814 |     0.97188 |         2401 |    2.10984 |      37.86 |     -122.22 |           3.585 |
|  2 |   7.2574 |         52 |    8.28814 |     1.07345 |          496 |    2.80226 |      37.85 |     -122.24 |           3.521 |
|  3 |   5.6431 |         52 |    5.81735 |     1.07306 |          558 |    2.54795 |      37.85 |     -122.25 |           3.413 |
|  4 |   3.8462 |         52 |    6.28185 |     1.08108 |          565 |    2.18147 |      37.85 |     -122.25 |           3.422 |

## EDA
 After loading the data, we see a **strong correlation** of both **Medium Income** (MedInc) and **location** with housing price.  Other features do not have a strong correlation.  The highest priced housing can be found in the San Francisco, L.A., and San Diego regions, while the lower priced housing is in the Central Valley.


|            |   Price Correlation |
|:-----------|--------------------:| 
| MedInc     |           0.688075  |
| AveRooms   |           0.151948  |
| HouseAge   |           0.105623  |
| AveOccup   |          -0.0237374 |
| Population |          -0.0246497 |
| AveBedrms  |          -0.0467005 |

<img src="img/map1.png"> 

## First Simple Model: Region of Housing
As a simple initial model, we simply model the housing price as the average housing price for each region.  This simple model can account for 20% of the variation in housing price.

| Region         |        Average Housing Price |
|:---------------|-----------------------------:|
| SF Region      |                     $283,809 |
| LA Region      |                     $239,050 |
| SD Region      |                     $197,564 |
| Central Valley |                     $107,598 |
| Other          |                     $162,839 |

This model has a high error due to large variations in housing price within a region.  Below, we see the large variationin housing price in the Los Angeles Area: 
<img src="img/map_model_one_error.png">

## Second Simple Model: Inverse Distance to City
The second model models price on the distance to several desirable neighborhoods in California.  The model can account for 31% of the variation in housing price.  In the map of Los Angeles below, the errors are much smaller throughout the city.

<img src="img/map_model_two_error.png">

## Third Model: Nearest Neighbors
Considering the average housing prices of the 8 nearest housing units models 79% of the pricing variation.  For example, in this map of Los Angeles, the error prediction is much smaller throughout the city.

<img src="img/map_model_three_error.png">

## Conclusion
It turns out that the best predictor of a housing price is the average price of the 5 nearest blocks.  Since housing is often built in developments of similar housing, it makes sense that the neighborhood would have the strongest effect on housing price.