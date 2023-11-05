import requests
import json

params = {
    # 'flon':100.54898053407669,
    # 'flat':13.743080902938331,
    # 'tlon':100.55885508656502,
    # 'tlat':13.724314618267575,
    # 'mode':'d',
    # 'type':25,
    # 'locale':"th",
    'keyword': 'chula',
    'key':'fe75c23350d22e5b0ff781a28a09aaf5'
}

response = requests.get(
    url = 'https://search.longdo.com/mapsearch/json/search?',
    params=params
)

d = json.loads(response.text)
print(d)
 