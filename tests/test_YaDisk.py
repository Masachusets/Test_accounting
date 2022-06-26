import requests
import pytest
from YaDisk import create_dir, YaToken


FIXTURE = [('Test_dir', '"Test_dir" created'),
           ('Test_dir', 'This folder already exists.')]


@pytest.mark.parametrize('dir_name, result', FIXTURE)
def test_create_dir(dir_name, result):
    headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {YaToken}'}
    assert create_dir(dir_name) == result
    res = requests.get('https://cloud-api.yandex.net/v1/disk/resources', params={'path': dir_name}, headers=headers)
    assert res.status_code == 200
    req = requests.get('https://cloud-api.yandex.net/v1/disk/resources', params={'path': '/'}, headers=headers)
    assert dir_name in (folder['name'] for folder in req.json()['_embedded']['items']  if folder['type'] == 'dir')
