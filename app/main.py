#!/usr/bin/python3
from datetime import datetime

import utils
import vk_requests


def main():
    for adv_id in vk_requests.adv_ids:
        stats = vk_requests.get_stats(adv_id)
        reach = vk_requests.get_reach(adv_id)
        current_time = datetime.now().strftime("%H:%M")
        current_date = datetime.now().strftime("%d.%m.%y")

        utils.save_data(adv_id, *stats, reach, current_date, current_time)
        utils.save_data_delta()


if __name__ == '__main__':
    main()
