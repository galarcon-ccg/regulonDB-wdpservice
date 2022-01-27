import os
from flask import Response, jsonify
from .querys import Querys
from .authorData import formatData_to_json_author_table


class HTprocess:
    querys = Querys()

    def __init__(self, id_dataset, gql_service):
        self.id_dataset = id_dataset
        self.gql_service = gql_service
        self.ht_response = ""

    def authorData(self, file_format):
        query = self.querys.AuthorsDataOfDataset
        variables = {"datasetId": "" + self.id_dataset}
        if os.path.exists("./cache/"+self.id_dataset+".cache"):
            try:
                cache = open("./cache/"+self.id_dataset+".cache", "r").read()
                data = cache
            except Exception as e:
                print(e)
                data = e
        else:
            data = self.gql_service(query, variables)
            try:
                data = data['data']['getAuthorsDataOfDataset'][0]['authorsData']
            except Exception as e:
                print(e)
                data = "error: "+e
            with open("./cache/"+self.id_dataset+".cache", "w") as file:
                file.write(data)
        if file_format == 'cvs' or file_format == 'CVS':
            self.ht_response = Response(
                data,
                mimetype="text/csv",
                headers={"Content-disposition": "attachment; authorData_"+self.id_dataset+"=.csv"}
            )
        elif file_format == 'jsontable' or file_format == 'JSONtable' or file_format == 'jsonTable':
            data = formatData_to_json_author_table(data)
            self.ht_response = jsonify(data)
        else:
            self.ht_response = 'invalid format: ' + file_format

    def get_response(self):
        return self.ht_response
