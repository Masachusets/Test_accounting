import requests
import pytest
from sel import enter_to_yandex
from YaToken import YaLogin, YaPassword


FIXTURE = [(YaLogin, YaPassword, 'Done'),
           ('pip@ert.ru', '234', 'Error')]

@pytest.mark.parametrize('login, password, result', FIXTURE)
def test_enter_to_yandex(login, password, result):
    assert enter_to_yandex(login, password) == result
