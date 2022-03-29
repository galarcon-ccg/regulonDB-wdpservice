from .querys import Querys


class WServices:
    querys = Querys()

    def __init__(self, gql_service, dataset_id, data_type):
        self.gql_service = gql_service
        self.dataset_id = dataset_id
        self.data_type = data_type
        self.query = self.querys.switch_querys[data_type]
        self.variables = {"datasetId": "" + dataset_id}

    def get_data(self):
        if self.data_type == "ge":
            data = self.gql_service(self.query, {"advancedSearch": ""+self.dataset_id+"[datasetIds]"})
            return data['data']['getGeneExpressionFromSearch']

        data = self.gql_service(self.query, self.variables)
        if self.data_type == "sites":
            return data['data']['getAllTFBindingOfDataset']
        elif self.data_type == "peaks":
            return data['data']['getAllPeaksOfDataset']
        elif self.data_type == "tus":
            return data['data']['getAllTransUnitsOfDataset']
        elif self.data_type == "tts":
            return data['data']['getAllTTSOfDataset']
        elif self.data_type == "tss":
            return data['data']['getAllTSSOfDataset']
        else:
            return {"error": "data type"}
