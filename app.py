from covidData import CovidInfo,CovidInfo_India
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

@app.route('/covid',methods=['GET'])
def respond():
    country = request.args.get('country','World')
    export_option = request.args.get('export',None)
    listCountries = request.args.get('listCountries',None)
    data = CovidInfo(country)

    if export_option:
        csv = data.cases.to_csv(index=False)
        response = make_response(csv)
        cd = 'attachment; filename=covid-cases.csv'
        response.headers['Content-Disposition'] = cd
        response.mimetype='text/csv'
        return response

    response = {}

    if listCountries:
        response['validCountries'] = data.validCountries
    response['Country'] = data.country
    response['Total Cases'] = str(data.total_cases)
    response['Deaths'] = str(data.deaths)

    return jsonify(response)

@app.route('/covid-india', methods=['GET'])
def respond_india():
    state = request.args.get('state', None)
    export_option = request.args.get('export',None)
    data = CovidInfo_India(state)

    if export_option:
        csv = data.cases.to_csv(index=False)
        response = make_response(csv)
        cd = 'attachment; filename=covid-cases-india.csv'
        response.headers['Content-Disposition'] = cd
        response.mimetype='text/csv'
        return response

    response ={}
    response['State']=data.state
    response['Total Cases']=str(data.total_cases)
    response['Recovered']=str(data.recovered)
    response['Deaths']=str(data.deaths)
    response['Active Cases']=str(data.active_cases)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)