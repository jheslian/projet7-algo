"""
Module (name)

description
"""

import pandas as pd
import itertools
from pathlib import Path


def save_to_txt(file_path, content):
    file = open(f'dataset/txt/brutforce_{Path(file_path).stem}.txt', 'w')
    for key, val in content.items():
        file.write(f"{key}\t{val}\n", )
    file.close()


def get_csv_content(file_path):
    datas = pd.read_csv(file_path)
    profit = datas.price * (datas.profit / 100)
    df = pd.DataFrame({
        'action': datas.name,
        'price': datas.price,
        'percentage': datas.profit,
        'profit': profit
    })
    return df


def brutforce(file_path: str, budget=500):
    csv_content = get_csv_content(file_path)
    tmp_profit = 0
    price_list = ()
    action_bought = {}
    content = pd.DataFrame()

    for i in csv_content.itertuples():
        for p_list in itertools.combinations(csv_content.price, i.Index + 1):
            total_price = sum(p_list)

            if 495 < total_price <= budget:
                res = csv_content.loc[csv_content['price'].isin(p_list)]
                total_profit = sum(res.profit)
                if tmp_profit < total_profit:
                    tmp_profit = total_profit
                    price_list = res.price
                    content = res
    for rec_index, rec in content.iterrows():
        action_bought[rec['action']] = rec['price']

    action_bought['Costs:'] = "{:.2f}".format(sum(price_list))
    action_bought['Profits:'] = "{:.2f}".format(tmp_profit)
    save_to_txt(file_path, action_bought)
