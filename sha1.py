import hashlib 
import json

h = hashlib.sha1()

with open('data.json', 'r') as myfile:
  data = myfile.read()

# h.update(data.encode('utf-8'))

teste = json.loads(data)

h.update(teste['decifrado'].encode('utf-8'))


print(h.hexdigest())