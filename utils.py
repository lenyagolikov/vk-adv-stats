import pandas as pd

filename = 'data.xlsx'


def save_data(adv_id, shows, clicks, spent, current_time):
    try:
        df = pd.read_excel(filename)
        print(f'Opened {filename}')
    except FileNotFoundError:
        df = pd.DataFrame(columns=['ID', 'shows', 'clicks', 'spent', 'time'])
        print(f'{filename} does not exist. New dataframe created.')

    df = df.append({'ID': adv_id, 'shows': shows, 'clicks': clicks,
                    'spent': spent, 'time': current_time}, ignore_index=True)

    df.to_excel(filename, index=False)
    print(f'Data saved in {filename}')


def delta():
    data = pd.read_excel(filename)

    for i in range(len(data) - 1, 0, -1):
        data.at[i, 'clicks'] = data.at[i, 'clicks'] - data.at[i - 1, 'clicks']
        data.at[i, 'shows'] = data.at[i, 'shows'] - \
            data.at[i - 1, 'shows']
        data.at[i, 'spent'] = data.at[i, 'spent'] - \
            data.at[i - 1, 'spent']

    data.to_excel('delta.xlsx', index=False)
