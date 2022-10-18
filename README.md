# COVID Live API
Provides the latest data from primary data sources on COVID-19. The API uses European CDC for country level data and uses data.gov.in for Indian State level data. Data from European CDC only includes total cases and deaths, whereas Indian state level data contains active cases and recovered cases as well.

## <ins>Country Level Data</ins>
#### 1. Basic Usage:
````
covid-live-api.herokuapp.com/covid
````
#### 2. Possible arguments:
- Raw Data for that Country
````
covid-live-api.herokuapp.com/covid?export=True
````
- Country Filtering
````
covid-live-api.herokuapp.com/covid?country=Algeria
covid-live-api.herokuapp.com/covid?country=New Zealand
````
- List of Valid Country Names
````
covid-live-api.herokuapp.com/covid?listCountries=True
````

## <ins>State Level Data for India</ins>
#### 1. Basic Usage:
````
covid-live-api.herokuapp.com/covid-india
````
#### 2. Possible arguments:
- Raw Data for that Country
````
covid-live-api.herokuapp.com/covid-india?export=True
````
- Country Filtering
````
covid-live-api.herokuapp.com/covid-india?state=Maharashtra
covid-live-api.herokuapp.com/covid-india?state=Uttar Pradesh
````
