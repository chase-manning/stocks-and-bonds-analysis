import get_shiller_data
import matplotlib.pyplot as plt
import pandas as pd

start_amount = float(10_000)

data = get_shiller_data.main()


def main(key, normalize=False):
    x = [obj[key] for obj in data]
    y = [obj["date_fraction"] for obj in data]

    if normalize:
        min_x = min(x)
        max_x = max(x)

        for i in range(len(x)):
            x[i] = (x[i] - min_x) / (max_x - min_x)

    # Chart the data
    plt.plot(y, x, linestyle='-', color='b', label='Line Plot')
    plt.xlabel("Date")
    plt.ylabel(key)
    plt.title(key)
    plt.legend()
    plt.show()
