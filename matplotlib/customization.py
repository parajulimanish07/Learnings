import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style


#Customization

# years =[2014, 2015, 2016, 2017, 2018, 2019, 2020]

# income = [55, 50, 60, 65, 70, 75, 80]

# income_ticks = list(range(50, 81, 2))

# plt.plot(years, income)
# plt.title("Income of JOHN over the years (in AUD)", fontsize=30, fontfamily="Arial")
# plt.xlabel("Years")
# plt.ylabel("Yearly Income in AUD")
# plt.yticks(income_ticks, [f"{x}k AUD" for x in income_ticks])

# plt.show()

# stock_a = [100, 120, 130, 140, 150, 160, 170, 180, 190, 200]

# stock_b = [150, 170, 190, 210, 230, 250, 270, 290, 310, 330]

# stock_c = [200, 220, 240, 260, 280, 300, 320, 340, 360, 380]

# plt.plot(stock_a, label="Company A")
# plt.plot(stock_b, label="Company B")
# plt.plot(stock_c, label="Company C")

# plt.legend(loc="lower right")

# plt.show()

#Piechart label


# style.use("dark_background")

# #MATPLOTLIB STYLESHEET FROM MATPLOT WEBSITE

# votes = [100, 200, 300, 400, 500]
# people = ["A", "B", "C", "D", "E"]

# plt.pie(votes, labels=None)
# plt.legend(labels=people)

# plt.show()


# x1, y1 =np.random.random(100), np.random.random(100)
# x2, y2 =np.arange(100), np.random.random(100) #arange creates a sequence of numbers

# plt.figure(1)
# plt.scatter(x1,y1)

# plt.figure(2)
# plt.plot(x2, y2)

# plt.show()


# x = np.arange(100)

# fig, axs = plt.subplots(2, 2)

# axs[0, 0].plot(x,np.sin(x))
# axs[0,0].set_title("Sine Wave")

# axs[0, 1].plot(x,np.cos(x))
# axs[0,1].set_title("Cosine Wave")


# axs[1, 0].plot(x,np.random.random(100))
# axs[1,0].set_title("Random Function")


# axs[1, 1].plot(x,np.log(x))
# axs[1,1].set_title("Log Function")
# axs[1,1].set_xlabel("TEST")

# fig.suptitle("Four Plots")

# plt.tight_layout()

# plt.savefig("fourplots.png", dpi=300) #dpi is dots per inch
