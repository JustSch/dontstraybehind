import requests
import json

url = "https://maps.googleapis.com/maps/api/place/textsearch/json?input={}&inputtype=textquery&fields=formatted_address,name,opening_hours&key"

response = 'Animal%20Shelter%20In%20NYC'

url_request = url.format(response)
r = requests.get(url_request)

results_object = r.json()['results']

result_list = []

for i in range(0,5):
    result_list.append((results_object[i]['name']))
    result_list.append(' ')
    result_list.append(results_object[i]['formatted_address'])
    result_list.append(' ')
result_list = ' '.join(map(str, result_list))

print(result_list)