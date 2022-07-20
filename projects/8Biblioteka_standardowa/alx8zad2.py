"""
urllib.request = json + API MetaWeather

htps://github.com/public-apis/public-apis

"""
import requests
import urllib.request as url
import json

input_city = input('Podaj nazwę miasta dla pogody: ')
input_date = input('Podaj datę dla sprawdzenia pogody rrrr/mm/dd: ')
woeid = None
city_name = ''
with url.urlopen(f'https://www.metaweather.com/api/location/search/?query={input_city}') as search_city:

    json_city_data = json.load(search_city)
    #print(json_city_data)

    for i in json_city_data:
        #print(i)
        woeid = i['woeid']
        city_name = i['title']

#input_date = '2021/01/6'
# Getting weather for selected day
get_weather_with_date = requests.get(f'https://www.metaweather.com/api/location/{woeid}/{input_date}/')
if get_weather_with_date.status_code != requests.codes.ok:
    print('Coś poszlo nie tak')
else:
    final_weather1 = get_weather_with_date.json()
    final_weather = eval(json.dumps(final_weather1[0], indent=3))
#    print(final_weather)
    print(f'Pogoda dla: {city_name}\n'
        f'na dzień: {final_weather["applicable_date"]}\n'
        f'temperatura minimalna: {round(final_weather["min_temp"], 2)}st C\n'
        f'temperatura maksymalna: {round(final_weather["max_temp"], 2)} st C\n'
        f'szybkość wiatru: {round(final_weather["wind_speed"], 2)} km/h\n'
        f'kierunek wiatru: {final_weather["wind_direction_compass"]}\n'
        f'wilgotność: {final_weather["humidity"]}%\n'
        f'sprawdzalność: {final_weather["predictability"]}%\n')

# Getting weather for today
get_weather = requests.get(f'https://www.metaweather.com/api/location/{woeid}/')

if get_weather.status_code != requests.codes.ok:
    print('Coś poszlo nie tak')
else:
    weather_table = get_weather.json()
    final_weather1 = json.dumps(weather_table["consolidated_weather"][0], indent=3)
    final_weather = eval(final_weather1)
#    print(final_weather1)
    print(f'Pogoda dla: {city_name}\n'
        f'na dzień: {final_weather["applicable_date"]}\n'
        f'temperatura minimalna: {round(final_weather["min_temp"], 2)}st C\n'
        f'temperatura maksymalna: {round(final_weather["max_temp"], 2)} st C\n'
        f'szybkość wiatru: {round(final_weather["wind_speed"], 2)} km/h\n'
        f'kierunek wiatru: {final_weather["wind_direction_compass"]}\n'
        f'wilgotność: {final_weather["humidity"]}%\n'
        f'sprawdzalność: {final_weather["predictability"]}%\n')

