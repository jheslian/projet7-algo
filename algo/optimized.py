"""
Calculate and save to txt file the action bought
"""
import pandas as pd
from pathlib import Path


def optimized(file_path: str, budget: float = 500, ):
    df = pd.read_csv(file_path)
    df = df[df[['price', 'profit']].gt(0.01).all(1)]
    df_sorted = df.sort_values(by=['profit', 'price'], ascending=False)

    profit_list = []
    cost_list = []
    action_list = []
    file = open(f'dataset/txt/{Path(file_path).stem}.txt', 'w')
    for row in df_sorted.itertuples():
        if budget > row.price:
            profit_list.append(row.price * (row.profit / 100))
            cost_list.append(row.price)
            action_list.append(row.name)
            budget = budget - row.price
            file.write(f"{row.name}\t{row.price}\n", )

    file.write("\nTotal costs: {:.2f}".format(sum(cost_list)))
    file.write("\nTotal profits: {:.2f}".format(sum(profit_list)))
    file.close()
