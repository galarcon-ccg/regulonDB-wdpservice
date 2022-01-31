import os
import json
from flask import Response, jsonify
from .querys import Querys
from .authorData import formatData_to_json_author_table
from .sitesData import process_sites_to_gff3
from .peaksData import process_peaks_to_gff3


class HTprocess:
    querys = Querys()

    def __init__(self, id_dataset, gql_service):
        self.id_dataset = id_dataset
        self.gql_service = gql_service
        self.ht_response = ""

    def peaks_data(self, file_format):
        file_format = file_format.lower()
        valid_formats = ["gff3", "jsontable"]
        if file_format not in valid_formats:
            self.ht_response = 'invalid format: ' + file_format
            return ""
        query = self.querys.PeaksDataOfDataset
        variables = {"datasetId": "" + self.id_dataset}
        data = self.check_cache(file_format)
        if not data:
            try:
                data = self.gql_service(query, variables)
                data = data['data']['getAllPeaksOfDataset']
                if file_format == 'gff3':
                    data = process_peaks_to_gff3(data)
                    self.ht_response = Response(
                        data,
                        mimetype="text/gff3",
                        headers={"Content-disposition": "attachment; gff3_" + self.id_dataset + ".gff3"}
                    )
                else:
                    data = str(data)
                with open("./cache/" + self.id_dataset + "_" + file_format + ".cache", "w") as file:
                    file.write(data)
            except Exception as e:
                print(e)
        else:
            if file_format == 'gff3':
                self.ht_response = Response(
                    data,
                    mimetype="text/gff3",
                    headers={"Content-disposition": "attachment; gff3_" + self.id_dataset + ".gff3"}
                )
            else:
                self.ht_response = 'invalid format: ' + file_format


    def sites_data(self, file_format):
        file_format = file_format.lower()
        valid_formats = ["gff3", "jsontable"]
        if file_format not in valid_formats:
            self.ht_response = 'invalid format: ' + file_format
            return ""
        query = self.querys.SitesDataOfDataset
        variables = {"datasetId": "" + self.id_dataset}
        data = self.check_cache(file_format)
        if not data:
            try:
                data = self.gql_service(query, variables)
                data = data['data']['getAllTFBindingOfDataset']
                if file_format == 'gff3':
                    data = process_sites_to_gff3(data)
                    self.ht_response = Response(
                        data,
                        mimetype="text/gff3",
                        headers={"Content-disposition": "attachment; gff3_" + self.id_dataset + ".gff3"}
                    )
                else:
                    data = str(data)
                with open("./cache/" + self.id_dataset + "_" + file_format + ".cache", "w") as file:
                    file.write(data)
            except Exception as e:
                print(e)
                data = "Error: " + e
        else:
            if file_format == 'gff3':
                self.ht_response = Response(
                    data,
                    mimetype="text/gff3",
                    headers={"Content-disposition": "attachment; gff3_" + self.id_dataset + ".gff3"}
                )
            else:
                self.ht_response = 'invalid format: ' + file_format

    def author_data(self, file_format):
        file_format = file_format.lower()
        valid_formats = ["cvs", "jsontable"]
        if file_format not in valid_formats:
            self.ht_response = 'invalid format: ' + file_format
            return ""
        query = self.querys.AuthorsDataOfDataset
        variables = {"datasetId": "" + self.id_dataset}
        data = self.check_cache(file_format)
        if not data:
            data = self.gql_service(query, variables)
            try:
                print("consulta")
                data = data['data']['getAuthorsDataOfDataset'][0]['authorsData']
                if file_format == 'jsontable':
                    data = str(formatData_to_json_author_table(data))
                with open("./cache/" + self.id_dataset + "_" + file_format + ".cache", "w") as file:
                    file.write(data)
            except Exception as e:
                print(e)
                data = "error: " + str(e)
        print("cache")
        if file_format == 'cvs':
            self.ht_response = Response(
                data,
                mimetype="text/csv",
                headers={"Content-disposition": "attachment; authorData_" + self.id_dataset + ".csv"}
            )
        elif file_format == 'jsontable':
            data = json.loads(data.replace("'", "\""))
            self.ht_response = jsonify(data)
        else:
            self.ht_response = 'invalid format: ' + file_format

    def check_cache(self, type_file):
        data = False
        if os.path.exists("./cache/" + self.id_dataset + "_" + type_file + ".cache"):
            try:
                return open("./cache/" + self.id_dataset + "_" + type_file + ".cache", "r").read()
            except Exception as e:
                print(e)
        return data

    def get_response(self):
        return self.ht_response
