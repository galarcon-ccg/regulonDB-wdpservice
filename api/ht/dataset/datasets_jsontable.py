from .introspection import Dataset


def dataset_jsontable(datasets):
    # Make Columns!
    columns = []
    for key in Dataset:
        column = False
        if Dataset[key] is str:
            column = {
                'Header': key,
                'accessor': "_"+key
            }
        elif Dataset[key] is int:
            column = {
                'Header': key,
                'accessor': "_"+key
            }
        elif type(Dataset[key]) is list:
            column = proses_list(key, Dataset[key])
        elif type(Dataset[key]) is dict:
            column = proses_dict(key, Dataset[key])
        if column:
            columns.append(column)
        # print(column)
    # print(columns)
    data = []
    for dataset in datasets:
        row = {}
        for key in dataset:
            if type(dataset[key]) is str:
                row['_'+key] = dataset[key]
        if len(row) > 0:
            data.append(row)
    print(data)
    return "hola"


def proses_list(key, data):
    columns = []
    for subcolumn in data[0]:
        # print(data[0][subcolumn])
        if data[0][subcolumn] is str:
            columns.append({
                'Header': subcolumn,
                'accessor': "_"+key+"_"+subcolumn
            })
        elif data[0][subcolumn] is int:
            columns.append({
                'Header': subcolumn,
                'accessor': "_" + key + "_" + subcolumn
            })
        elif data[0][subcolumn] is list:
            columns.append({
                'Header': subcolumn,
                'columns': proses_list(subcolumn, data[0][subcolumn])
            })
        elif data[0][subcolumn] is dict:
            columns.append({
                'Header': subcolumn,
                'columns': proses_dict(subcolumn, data[0][subcolumn])
            })
    return {
        'Header': key,
        'columns': columns
    }


def proses_dict(key, data):
    columns = []
    for subcolumn in data:
        # print(data[column])
        if data[subcolumn] is str:
            columns.append({
                "Header": subcolumn,
                'accessor': "_"+key+"_"+subcolumn
            })
        elif data[subcolumn] is int:
            columns.append({
                'Header': subcolumn,
                'accessor': "_" + key + "_" + subcolumn
            })
        elif data[subcolumn] is list:
            columns.append({
                'Header': subcolumn,
                'columns': proses_list(subcolumn, data[subcolumn])
            })
        elif data[subcolumn] is dict:
            columns.append({
                'Header': subcolumn,
                'columns': proses_dict(subcolumn, data[subcolumn])
            })

    return {
        'Header': key,
        'columns': columns
    }
