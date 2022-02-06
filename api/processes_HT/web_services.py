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
        data = self.gql_service(self.query, self.variables)
        if self.data_type == "sites":
            return data['data']['getAllTFBindingOfDataset']
        elif self.data_type == "peaks":
            return data['data']['getAllPeaksOfDataset']
        else:
            return {"error": "data type"}
