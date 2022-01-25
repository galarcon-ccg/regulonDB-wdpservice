from ast import Try
from flask import Flask
from flask_cors import CORS
from sgqlc.endpoint.http import HTTPEndpoint
from io import StringIO
import csv
import re

app = Flask(__name__)
CORS(app)
url = 'http://132.248.220.219/graphql'


@app.route('/<datasetId>')
def hello(datasetId):
    json_author_table = {
        'comments': [],
        'columns': [],
        'data': []
    }
    variables = {"datasetId": ""+datasetId}
    query = """query AuthorData($datasetId: String!)
    {
        getAuthorsDataOfDataset(datasetId: $datasetId){
            authorsData
        }
    }"""
    endpoint = HTTPEndpoint(url)
    data = endpoint(query,variables)
    file = StringIO(data['data']['getAuthorsDataOfDataset'][0]['authorsData'])
    reader = csv.reader(file, delimiter=',')
    # search comments
    lines_comments = []
    index = 0
    for row in reader:
        if re.search("^#",row[0]):
            json_author_table['comments'].append("".join(row))
        +(+index)
    print(json_author_table)
    return 'My First API !!'

