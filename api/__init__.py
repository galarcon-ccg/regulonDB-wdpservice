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
        ht_process.author_data(file_format)
        return ht_process.get_response()
    elif data_type == 'sitesData':
        ht_process.sites_data(file_format)
        return ht_process.get_response()
    elif data_type == 'peaksData':
        ht_process.peaks_data(file_format)
        return ht_process.get_response()
    return response

