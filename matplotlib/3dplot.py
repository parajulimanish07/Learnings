import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import random

# ax= plt.axes(projection= "3d")

# x= np.random.random(100)
# y= np.random.random(100)
# z= np.random.random(100)

# x = np.arange(-5, 5, 0.1)
# y = np.arange(-5, 5, 0.1)

# X,Y = np.meshgrid(x,y)
# Z = np.sin(X) + np.cos(Y)





# ax.plot_surface(X,Y,Z, cmap= "Spectral")
# ax.set_title("3D Plot")
# ax.set_xlabel("X-axis")
# ax.view_init(azim=0, elev=90) #azim is default for default values, elev is the elevation of the plot
# plt.show()



#ANIMATION

heads_tails = [0,0]

for _ in range (100000):
    heads_tails[random.randint(0,1)] += 1
    plt.bar(["Heads", "Tails"], heads_tails, color=["red", "blue", ])
    plt.pause(0.001)

plt.show()

