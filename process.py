import matplotlib.pyplot as plt                                                 
import numpy as np
from matplotlib.colors import ListedColormap, BoundaryNorm    
from matplotlib.ticker import LinearLocator, MultipleLocator

def Input():
    size = int(input("Enter size of Board: "))
    if (size <= 0):
        raise ValueError("Size should be positive")
    steps = int(input("Enter number of steps of the Game: "))
    if (steps <= 0):
        raise ValueError("Steps should be positive")
    duration = float(input("Enter duration between each steps: "))
    if (duration < 0.):
        raise ValueError("Steps should be positive")
    aliveCels = int(input("Enter number of alive cels: "))
    if (aliveCels < 0):
        raise ValueError("Alive Cels should be positive or null")
    return size, steps, duration, aliveCels

def Init():
    (size, steps, duration, aliveCels) = Input()
    pos = []
    print("Enter the coordinates (x, y) of each alive cels: ")
    print("Coordinates must be between 0 and", aliveCels-1)
    print("\ny\n^\n|\n|\n|\n|=====> x")
    for i in range(aliveCels):
        print("cel", i+1,":")
        x = int(input("X: "))
        y = int(input("Y: "))
        pos.append((x, y))
        print()
    return size, pos, steps, duration

def Game(board, n, wait=1):                                          
    #There is the creation of GUI
    cmap = ListedColormap(["white", "black"]) #Colors chosen for the Game       
    bounds = [0, 1, 2]
    norm = BoundaryNorm(bounds, cmap.N)

    fig, ax = plt.subplots()
    fig.canvas.set_window_title("Game Of Life by Mickael")                      

    #grid sugar syntax
    ax.set_xlim(0, board.size)
    ax.set_ylim(0, board.size)
    # Proportion of major sticks => here all 10
    ax.xaxis.set_major_locator(MultipleLocator(10))
    ax.yaxis.set_major_locator(MultipleLocator(10))
    # Proportion of minors sticks => here all 1
    ax.xaxis.set_minor_locator(MultipleLocator(1))
    ax.yaxis.set_minor_locator(MultipleLocator(1))
    ax.grid(which='both', color='#CCCCCC')

    #Dynamic text init
    text = ax.text(board.size+1, board.size+1, "", size="x-large", zorder=1.)
    #text.set_color("red")
    #text.set_zorder(1.)

    v = board.matrix
    maxIter = str(n)
    for i in range(n):                                                          
        #There is sugar syntax to print dynamic text 
        infoInter = "Iterations: " + str(i+1) + "\nFinal iteration: " + maxIter
        text.set_text(infoInter)

        #Refresh figure and axes 
        ax.matshow(v, cmap=cmap, norm=norm, 
            extent=[0, board.size, 0, board.size])                          
        ax.xaxis.set_ticks_position("bottom") #Xaxis starts at the left lower
        plt.pause(wait)                                                         
        board.play()
        fig.canvas.draw()
        v = board.matrix
    plt.show(block=True)
    print("Game has ended.")  

