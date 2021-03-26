import matplotlib.pyplot as plt                                                 
from matplotlib.colors import ListedColormap    
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
    cmap = ListedColormap(["white", "black"]) #Colors chosen for the Game       
    fig, ax = plt.subplots()
    fig.canvas.set_window_title("Game Of Life by Mickael")                      
    text = ax.text(0, 0, "")
    ax.axis('off')                                                             
    v = board.matrix
    maxIter = str(n)
    for i in range(n):                                                          
        infoInter = "Iterations: " + str(i+1) + "\nFinal iteration: " + maxIter
        text.set_text(infoInter)
        ax.matshow(v, cmap=cmap)                                                
        plt.pause(wait)                                                         
        board.play()
        fig.canvas.draw()
        v = board.matrix
    plt.show(block=True)
    print("Game has ended.")  

