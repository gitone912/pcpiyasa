import requests
import json
URL='http://127.0.0.1:8000/get_processor_data/'
with open ('processor.json') as file:
    # Reading from file
    data = json.loads(file.read())
json_data = json.dumps(data)
print(json_data)
r = requests.post(url= URL ,data= json_data)
data = r.json()
print(data)