import numpy as np

def initRandomCells(n, mat, size):
    # Pre: mat (size x size) only contains 0 (dead cels) and n > 0
    # Post: mat contains n cells 
    i = 0
    while (i < n and i < size*size):
        x = np.random.randint(size)
        y = np.random.randint(size)
        if (mat[x, y] != 1):
            mat[x, y] = 1 
            i += 1
    return mat

def aliveAroundCells(mat, size, x, y):
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
    neighbours = aliveAroundCells(mat, size, x, y)
    print("neighbours", neighbours)
    if (neighbours == 2 or neighbours == 3 and mat[x, y] == 1):
        return 1
    elif (neighbours == 3 and mat[x, y] == 0):
        return 1
    return 0

class Board:                                                                    
    def __init__(self, size, init=0):                                                   
        if (size <= 0 or init < 0):
            raise ValueError("size: positive or null\n init: positive\n")
        self.size = size   
        self.matrix = initRandomCells(
                init, 
                np.zeros((size, size), 
                dtype=int), 
                size)
            

