import requests
import json

payload ={}
r = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=seu_token', json=payload)
print(r.text)

answer = r.json()

with open('data.json', 'w') as json_file:  
    json.dump(answer, json_file)
	