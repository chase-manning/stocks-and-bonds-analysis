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

print(len(data))


def calc(start_index, dca_duration):
    investment_amount = float(1)
    current_amount = 0
    investments_made = 0
    previous = None
    start_cape = data[start_index:][0][scale_key]
    for obj in data[start_index:]:
        if (previous is None):
            previous = obj
            continue

        # Calculate the amount of money in stocks and bonds
        bonds_ratio = 0.35
        stocks_ratio = float(1) - bonds_ratio

        # Calculate the amount of money in stocks and bonds
        stocks = current_amount * stocks_ratio
        bonds = current_amount * bonds_ratio

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
        current_amount = stocks + bonds

        # Adding monthly investment
        if investments_made < dca_duration:
            current_amount += investment_amount / dca_duration
            investments_made += 1

        previous = obj

    return current_amount * start_cape


def main():
    dca_durations = [i for i in range(1, 12 * 10)]

    y = []
    x = dca_durations
    for dca_duration in dca_durations:
        total_profit = 0
        start_indexes = [i for i in range(0, len(data) - dca_duration)]
        for start_index in start_indexes:
            total_profit += calc(start_index, dca_duration)
        if (len(start_indexes) == 0):
            y.append(0)
        else:
            y.append(total_profit / len(start_indexes))

    # log the highest value of x and the corresponding y
    max_x = max(y)
    max_y = x[y.index(max_x)]
    locale.setlocale(locale.LC_ALL, '')
    print(
        f"Max value: {locale.currency(max_x, grouping=True)} at {max_y} months")

    # Chart the data
    plt.plot(x, y, linestyle='-', color='b', label='Line Plot')
    plt.xlabel('DCA Duration')
    plt.ylabel('Average Profit')
    plt.title('DCA Duration vs Average Profit')
    plt.legend()
    plt.show()
