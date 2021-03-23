from classes import * 


def printMatrix(size):
    # x: Rows
    # y: Columns 
    for x in range(size):
        for y in range(size):
            print("|", end=" ")
        print()

N = Board(3, init=5)
