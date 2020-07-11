import csv 
import json 
import pandas as pd

csvPath ='C:/Users/spanda/Desktop/Trinity/Urban Computing/project folder/all_form.csv'
jsonPath ='C:/Users/spanda/Desktop/Trinity/Urban Computing/project folder/data.json'

data = {}

csv_file = pd.DataFrame(pd.read_csv(csvPath, sep = ",", header = 0, index_col = False))
csv_file.to_json(jsonPath, orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)


with open(csvPath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for csvrow in csvReader:
        colid = csvrow["t"]
        data[colid] = csvrow
        
with open(jsonPath,'w') as jsonFile:
    jsonFile.write(json.dumps(data,indent=4))