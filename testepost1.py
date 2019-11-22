import requests
import json

answer = {'answer': ('answer', open('answer.json', 'rb'))}
response = requests.post(url=('https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=seu_token'), files=answer)
print(response.status_code)
print(response.json())