import get_shiller_data
import matplotlib.pyplot as plt
import pandas as pd
import locale

data = get_shiller_data.main()

scale_key = "tr_cape"
cape_values = [obj[scale_key] for obj in data]
min_cape = min(cape_values)
max_cape = max(cape_values)

for obj in data:
    obj[scale_key] = (obj[scale_key] - min_cape) / (max_cape - min_cape)


def main():
    # current_amount = 0
    previous = None
    bonds = 0
    stocks = 0
    for obj in data:
        if (previous is None):
            previous = obj
            continue

        # Calculate the amount of money in stocks and bonds
        bonds_ratio = previous[scale_key]
        stocks_ratio = float(1) - bonds_ratio

        # Adding monthly investment

        # Calculate the amount of money in stocks and bonds
        stocks += obj["cpi"] * stocks_ratio
        bonds += obj["cpi"] * bonds_ratio

        # Get percent increase in the stock market
        key = "real_price"
        profit = obj[key] - previous[key]
        stock_increase = profit / previous[key]
        stocks = stocks * (1 + stock_increase)

        # Get percent increase in the bond market
        key = "real_total_bond_returns"
        profit = obj[key] - previous[key]
        bond_increase = profit / previous[key]
        bonds = bonds * (1 + bond_increase)

        # Calculate the new total amount

        previous = obj

    current_amount = stocks + bonds
    locale.setlocale(locale.LC_ALL, '')
    print("Total amount: ", locale.currency(current_amount, grouping=True))
