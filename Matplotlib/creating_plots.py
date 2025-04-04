from matplotlib import pyplot as plt
import numpy as np

# print(plt.style.use("fivethirtyeight"))
# Enable XKCD-style sketch plots
plt.rcParams["font.family"] = "Nakula"
# plt.xkcd()

# Ages of developers
ages_x = [
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    30,
    31,
    32,
    33,
    34,
    35,
    36,
    37,
    38,
    39,
    40,
    41,
    42,
    43,
    44,
    45,
    46,
    47,
    48,
    49,
    50,
    51,
    52,
    53,
    54,
    55,
]

x_indexes = np.arange(len(ages_x))
width = 0.25

# Median salary data for Python developers
py_dev_y = [
    20046,
    17100,
    20000,
    24744,
    30500,
    37732,
    41247,
    45372,
    48876,
    53850,
    57287,
    63016,
    65998,
    70003,
    70000,
    71496,
    75370,
    83640,
    84666,
    84392,
    78254,
    85000,
    87038,
    91991,
    100000,
    94796,
    97962,
    93302,
    99240,
    102736,
    112285,
    100771,
    104708,
    108423,
    101407,
    112542,
    122870,
    120000,
]

# Plotting Python developers' salary data
# plot() takes x-axis and y-axis to plot the data label is used to show what the line describes
# plot default shows line chart
# plt.plot(ages_x, py_dev_y, label="Python")

# Median salary data for JavaScript developers
js_dev_y = [
    16446,
    16791,
    18942,
    21780,
    25704,
    29000,
    34372,
    37810,
    43515,
    46823,
    49293,
    53437,
    56373,
    62375,
    66674,
    68745,
    68746,
    74583,
    79000,
    78508,
    79996,
    80403,
    83820,
    88833,
    91660,
    87892,
    96243,
    90000,
    99313,
    91660,
    102264,
    100000,
    100000,
    91660,
    99240,
    108000,
    105000,
    104000,
]

# Plotting JavaScript developers' salary data
# plt.plot(ages_x, js_dev_y, label="JavaScript")

# Median salary data for all developers
dev_y = [
    17784,
    16500,
    18012,
    20628,
    25206,
    30252,
    34368,
    38496,
    42000,
    46752,
    49320,
    53200,
    56000,
    62316,
    64928,
    67317,
    68748,
    73752,
    77232,
    78000,
    78508,
    79536,
    82488,
    88935,
    90000,
    90056,
    95000,
    90000,
    91633,
    91660,
    98150,
    98964,
    100000,
    98988,
    100000,
    108923,
    105000,
    103117,
]

# Plotting salary data for all developers with different line style and color
# plt.plot(ages_x, dev_y, color="#444444", linestyle="--", label="All Devs")

# Adding labels and title to the plot
plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")
plt.title("Median Salary (USD) by Age")

# Adding a legend to distinguish the lines
plt.legend()

# adding a grid to the graph
# plt.grid()

# Adjusting the layout for better fit
plt.tight_layout()

# Saving the plot to a file
# plt.savefig("plot.png")

# Displaying the plot
# plt.show()

# displaying the data using the bar chart (vertical chart)
plt.bar(x_indexes - width, py_dev_y, width=width, color="#008fd5", label="Python")
plt.bar(x_indexes, js_dev_y, width=width, color="#e5ae38", label="JavaScript")
plt.bar(x_indexes + width, dev_y, width=width, color="#444444", label="Developer")

# Adding labels and title to the plot
plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")
plt.title("Median Salary (USD) by Age")

plt.legend()

plt.xticks(ticks=x_indexes, labels=ages_x)

plt.tight_layout()

plt.show()
