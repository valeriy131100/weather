import requests

url_template = 'https://wttr.in/{}'

params = {
    "m": "",  # метрическая система
    "n": "",  # узкая версия
    "T": "",  # черно-белый вариант
    "q": "",  # тихая версия
    "lang": "ru"
}

cities = ('Лондон', 'Шереметьево', 'Череповец')

for city in cities:
    url = url_template.format(city)
    response = requests.get(url, params=params)

    response.raise_for_status()
    print(response.text)
