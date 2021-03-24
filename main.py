from classes import * 


def printMatrix(size):
    # x: Rows
    # y: Columns 
    for x in range(size):
        for y in range(size):
            print("|", end=" ")
        print()

M = Board(3)
M.matrix[0, 0] = 1
M.matrix[0, 1] = 1
M.matrix[1, 0] = 1
AliveOrNot(M.matrix, M.size, 0, 0) == 1
