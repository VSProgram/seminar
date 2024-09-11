import requests


res = requests.get(url='https://yandex.ru')


def get_index(handler: str)-> Response:
    baseurl = 'https://yandex.ru'
    url = baseurl+'/?'+handler
    return requests.get(url= url)

res = get_index(handler='xxx')

stop = 0


# ruff

# wsl ubuntu