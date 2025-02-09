import get_shiller_data
import matplotlib.pyplot as plt
import pandas as pd

data = get_shiller_data.main()

print(data[-1]["date_fraction"])
x = [obj["date_fraction"] for obj in data]
y = [obj["cape"] for obj in data]

# Create line plot
plt.plot(x, y, linestyle='-', color='b', label='Line Plot')

# Calculate the Exponential Moving Average (EMA)
ema_span = 20  # You can adjust the span for the EMA
y_series = pd.Series(y)
ema = y_series.ewm(span=ema_span, adjust=False).mean()

# Plot the EMA
plt.plot(x, ema, linestyle='--', color='r', label='EMA')
# plt.yscale('log')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Matplotlib Chart')
plt.legend()

# Show the plot
plt.show()
