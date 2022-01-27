from typing_extensions import Self
from querys import Querys



class HTprocess:
    
    querys = Querys()
    
    def __init__(self, datasetId, gql_service):
        self.datasetId = datasetId
        self.variables = {"datasetId": ""+datasetId}
    
    def authorData(self, format):
        query = self.querys.AuthorsDataOfDataset
        if format == 'cvs' or format == 'CVS':
            return ',,'
        elif format == 'jsontable' or format == 'JSONtable' or format == 'jsonTable':
            #JSONtable process
            return {}
        else:
            return 'invalid format: '+format
