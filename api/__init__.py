from ast import Try
from flask import Flask, json
from flask_cors import CORS
from sgqlc.endpoint.http import HTTPEndpoint
from io import StringIO
import csv
import re

from sqlalchemy import column

app = Flask(__name__)
CORS(app)
url = 'http://132.248.220.219/graphql'


@app.route('/<datasetId>')
def author_data(datasetId):
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
    data = endpoint(query, variables)
    try:
        strFile = data['data']['getAuthorsDataOfDataset'][0]['authorsData']
    except:
        return "error"
    file = StringIO(""+strFile)
    reader = csv.reader(file, delimiter=',')
    author_data = []
    # search comments
    for row in reader:
        if re.search("^#", row[0]):
            json_author_table['comments'].append("".join(row))
        else:
            author_data.append(row)
    columns = []
    for index in range(len(author_data)):
        row = author_data[index]
        if index == 0:
            for cell in row:
                columns.append("_"+cell.replace(" ", "_").casefold())
                json_author_table['columns'].append({
                    'Header': ""+cell,
                    'accessor': "_"+cell.replace(" ", "_").casefold()
                })
        else:
            data = {}
            for i in range(len(row)):
                data[columns[i]] = row[i]
            json_author_table['data'].append(data)
    response = app.response_class(
        response=json.dumps(json_author_table),
        status=200,
        mimetype='application/json'
    )
    return response
