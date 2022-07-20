"""
urllib.request = json + API MetaWeather

htps://github.com/public-apis/public-apis

"""

import requests
import json

response = requests.get('https://jsonplaceholder.typicode.com/posts/100')
if response.status_code != requests.codes.ok:
    print('coś poszło nie tak')
else:
    print(response.json())

requestBody = {
    'title': 'Nasz tytuł',
    'body' : 'Treść posta',
    'userId': 1,
    'troololo' : True
}
response2 = requests.post('https://jsonplaceholder.typicode.com/posts', json=requestBody)

if response2.status_code != requests.codes.created:
    print('POST coś poszło nie tak')
else:
    print(response2.json())

'''
#ingredinets = input(' Podaj składniki')
#queryString = input('Co chcesz wyszukać ')

response3 = requests.get(f'http://recipepuppy.com/api?i={ingredinets}&q={queryString}')
if response3.status_code != requests.codes.ok:
    print('POST coś poszło nie tak')
else:
    print(response3.json())
'''
brew_search = input('Podaj frazę wyszukiwania browaru: ')
brewery = requests.get(f'https://api.openbrewerydb.org/breweries/search?query={brew_search}')
if brewery.status_code != requests.codes.ok:
    print("cos poszło nie tak")
else:
    format = json.dumps(brewery.json(), indent=2)
    print(format)