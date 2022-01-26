from re import A
from flask import Flask, json
from flask_cors import CORS
from sgqlc.endpoint.http import HTTPEndpoint

from api.processes_HT.authorData import formatData_to_json_author_table

app = Flask(__name__)
CORS(app)
url = 'http://132.248.220.219/graphql'
endpoint = HTTPEndpoint(url)

@app.route('/process/ht-dataset/jsontable/site/<datasetId>')
def jsontable_site(datasetId):
    return datasetId

@app.route('/<datasetId>')
def author_data(datasetId):
    variables = {"datasetId": ""+datasetId}
    query = """query AuthorData($datasetId: String!)
    {
        getAuthorsDataOfDataset(datasetId: $datasetId){
            authorsData
        }
    }"""
    data = endpoint(query, variables)
    authorsData = {}
    try:
        authorsData = data['data']['getAuthorsDataOfDataset'][0]['authorsData']
    except:
        return "error"
    json_author_table = formatData_to_json_author_table(authorsData)
    response = app.response_class(
        response=json.dumps(json_author_table),
        status=200,
        mimetype='application/json'
    )
    return response
