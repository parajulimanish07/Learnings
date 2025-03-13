# #matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy.

import numpy as np
import matplotlib.pyplot as plt #usual convention for importing matplotlib

# # Data for plotting

# years = [2006 + x for x in range(16)]
# weights = [80, 83, 84, 85, 86, 82, 81, 79, 83, 85, 86, 87, 88, 89, 90, 91]


# # plt.plot(years, weights, c="b", lw=3, linestyle="--") #scatter plot le dot dot , plot le line chart, lw - line width, linestyle = "--" for dashed line

# plt.plot(years, weights, "r--", lw=3)
# plt.show()
# #Scatter plot

# # plt.scatter(X_data, y_data, c="#0f0", s=150, marker ="*", alpha=0.3) #c is color, s is size of the dots, marker is the shape of the dots, alpha is the transparency of the dots



# X= [ "C++", "Java", "Python", "Ruby", "C#", "PHP"]
# y = [ 10, 30, 150, 4, 55, 60]

# plt.bar(X, y, color="r", align="edge", width=0.5, edgecolor="green", lw=6) #bar diagram
# plt.show()

#histogram - shows the frequency of each data point

# ages = np.random.normal(20, 1.5, 1000) #mean, standard deviation, number of data points
 # plt.hist(ages, bins =[ages.min(), 18, 21, ages.max()])
# plt.hist(ages, bins=20, cumulative=True) #cumulative mean the frequency of the data points will be added cumulatively
# plt.show()

#piecharts

# langs = ["Python", "C++", "C#", "Java", "PHP"]
# votes = [50, 24, 14, 6, 17]
# explodes = [0,0,0,0.2,0] #exploding" means pulling one or more slices of the pie away from the center to make them stand out. 
 

# plt.pie(votes, labels=langs, explode=explodes,
#         autopct="%.2f%%", startangle=90)
# plt.show()

#Boxplot

# heights = np.random.normal(172, 8, 300) #mean , standard deviation , number of data points

# plt.boxplot(heights)
# plt.show()

# first = np.linspace(0,10,25)
# second = np.linspace(10,200,25)
# third = np.linspace(200,210,25)
# fourth = np.linspace(210,230,25)

# data = np.concatenate([first, second, third, fourth])

# plt.boxplot(data)
# plt.show()

#HEATMAPS, CRAZY SILHOUETTE PLOTS (WE DONT DISCUSS HERE)

