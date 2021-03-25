from process import Game, Init
from classes import * 

def main(argv):
    (size, pos, steps, duration) = Init()
    M = Board(size, pos)
    Game(M, steps, wait=duration)
    return True

if __name__ == "__main__":
    main(sys.argv)

