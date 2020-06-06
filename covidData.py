import pandas as pd

class CovidInfo():

    def __init__(self,country='World'):
        self.url_cases = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
        cases_raw = pd.read_csv(self.url_cases)
        self.cases = self.casesCleaner(cases_raw)
        self.countryFilter(country)

    def casesCleaner(self,df):
        df_new = df[['location','date','total_cases','new_cases','total_deaths','new_deaths',
                        'total_cases_per_million','new_cases_per_million','total_deaths_per_million',
                        'new_deaths_per_million','total_tests','new_tests','total_tests_per_thousand',
                        'new_tests_per_thousand']]
        return df_new

    def metricSetter(self,cases):
        self.last_updated = max(cases.loc[cases['location']==self.country,'date'])
        self.total_cases = int(cases.loc[(cases['location']==self.country)&
                                (cases['date']==self.last_updated),'total_cases'])
        self.deaths = int(cases.loc[(cases['location']==self.country)&
                                (cases['date']==self.last_updated),'total_deaths'])

    def countryFilter(self,country='World'):
        self.country = 'World'
        if self.validCountry(country):
            self.country = country
            self.cases = self.cases.loc[self.cases['location']==country]
        self.metricSetter(self.cases)

    def validCountry(self,country):
        self.validCountries = list(self.cases['location'].unique())
        return country in self.validCountries

    def __repr__(self):
        return str(self.cases)
    
    def __str__(self):
        result_dict = {'Country':self.country,'Total Cases':self.total_cases,'Deaths':self.deaths}
        return str(result_dict)    


class CovidInfo_India():

    def __init__(self,state=None):
        self.url_cases = 'https://api.data.gov.in/resource/cd08e47b-bd70-4efb-8ebc-589344934531?format=csv&limit=all&api-key=579b464db66ec23bdd000001cdc3b564546246a772a26393094f5645'
        cases_raw = pd.read_csv(self.url_cases)
        self.last_updated = cases_raw['DateTime'][0]
        self.cases = self.casesCleaner(cases_raw)
        self.stateFilter(state)
    
    def casesCleaner(self,df):
        df.drop(['S. No.','Date','DateTime'],axis=1,inplace=True)
        df.columns = ['State','Total Cases','Recovered','Death']
        return df

    def metricSetter(self,cases):
        self.total_cases = cases['Total Cases'].sum()
        self.recovered = cases['Recovered'].sum()
        self.deaths = cases['Death'].sum()
        self.active_cases = self.total_cases - self.recovered - self.deaths

    def stateFilter(self,state=None):
        self.state=None
        if self.validState(state):
            self.state=state
            self.cases = self.cases.loc[self.cases['State']==state]
        self.metricSetter(self.cases)
    
    def validState(self,state):
        validStates = list(self.cases['State'])
        return state in validStates

    def __repr__(self):
        return str(self.cases)

    def __str__(self):
        result_dict = {'State':self.state,'Total Cases':self.total_cases,
                        'Recovered':self.recovered,'Deaths':self.deaths,
                        'Active Cases':self.active_cases}
        return str(result_dict)





