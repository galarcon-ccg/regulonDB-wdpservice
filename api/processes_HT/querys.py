class Querys:
    AuthorsDataOfDataset = """
    query AuthorsDataOfDataset($datasetId: String!)
    {
        getAuthorsDataOfDataset(datasetId: $datasetId){
            authorsData
        }
    }
    """