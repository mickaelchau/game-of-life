from classes import * 
import numpy as np        
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap   
#import sys

def printM(M):
    for i in range(M.size):
        for j in range(M.size):
            print(M.matrix[i, j], end =" ")
        print()

def matplotlibPrint(board, n, wait=1):
    cmap = ListedColormap(["white", "black"]) #Colors chosen for the Game
    fig, ax = plt.subplots()
    fig.canvas.set_window_title("Game Of Life by Mickael")
    #ax.axis('off')
    v = board.matrix
    for i in range(n):
        ax.matshow(v, cmap=cmap)
        plt.draw()
        plt.pause(wait)
        board.play()
        v = board.matrix
    #print("end")
    plt.show() #Block plot at the end
    

if __name__ == "__main__":
    #print(f"Arguments count: {len(sys.argv)}")
    #for i, arg in enumerate(sys.argv):
     #   print(f"Argument {i:>6}: {arg}")
    M = Board(50, [(25, 25), (25, 26), (25, 27), (24, 27),(23, 26)])
    matplotlibPrint(M, 100, wait=0.2)

