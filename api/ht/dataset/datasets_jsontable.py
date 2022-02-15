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
            column = proses_head_list(key, Dataset[key])
        elif type(Dataset[key]) is dict:
            column = proses_head_dict(key, Dataset[key])
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
            elif type(dataset[key]) is list:
                row = {**row, **proses_data_list(key, dataset[key])}
            elif type(dataset[key]) is dict:
                row = {**row, **proses_data_dict(key, dataset[key])}
        if len(row) > 0:
            data.append(row)
    print(data)
    return "hola"


def proses_data_list(key, data_list):
    row = {}
    for dt in data_list:
        try:
            if type(dt) is str:
                if key in row.keys():
                    row[key].append(dt)
                else:
                    row[key] = [dt]
            elif type(dt) is list:
                row = {**row, **proses_data_list(key, dt)}
            elif type(dt) is dict:
                row = {**row, **proses_data_dict(key, dt)}
        except Exception as e:
            print("error prosses data list: "+str(e)+" on dt: "+str(dt))
    return row


def proses_data_dict(key, data_dict):
    row = {}
    for sub_key in data_dict:
        try:
            dt = data_dict[sub_key]
            nw_key = '_' + key + '_' + sub_key
            if type(dt) is str:
                if nw_key in row.keys():
                    row[nw_key] = row[nw_key].append(dt)
                else:
                    row[nw_key] = [dt]
            elif type(dt) is list:
                if len(dt) > 0:
                    row = {**row, **proses_data_list(nw_key, dt)}
            elif type(dt) is dict:
                row = {**row, **proses_data_dict(nw_key, dt)}
        except Exception as e:
            print("prosses data dict"+str(e)+" on kay: "+str(sub_key))
    return row


def proses_head_list(key, data):
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
                'columns': proses_head_list(subcolumn, data[0][subcolumn])
            })
        elif data[0][subcolumn] is dict:
            columns.append({
                'Header': subcolumn,
                'columns': proses_head_dict(subcolumn, data[0][subcolumn])
            })
    return {
        'Header': key,
        'columns': columns
    }


def proses_head_dict(key, data):
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
                'columns': proses_head_list(subcolumn, data[subcolumn])
            })
        elif data[subcolumn] is dict:
            columns.append({
                'Header': subcolumn,
                'columns': proses_head_dict(subcolumn, data[subcolumn])
            })

    return {
        'Header': key,
        'columns': columns
    }
