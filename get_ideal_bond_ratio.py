import get_shiller_data
import matplotlib.pyplot as plt
import pandas as pd

start_amount = float(10_000)

data = get_shiller_data.main()


def calc(bonds_ratio):
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


def main():
    x = [calc(i / 100) for i in range(0, 100)]
    y = [i for i in range(0, 100)]

    # log the highest value of x and the corresponding y
    max_x = max(x)
    max_y = y[x.index(max_x)]
    print(f"Max value: {max_x}x at {max_y}% bonds")

    # Chart the data
    plt.plot(y, x, linestyle='-', color='b', label='Line Plot')
    plt.xlabel('Bonds Ratio')
    plt.ylabel('Final Returns (x)')
    plt.title('Bonds Ratio vs Final Returns (x)')
    plt.legend()
    plt.show()
