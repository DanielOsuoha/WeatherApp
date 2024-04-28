import requests

API_KEY = '8f3e86f89fdbb70120c80bc243d65e8b'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    url = f'{BASE_URL}?q={city}&appid={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(requests.status_code)
        return None
    

if __name__ == '__main__':
    city = input('Enter the city name: ')
    print(get_weather(city))
    