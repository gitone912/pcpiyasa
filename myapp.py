import requests
import json
URL='http://127.0.0.1:8000/get_processor_data/'
with open ('processor.json', encoding='utf-8') as file:
    # Reading from file
    data = json.load(file)
json_data = json.dumps(data, ensure_ascii=False)
print(json_data.encode('utf-8')) # encode the string as utf-8 before sending it

response = requests.post(URL, data=json_data.encode('utf-8'))
print(response.status_code)
