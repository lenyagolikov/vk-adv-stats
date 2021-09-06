import pandas as pd

filename = 'data.xlsx'
filedelta = 'delta.xlsx'


def save_data(adv_id, shows, clicks, lead_form_sends, reach, join_rate, spent, ctr, ecpc, ecpm, total_reach,
              links, to_group, current_date, current_time):
    try:
        df = pd.read_excel(filename)
        print(f'Opened {filename}')
    except FileNotFoundError:
        df = pd.DataFrame(columns=
                          ['ID', 'Дата', 'Время', 'Просмотры', 'Клики', 'Заявки', 'Охват',
                           'Показано снова', 'Общий охват', 'Переходы по ссылке', 'Переходы в группу',
                           'Вступлений', 'Потрачено', 'cpl', 'ctr', 'ecpc', 'ecpm',
                           ]
                          )
        print(f'{filename} does not exist. New dataframe created.')

    df = df.append({'ID': adv_id, 'Просмотры': shows, 'Клики': clicks, 'Заявки': lead_form_sends,
                    'Показано снова': 0, 'Охват': reach, 'Переходы по ссылке': links,
                    'Переходы в группу': to_group, 'Вступлений': join_rate, 'ctr': ctr,
                    'ecpc': ecpc, 'ecpm': ecpm, 'cpl': 0, 'Потрачено': spent,
                    'Общий охват': total_reach, 'Дата': current_date, 'Время': current_time,
                    }, ignore_index=True)

    df.to_excel(filename, index=False)
    print(f'Data saved in {filename}')


def save_data_delta():
    data = pd.read_excel(filename)

    for i in range(len(data) - 1, 0, -1):
        data.at[i, 'Клики'] = data.at[i, 'Клики'] - data.at[i - 1, 'Клики']
        data.at[i, 'Просмотры'] = data.at[i, 'Просмотры'] - \
                                  data.at[i - 1, 'Просмотры']
        data.at[i, 'Потрачено'] = data.at[i, 'Потрачено'] - \
                                  data.at[i - 1, 'Потрачено']
        data.at[i, 'Заявки'] = data.at[i, 'Заявки'] - data.at[i - 1, 'Заявки']
        data.at[i, 'Охват'] = data.at[i, 'Охват'] - data.at[i - 1, 'Охват']
        data.at[i, 'Общий охват'] = data.at[i, 'Общий охват'] - \
                                    data.at[i - 1, 'Общий охват']
        data.at[i, 'Показано снова'] = data.at[i, 'Охват'] - \
                                       data.at[i, 'Общий охват']
        data.at[i, 'Вступлений'] = data.at[i, 'Вступлений'] - \
                                   data.at[i - 1, 'Вступлений']
        data.at[i, 'Переходы по ссылке'] = data.at[i, 'Переходы по ссылке'] - \
                                           data.at[i - 1, 'Переходы по ссылке']
        data.at[i, 'Переходы в группу'] = data.at[i, 'Переходы в группу'] - \
                                          data.at[i - 1, 'Переходы в группу']
        data.at[i, 'ecpc'] = data.at[i, 'ecpc'] - data.at[i - 1, 'ecpc']
        data.at[i, 'ecpm'] = data.at[i, 'ecpm'] - data.at[i - 1, 'ecpm']

    data.to_excel(filedelta, index=False)


def calculate_values():
    data = pd.read_excel(filedelta)

    for i in range(len(data)):
        if data.at[i, 'Заявки'] != 0:
            data.at[i, 'cpl'] = round(
                data.at[i, 'Потрачено'] / data.at[i, 'Заявки'], 3)
        data.at[i, 'ecpm'] = round(
            (data.at[i, 'Потрачено'] / 1000) * data.at[i, 'Просмотры'], 3)
        if data.at[i, 'Клики'] != 0:
            data.at[i, 'ecpc'] = round(
                data.at[i, 'Потрачено'] / data.at[i, 'Клики'], 3)
        if data.at[i, 'Просмотры'] != 0:
            data.at[i, 'ctr'] = round(
                (data.at[i, 'Клики'] / data.at[i, 'Просмотры']) * 100, 3)

    data.to_excel('manual_calculates.xlsx', index=False)
