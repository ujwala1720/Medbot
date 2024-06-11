import requests

url = "https://v1.nocodeapi.com/ujwalawwwwww/fit/fSvvTXbJJULJubFk/aggregatesDatasets?dataTypeName=activity_summary"
params = {}
r = requests.get(url = url, params = params)
result = r.json()
print(result)