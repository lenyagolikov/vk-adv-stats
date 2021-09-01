import requests
from decouple import config

token = config('token')
version = '5.131'
account_id = config('account_id')
url = 'https://api.vk.com/method/ads.getStatistics'
adv_ids = map(int, config('adv_ids').split(', '))


def create_request(adv):
    response = requests.get(url, params={
        'access_token': token,
        'v': version,
        'account_id': account_id,
        'ids_type': 'ad',
        'ids': adv,
        'period': 'day',
        'date_from': '2021-09-02',
        'date_to': '2021-09-02',
    })

    return response
