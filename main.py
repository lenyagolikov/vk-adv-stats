#!/usr/bin/python3
import time
from datetime import datetime

import config
import utils


def main():
    for adv_id in config.adv_ids:
        shows = 0
        clicks = 0
        spent = 0

        response = config.create_request(adv_id).json()['response']
        time.sleep(0.5)

        try:
            shows = response[0]['stats'][0]['impressions']
        except:
            pass
        try:
            spent = response[0]['stats'][0]['spent']
        except:
            pass
        try:
            clicks = response[0]['stats'][0]['clicks']
        except:
            pass
        current_time = datetime.now().strftime("%H:%M")

        utils.save_data(adv_id, shows, clicks, spent, current_time)
        utils.delta()


if __name__ == '__main__':
    main()
