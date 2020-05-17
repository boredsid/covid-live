import pandas as pd

class CovidInfo():

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
        validStates = ['Andaman and Nicobar Islands','Andhra Pradesh','Arunachal Pradesh',
                        'Assam','Bihar','Chandigarh','Chhattisgarh','Dadar Nagar Haveli','Delhi',
                        'Goa','Gujarat','Haryana','Himachal Pradesh','Jammu and Kashmir','Jharkhand',
                        'Karnataka','Kerala','Ladakh','Madhya Pradesh','Maharashtra','Manipur',
                        'Meghalaya','Mizoram','Odisha','Puducherry','Punjab','Rajasthan','Tamil Nadu',
                        'Telengana','Tripura','Uttarakhand','Uttar Pradesh','West Bengal']

        if state in validStates:
            return True
        else:
            return False

    def __repr__(self):
        return str(self.cases)

    def __str__(self):
        result_dict = {'State':self.state,'Total Cases':self.total_cases,
                        'Recovered':self.recovered,'Deaths':self.deaths,
                        'Active Cases':self.active_cases}
        return str(result_dict)





