from covidData import CovidInfo
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

@app.route('/covid', methods=['GET'])
def respond():
    state = request.args.get('state', None)
    export_option = request.args.get('export',None)
    data = CovidInfo(state)

    if not export_option:
        response ={}
        response['State']=data.state
        response['Total Cases']=str(data.total_cases)
        response['Recovered']=str(data.recovered)
        response['Deaths']=str(data.deaths)
        response['Active Cases']=str(data.active_cases)
        return jsonify(response)
    else:
        csv = data.cases.to_csv(index=False)
        response = make_response(csv)
        cd = 'attachment; filename=covid-cases-india.csv'
        response.headers['Content-Disposition'] = cd
        response.mimetype='text/csv'
        return response

if __name__ == '__main__':
    app.run(debug=True)