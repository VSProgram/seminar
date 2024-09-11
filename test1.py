import requests


res = requests.get(url='https://yandex.ru')


def get_index(handler: str):
    baseurl = 'https://yandex.ru'
    url = baseurl+'/?'+handler
    return requests.get(url= url)

res = get_index(handler='хубабуба')

stop = 0 #Для отладки

# установить mypy