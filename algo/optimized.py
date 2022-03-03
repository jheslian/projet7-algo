"""
Calculate and save to txt file the action bought
"""
import pandas as pd
from pathlib import Path


def save_to_txt(file_path, content):
    file = open(f'dataset/txt/optimize_{Path(file_path).stem}.txt', 'w')
    for key, val in content.items():
        file.write(f"{key}\t{val}\n", )
    file.close()


def get_csv_content(file_path):
    df = pd.read_csv(file_path)
    df = df[df[['price', 'profit']].gt(0.01).all(1)]
    df_sorted = df.sort_values(by=['profit', 'price'], ascending=False)
    return df_sorted


def optimized(file_path: str, budget: float = 500, ):
    profit_list = []
    cost_list = []
    action_bought = {}

    csv_content = get_csv_content(file_path)
    for row in csv_content.itertuples():
        if budget > row.price:
            profit_list.append(row.price * (row.profit / 100))
            cost_list.append(row.price)
            action_bought[row.name] = row.price
            budget = budget - row.price

    action_bought['Costs:'] = "{:.2f}".format(sum(cost_list))
    action_bought['Profits:'] = "{:.2f}".format(sum(profit_list))
    save_to_txt(file_path, action_bought)
