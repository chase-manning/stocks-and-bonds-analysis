import get_shiller_data
import matplotlib.pyplot as plt
import pandas as pd

start_amount = float(10_000)

data = get_shiller_data.main()


def main(bonds_ratio):
    stocks_ratio = float(1) - bonds_ratio

    current_amount = start_amount
    previous = None
    for obj in data:
        if (previous is None):
            previous = obj
            continue

        # Calculate the amount of money in stocks and bonds
        stocks = current_amount * stocks_ratio
        bonds = current_amount * bonds_ratio

        # Get percent increase in the stock market
        key = "real_price"
        profit = obj[key] - previous[key]
        stock_increase = profit / previous[key]
        new_stock_value = stocks * (1 + stock_increase)

        # Get percent increase in the bond market
        key = "real_total_bond_returns"
        profit = obj[key] - previous[key]
        bond_increase = profit / previous[key]
        new_bond_value = bonds * (1 + bond_increase)

        # Calculate the new total amount
        current_amount = new_stock_value + new_bond_value

        previous = obj

    return current_amount / start_amount
