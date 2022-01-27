from flask import send_file
from .querys import Querys


class HTprocess:
    querys = Querys()

    def __init__(self, id_dataset, gql_service):
        self.id_dataset = id_dataset
        self.gql_service = gql_service
        self.ht_response = ""

    def authorData(self, file_format):
        query = self.querys.AuthorsDataOfDataset
        variables = {"datasetId": "" + self.id_dataset}
        data = self.gql_service(query, variables)
        try:
            data = data['data']['getAuthorsDataOfDataset'][0]['authorsData']
        except Exception as e:
            print(e)
            data = {}
        if file_format == 'cvs' or file_format == 'CVS':
            self.ht_response = data
        elif file_format == 'jsontable' or file_format == 'JSONtable' or file_format == 'jsonTable':
            # JSONtable process
            self.ht_response = {}
        else:
            self.ht_response = 'invalid format: ' + file_format

    def get_response(self):
        return self.ht_response
