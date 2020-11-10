#upd 1: f-strings
#rapidapi.com/community/api/open-weather-map
import requests

url = "https://rapidapi.p.rapidapi.com/weather"

querystring = {
    "q":"Saint Petersburg,ru",
    "lat":"0",
    "lon":"0",
    "lang":"ru",
    "units":"metric"
    }

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "get your's on rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
print("Status code:", response.status_code)

response_dict = response.json()
print(f'''
Город: {response_dict['name']}
На улице {response_dict['weather'][0].get('description')}
Температура: {str(int(response_dict['main']['temp']))}°C
Чувствуется как: {str(int(response_dict['main']['feels_like']))}°C''')
