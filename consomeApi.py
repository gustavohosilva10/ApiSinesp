import requests
import json

placa = input("Digite sua placa:")


url = 'https://sinesp.contrateumdev.com.br/api'
body = {
   "key":"chavedemostracao",
   "plate":placa
}

headers = {'content-type': 'application/json'}

r = requests.post(url, data=json.dumps(body), headers= headers)

print(r.text)

