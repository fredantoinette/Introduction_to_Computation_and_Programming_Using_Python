"""
It is somemtimes illuminating to plot things relative to a baseline, as seen 
in the figure depicting housing prices relative to $200,000. Modify 
plot_housing to produce such plots. The bars below the baseline should be in 
red. Hint: use the bottom keyword argument to plt.bar.
"""


import numpy as np
import matplotlib.pyplot as plt


# Housing prices relative to $200,000

def plot_housing():
    labels, prices = ([], [])
    with open("midWestHousingPrices.csv", "r") as f:
        # Each line of file contains year quarter price
        # for Midwest region of U.S.
        for line in f:
            year, quarter, price = line.split(",")
            label = year[2:4] + "\n Q" + quarter[1]
            labels.append(label)
            prices.append(int(price) / 1000)
    quarters = np.arange(len(labels)) # x coords of bars
    width = 0.8 # Width of bars
    baseline = 200
    bars = plt.bar(quarters, np.array(prices) - baseline, width, 200)
    for bar in bars:
        if bar.get_height() < 0:
            bar.set_color("r")
    plt.axhline(200)
    plt.xticks(quarters + width / 2, labels)
    plt.title("Housing Prices in U.S. Midwest")
    plt.xlabel("Quarter")
    plt.ylabel("Average Price ($1,000\'s)")
    plt.ylim(150, 250)
    plt.show()
    
plot_housing()
