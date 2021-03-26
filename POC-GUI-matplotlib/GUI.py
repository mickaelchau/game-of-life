# I did not know how to to refresh matlab figure so I did a POC

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

cmap = ListedColormap(["black", "white"]) #Colors chosen for the Game
fig, ax = plt.subplots() 
fig.canvas.set_window_title("Game Of Life by Mickael")

ax.axis('off')
for i in range(10):
    v = np.random.randint(2, size=(50, 50)) #Random generation of matrix 
    ax.matshow(v, cmap=cmap)
    plt.draw()
    plt.pause(1)
plt.show(block=True) #Block plot at the end

