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
            Board(1, cells=[(-1, 2)])

    def testWithInit(self):
        M = Board(3, cells=[(0, 0), (0, 1), (1, 1), (2, 2), (1, 0)])
        assert (M.size == 3 and countOnes(M.matrix, 3) == 5)

    def testTooManyOne(self):
        M = Board(1, cells=[(0,0)])
        assert (M.size == 1 and countOnes(M.matrix, 1) == 1)

class TestAliveArroundCells:
    def testNegativeCoordinates(self):
        M = Board(1, cells=[])
        with pytest.raises(ValueError):
            aliveAroundCells(M.matrix, M.size, -1, 2)

    def testNoAlive(self):
        M = Board(3)
        assert(aliveAroundCells(M.matrix, M.size, 1, 1) == 0)
    
    def testMiddleAlive(self):
        M = Board(3)
        M.matrix[1, 1] = 1
        assert(aliveAroundCells(M.matrix, M.size, 1, 1) == 0)

    def testNormalCase(self):
        M = Board(3)
        M.matrix[1, 2] = 1
        M.matrix[2, 2] = 1
        M.matrix[1, 0] = 1
        assert(aliveAroundCells(M.matrix, M.size, 1, 1) == 3)

    def testCornerCase1(self):
        M = Board(3)
        M.matrix[0, 0] = 1
        M.matrix[0, 1] = 1
        M.matrix[0, 2] = 1
        assert(aliveAroundCells(M.matrix, M.size, 0, 0) == 1)

    def testCornerCase2(self):
        M = Board(3)
        M.matrix[0, 1] = 1
        M.matrix[1, 1] = 1
        M.matrix[1, 2] = 1
        assert(aliveAroundCells(M.matrix, M.size, 1, 1) == 2)

class TestAliveOrNot:

    def testNoAlive(self):
        M = Board(3)
        assert(AliveOrNot(M.matrix, M.size, 1, 1) == 0)
    
    def test3AliveDeadInMiddle(self):
        M = Board(3)
        M.matrix[0, 1] = 1
        M.matrix[1, 0] = 1
        M.matrix[1, 2] = 1
        assert(AliveOrNot(M.matrix, M.size, 1, 1) == 1)

    def test3AliveAliveInMiddle(self):
        M = Board(3)
        M.matrix[0, 1] = 1
        M.matrix[1, 0] = 1
        M.matrix[1, 2] = 1
        M.matrix[1, 1] = 1
        assert(AliveOrNot(M.matrix, M.size, 1, 1) == 1)

    def test2AliveAndAlive(self):
        M = Board(3)
        M.matrix[0, 0] = 1
        M.matrix[0, 1] = 1
        M.matrix[1, 0] = 1
        assert(AliveOrNot(M.matrix, M.size, 0, 0) == 1)

    def test4AliveAndAlive(self):
        M = Board(3)
        M.matrix[0, 1] = 1
        M.matrix[1, 1] = 1
        M.matrix[1, 2] = 1
        M.matrix[2, 1] = 1
        M.matrix[2, 0] = 1
        M.matrix[0, 2] = 1
        assert(AliveOrNot(M.matrix, M.size, 1, 1) == 0)

    def test1AliveAndAlive(self):
        M = Board(3)
        M.matrix[0, 0] = 1
        M.matrix[0, 1] = 1
        assert(AliveOrNot(M.matrix, M.size, 0, 0) == 0)

class TestBoardPlay:
    def testBlinker(self):
        M = Board(3)
        M.matrix[0, 1] = 1
        M.matrix[1, 1] = 1
        M.matrix[2, 1] = 1
        M.play()
        assert(M.matrix[1, 0] == 1 and M.matrix[1, 1] == 1 
            and M.matrix[1, 2] == 1 and countOnes(M.matrix, M.size) == 3)

    def testToad(self):
        M = Board(4)
        M.matrix[2, 0] = 1
        M.matrix[2, 1] = 1
        M.matrix[2, 2] = 1
        M.matrix[1, 1] = 1
        M.matrix[1, 2] = 1
        M.matrix[1, 3] = 1
        M.play()
        assert(M.matrix[2, 0] == 1 and M.matrix[3, 1] == 1 
            and M.matrix[1, 0] == 1 and M.matrix[0, 2] == 1 
            and M.matrix[1, 3] == 1 and M.matrix[2, 3] == 1 
            and countOnes(M.matrix, M.size) == 6)

    def testBlock(self):
        M = Board(4)
        M.matrix[1, 1] = 1
        M.matrix[1, 2] = 1
        M.matrix[2, 1] = 1
        M.matrix[2, 2] = 1
        M.play()
        assert(M.matrix[1, 1] == 1 and M.matrix[1, 2] == 1
            and M.matrix[2, 1] == 1 and M.matrix[2, 2] == 1
            and countOnes(M.matrix, M.size) == 4)

    def testBoat(self):
        M = Board(5)
        M.matrix[1, 1] = 1
        M.matrix[1, 2] = 1
        M.matrix[2, 1] = 1
        M.matrix[2, 3] = 1
        M.matrix[3, 2] = 1
        M.play()
        assert(M.matrix[1, 1] == 1 and M.matrix[1, 2] == 1
            and M.matrix[2, 1] == 1 and M.matrix[2, 3] == 1
            and M.matrix[3, 2] == 1 and countOnes(M.matrix, M.size) == 5)

