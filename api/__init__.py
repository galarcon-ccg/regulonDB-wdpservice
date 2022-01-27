import os
from flask import Flask, json
from flask_cors import CORS
from sgqlc.endpoint.http import HTTPEndpoint
from api.processes_HT.ht_process import HTprocess
from api.processes_HT.authorData import formatData_to_json_author_table

app = Flask(__name__)
CORS(app)
gql_url = os.environ.get("GQL_SERVICE")
gql_service = HTTPEndpoint(gql_url)


@app.route('/')
def index():
    return "welcome :)"


@app.route('/process/ht-dataset/<id_dataset>/<data_type>/<file_format>')
def process_ht(id_dataset, data_type, file_format):
    ht_process = HTprocess(id_dataset, gql_service)
    response = 'error'
    if data_type == 'authorData':
        ht_process.authorData(file_format)
        return ht_process.get_response()
    return response


'''





@app.route('/process/ht-dataset/<datasetId>/<type>/<format>')
def process_ht(datasetId, type, format):
    ht_process = HTprocess(datasetId, gql_service)
    response = 'error'
    if type == 'authorData':
        ht_process.authorData(format)
    return response


@app.route('/<datasetId>')
def author_data(datasetId):
    variables = {"datasetId": "" + datasetId}
    query = """query AuthorsDataOfDataset($datasetId: String!)
    {
        getAuthorsDataOfDataset(datasetId: $datasetId){
            authorsData
        }
    }"""
    data = gql_service(query, variables)
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

'''
