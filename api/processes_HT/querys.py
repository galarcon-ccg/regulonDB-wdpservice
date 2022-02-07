class Querys:

    AuthorsDataOfDataset = """
    query AuthorsDataOfDataset($datasetId: String!)
    {
        getAuthorsDataOfDataset(datasetId: $datasetId){
            authorsData
        }
    }
    """

    PeaksDataOfDataset = """
    query PeaksDataOfDataset($datasetId: String!) {
        getAllPeaksOfDataset(datasetId: $datasetId) {
            _id
            name
            closestGenes {
              _id
              name
              distanceTo
              productName
            }
            chromosome
            peakLeftPosition
            peakRightPosition
            score
            siteIds
            datasetIds
            temporalId
        }
    }
    """

    SitesDataOfDataset = """
    query SitesDataOfDataset($datasetId: String!) {
        getAllTFBindingOfDataset(datasetId: $datasetId) {
            _id
            chromosome
            chrLeftPosition
            chrRightPosition
            closestGenes {
                _id
                name
                distanceTo
                transcriptionUnits {
                    _id
                    name
                    distanceTo
                }
            }
            foundClassicRIs {
                tfbsLeftPosition
                tfbsRightPosition
                relativeGeneDistance
                relativeTSSDistance
                strand
                sequence
            }
            foundDatasetRIs {
                tfbsLeftPosition
                tfbsRightPosition
                relativeGeneDistance
                relativeTSSDistance
                strand
                sequence
            }
            peakId
            score
            strand
            sequence
            datasetIds
            temporalId
            nameCollection
        }
    }
    """

    TuDataOfDataset = """
    query TuDataOfDataset($datasetId: String!)
    {
        getAllTransUnitsOfDataset(datasetId: $datasetId){
            _id
            chromosome
            leftEndPosition
            rightEndPosition
            name
            strand
            length
            termType
            genes {
              _id
              name
              bnumber
            }
            phantom
            pseudo
            datasetIds
            temporalId
        }
    }
    """

    switch_querys = {
        "author": AuthorsDataOfDataset,
        "peaks": PeaksDataOfDataset,
        "sites": SitesDataOfDataset,
        "tu": TuDataOfDataset
    }
