from classes import *
import pytest

def countOnes(mat, size):
#count the alive cells
    ones = 0
    for x in range(size):
        for y in range(size):
            if (mat[x][y] != 0):
                ones += 1
    return ones

class TestBoardInitialization:
    def testNoInit(self): 
        M = Board(5)
        assert (M.size == 5 and countOnes(M.matrix, 5) == 0)
    
    def testNegativeNumber(self):
        with pytest.raises(ValueError):
            Board(-1)

    def testNegativeInit(self):
        with pytest.raises(ValueError):
            Board(1, init=-5)

    def testWithInit(self):
        M = Board(3, init=5)
        assert (M.size == 3 and countOnes(M.matrix, 3) == 5)

    def testTooManyOne(self):
        M = Board(1, init=5)
        assert (M.size == 1 and countOnes(M.matrix, 1) == 1)

class TestBoardAliveArroundCells:
    def testiNegativeCoordinates(self):
        M = Board(1, init=5)
        with pytest.raises(ValueError):
            M.aliveAroundCells(-1,2)

    def testNoAlive(self):
        M = Board(3)
        assert(M.aliveAroundCells(1, 1) == 0)
    
    def testMiddleAlive(self):
        M = Board(3)
        M.matrix[1, 1] = 1
        assert(M.aliveAroundCells(1, 1) == 0)

    def testNormalCase(self):
        M = Board(3)
        M.matrix[1, 2] = 1
        M.matrix[2, 2] = 1
        M.matrix[1, 0] = 1
        assert(M.aliveAroundCells(1, 1) == 3)

    def testCornerCase1(self):
        M = Board(3)
        M.matrix[0, 0] = 1
        M.matrix[0, 1] = 1
        M.matrix[0, 2] = 1
        assert(M.aliveAroundCells(0, 0) == 1)

    def testCornerCase2(self):
        M = Board(3)
        M.matrix[0, 1] = 1
        M.matrix[1, 1] = 1
        M.matrix[1, 2] = 1
        assert(M.aliveAroundCells(1, 1) == 2)
