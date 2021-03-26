import matplotlib.pyplot as plt                                                 
from matplotlib.colors import ListedColormap    

def Init():
    size = int(input("Enter size of Board: "))
    steps = int(input("Enter number of steps of the Game: "))
    duration = float(input("Enter duration between each steps: "))
    aliveCels = int(input("Enter number of alive cels: "))
    if (size < 0 or steps < 0 or duration < 0 or aliveCels < 0):
        raise ValueError("variables should be positive")
    pos = []
    print("Enter the coordinates (x, y) of each alive cels: ")
    print("Coordinates must be between 0 and", aliveCels-1)
    print("\nx\n^\n|\n|\n|\n|=====> y")
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
    ax.axis('off')                                                             
    v = board.matrix                                                            
    for i in range(n):                                                          
        ax.matshow(v, cmap=cmap)                                                
        plt.pause(wait)                                                         
        board.play()                                                            
        v = board.matrix                                                        
    plt.show() #Block plot at the end                                           
    print("Game has ended.")  

