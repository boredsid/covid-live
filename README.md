# COVID Live API
Provides the latest data from primary data sources on COVID-19 and uses European CDC for country level data and uses data.gov.in for Indian State level data

## <ins>Country Level Data</ins>
#### 1. Basic Usage:
````
covid-live-api.herokuapp.com\covid
````
#### 2. Possible arguments:
- Raw Data for that Country
````
covid-live-api.herokuapp.com\covid?export=True
````
- Country Filtering
````
covid-live-api.herokuapp.com\covid?country=Algeria
````
- List of Valid Country Names
````
covid-live-api.herokuapp.com\covid?listCountries=True
````

## <ins>State Level Data for India</ins>
#### 1. Basic Usage:
````
covid-live-api.herokuapp.com\covid-india
````
#### 2. Possible arguments:
- Raw Data for that Country
````
covid-live-api.herokuapp.com\covid-india?export=True
````
- Country Filtering
````
covid-live-api.herokuapp.com\covid-india?state=Maharashtra
````

## More Features to be added soon!

