import get_shiller_data
import matplotlib.pyplot as plt

data = get_shiller_data.main()

print(data[-1]["date_fraction"])
x = [obj["date_fraction"] for obj in data]
y = [obj["cape"] for obj in data]

# Create line plot
plt.plot(x, y, linestyle='-', color='b', label='Line Plot')

# Adding labels and title
# plt.yscale('log')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Matplotlib Chart')
plt.legend()

# Show the plot
plt.show()
