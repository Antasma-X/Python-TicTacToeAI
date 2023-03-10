import numpy as np
board=np.array([' ' for i in range(9)])

def printBoard():
    print("""
    {} | {} | {}  
   -----------
    {} | {} | {}  
   -----------
    {} | {} | {}
                """.format(board[0],board[1],board[2],board[3],board[4],board[5],board[6],board[7],board[8]))

def checkDraw():
    for i in range(9):
        if board[i]==' ':
            return
    print("Draw")
    quit()

def checkDepth():
    counter=0
    for i in range(9):
        if board[i]==' ':
            counter+=1
    return counter






