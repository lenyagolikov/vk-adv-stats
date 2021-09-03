import pandas as pd

filename = 'data.xlsx'
filedelta = 'delta.xlsx'


def save_data(adv_id, shows, clicks, lead_form_sends, reach, join_rate, spent, ctr, ecpc, ecpm, total_reach, current_date, current_time):
    try:
        df = pd.read_excel(filename)
        print(f'Opened {filename}')
    except FileNotFoundError:
        df = pd.DataFrame(columns=['ID', 'date', 'time', 'shows', 'clicks', 'leads', 'reach',
                          'join_rate', 'spent', 'cpl', 'ctr', 'ecpc', 'ecpm', 'total_reach'])
        print(f'{filename} does not exist. New dataframe created.')

    df = df.append({'ID': adv_id, 'shows': shows, 'clicks': clicks, 'leads': lead_form_sends,
                    'reach': reach, 'join_rate': join_rate, 'ctr': ctr, 'ecpc': ecpc, 'ecpm': ecpm, 'cpl': 0,
                    'spent': spent, 'total_reach': total_reach, 'date': current_date, 'time': current_time
                    }, ignore_index=True)

    df.to_excel(filename, index=False)
    print(f'Data saved in {filename}')


def save_data_delta():
    data = pd.read_excel(filename)

    for i in range(len(data) - 1, 0, -1):
        data.at[i, 'clicks'] = data.at[i, 'clicks'] - data.at[i - 1, 'clicks']
        data.at[i, 'shows'] = data.at[i, 'shows'] - \
            data.at[i - 1, 'shows']
        data.at[i, 'spent'] = data.at[i, 'spent'] - \
            data.at[i - 1, 'spent']
        data.at[i, 'leads'] = data.at[i, 'leads'] - data.at[i - 1, 'leads']
        data.at[i, 'reach'] = data.at[i, 'reach'] - data.at[i - 1, 'reach']
        data.at[i, 'join_rate'] = data.at[i, 'join_rate'] - \
            data.at[i - 1, 'join_rate']
        data.at[i, 'ecpc'] = data.at[i, 'ecpc'] - data.at[i - 1, 'ecpc']
        data.at[i, 'ecpm'] = data.at[i, 'ecpm'] - data.at[i - 1, 'ecpm']
        data.at[i, 'total_reach'] = data.at[i, 'total_reach'] - \
            data.at[i - 1, 'total_reach']

    data.to_excel(filedelta, index=False)


def calculate_values():
    data = pd.read_excel(filedelta)

    for i in range(len(data)):
        if data.at[i, 'leads'] != 0:
            data.at[i, 'cpl'] = round(
                data.at[i, 'spent'] / data.at[i, 'leads'], 3)
        data.at[i, 'ecpm'] = round(
            (data.at[i, 'spent'] / 1000) * data.at[i, 'shows'], 3)
        if data.at[i, 'clicks'] != 0:
            data.at[i, 'ecpc'] = round(
                data.at[i, 'spent'] / data.at[i, 'clicks'], 3)
        data.at[i, 'ctr'] = round(
            (data.at[i, 'clicks'] / data.at[i, 'shows']) * 100, 3)

    data.to_excel('manual_calculates.xlsx', index=False)
