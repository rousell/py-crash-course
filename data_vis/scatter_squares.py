import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.GnBu, edgecolor='none', s=40)

# Set chart title and label axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels
plt.axis([0, max(x_values) * 1.1, 0, max(y_values) * 1.1])

plt.savefig('data_vis/chart_imgs/squares_plot.png', bbox_inches='tight')