import requests
from YaToken import YaToken


def create_dir(dir_name: str, token=YaToken):
    """Метод создаёт папку на яндекс диске"""
    headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {token}'}
    if 'error' not in requests.get('https://cloud-api.yandex.net/v1/disk/resources',
                                   params={'path': dir_name}, headers=headers).json():
        return 'This folder already exists.'
    requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                 params={'path': dir_name}, headers=headers)
    return f'"{dir_name}" created'
