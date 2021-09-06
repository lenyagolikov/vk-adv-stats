import requests
from decouple import config

adv_ids = map(int, config('adv_ids').split(', '))


def get_stats(adv):
    url = 'https://api.vk.com/method/ads.getStatistics'

    response = requests.get(url, params={
        'access_token': config('token'),
        'v': config('version'),
        'account_id': config('account_id'),
        'ids_type': 'ad',
        'ids': adv,
        'period': 'day',
        'date_from': '2021-09-03',
        'date_to': '2021-09-03',
    })

    stats = response.json()['response'][0]['stats']

    if stats:
        shows = stats[0].get('impressions', 0)
        clicks = stats[0].get('clicks', 0)
        lead_form_sends = stats[0].get('lead_form_sends', 0)
        reach = stats[0].get('reach', 0)
        join_rate = stats[0].get('join_rate', 0)
        spent = stats[0].get('spent', 0)
        ctr = stats[0].get('ctr', 0)
        ecpc = stats[0].get('effective_cost_per_click', 0)
        ecpm = stats[0].get('effective_cost_per_mille', 0)

        return shows, clicks, lead_form_sends, reach, join_rate, spent, ctr, ecpc, ecpm

    return 0, 0, 0, 0, 0, 0, 0, 0, 0


def get_reach(adv):
    url = 'https://api.vk.com/method/ads.getPostsReach'

    response = requests.get(url, params={
        'access_token': config('token'),
        'v': config('version'),
        'account_id': config('account_id'),
        'ids_type': 'ad',
        'ids': adv,
    })

    stats = response.json()['response'][0]

    reach_total = stats.get('reach_total', 0)
    links = stats.get('links', 0)
    to_group = stats.get('to_group', 0)
    # join_group = stats.get('join_group', 0)

    return reach_total, links, to_group


def target_stats(adv):
    url = 'https://api.vk.com/method/ads.getTargetingStats'
