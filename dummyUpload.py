import json
import requests
import random
import datetime

url = "https://autometa-116e.restdb.io/rest/data"

createDT = str(datetime.datetime.now)

randFuel = str(random.randint(0, 100))

randEco = str(random.randrange(1, 20))

jsonData = {"fuelLevel":randFuel, "economy":randEco}

payload = json.dumps(jsonData)
headers = {
    'content-type': "application/json",
    'x-apikey': "0f02171996cf0b68684f8020541d7acc57f70",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
