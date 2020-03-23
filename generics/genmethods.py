import json

def read_json_val(filename,name,key):
    with open("./"+filename+".json") as f:
        data=json.load(f)
    return(data[name][key])