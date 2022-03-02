"""
Module (name)

description
"""

import pandas as pd
import itertools
from pathlib import Path


def brutforce(file_path: str, budget=500):
    datas = pd.read_csv(file_path, )
    profit = datas.price * (datas.profit / 100)
    df = pd.DataFrame({
        'action': datas.name,
        'price': datas.price,
        'percentage': datas.profit,
        'profit': profit
    })

    tmp_profit = 0
    price_list = ()
    content = pd.DataFrame()

    file = open(f'dataset/txt/{Path(file_path).stem}.txt', 'w')
    for i in df.itertuples():
        for p_list in itertools.combinations(df.price, i.Index + 1):
            total_price = sum(p_list)

            if 495 < total_price <= budget:
                res = df.loc[df['price'].isin(p_list)]
                total_profit = sum(res.profit)
                if tmp_profit < total_profit:
                    tmp_profit = total_profit
                    price_list = res.price
                    content = res
    for rec_index, rec in content.iterrows():
        file.write(f"{rec['action']}\t{rec['price']}\n")

    file.write("\nTotal costs: {:.2f}".format(sum(price_list)))
    file.write("\nTotal profits: {:.2f}".format(tmp_profit))
    file.close()
