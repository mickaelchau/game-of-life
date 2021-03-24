import numpy as np

def initCells(cells, mat, size):
    # Pre: mat (size x size) only contains 0 (dead cels) and n > 0
    # Post: mat contains n cells 
    longueur = len(cells)
    for i in cells:
        (x, y) = i
        if (x < 0 or y < 0 or y > size or x > size):
            raise ValueError("x and y must be in [0, size-1]")
        mat[x, y] = 1
    return mat

def aliveAroundCells(mat, size, x, y):
    #Pre: mat of sizexsize 
    #Post: return nb of alive neighbours cells of (x, y) cell
    if (x >= size or x < 0 or y >= size or y < 0):
        raise ValueError("x and y must be in [0, size]")
    
    count = 0;
    yminus = y-1 if (y-1 >= 0) else y
    yplus = y+1 if (y+1 < size) else y
    xminus = x-1 if (x-1 >= 0) else x
    xplus = x+1 if (x+1 < size) else x 
    #know limits of the iteration matrix 
    for i in range(xminus, xplus+1):
        for j in range(yminus, yplus+1):
            count += mat[i, j]
    count -= mat[x, y] #Do not want the middle one
    return count

def AliveOrNot(mat, size, x, y):
    #Pre: mat of sizexsize & Use aliveAroundCells
    #Post: Compute if (x, y) cell is alive or dead
    neighbours = aliveAroundCells(mat, size, x, y)
    if (neighbours == 2 or neighbours == 3 and mat[x, y] == 1):
        return 1
    elif (neighbours == 3 and mat[x, y] == 0):
        return 1
    return 0

class Board:                                                                    
    def __init__(self, size, cells=[]):            
        #Post: Init an Empty Board or a Board with init cells
        if (size <= 0):
            raise ValueError("size: positive or null\n")
        self.size = size   
        self.matrix = initCells(
                cells, 
                np.zeros((size, size), 
                dtype=int), 
                size)
"""        
    def play(self):
        for x in range(self.size):
            for y in range(self.size):
                self.matrix[x, y] = AliveOrNot(self.matrix, self.size, x, y)

    def print(self):
        for x in range(self.size):
            for y in range(self.size):
                print("| ", self.matrix[x, y], end=" ")
            print("|")
            print()
"""
