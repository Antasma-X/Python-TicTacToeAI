from abc import ABC
from pickle import TRUE
import random
import tictactoe
import math
import numpy as np
import config

class Player(ABC):
    
    def __init__(self,symbol) -> None:
        self.symbol=symbol

    def checkWin(self,board):
        if board[0]==self.symbol and board[1]==self.symbol and board[2]==self.symbol or board[3]==self.symbol and board[4]==self.symbol and board[5]==self.symbol or board[6]==self.symbol and board[7]==self.symbol and board[8]==self.symbol or board[0]==self.symbol and board[3]==self.symbol and board[6]==self.symbol or board[1]==self.symbol and board[4]==self.symbol and board[7]==self.symbol or board[2]==self.symbol and board[5]==self.symbol and board[8]==self.symbol or board[2]==self.symbol and board[4]==self.symbol and board[6]==self.symbol or board[0]==self.symbol and board[4]==self.symbol and board[8]==self.symbol:
            print(f"Player {self.symbol} wins!")
            exit()

class HumanPlayer(Player):

    def enterSymbol(self,board,usePruning):
        while True:
            temp=int(input("Enter Position: "))
            if type(temp)!=int or temp>8 or board[temp]!=' ' :
                print("Please enter proper postion")
            else:
                board[temp]=self.symbol
                break

class randomPlayer(Player):

    def enterSymbol(self,board,usePruning):
        numbers=[]
        for i in range(9):
            if board[i]==' ':
                numbers.append(i)
        board[random.choice(numbers)]=self.symbol

class aiPlayer(Player):

    def enterSymbol(self,board,usePruning):
        if usePruning:
            pos=self.miniMaxAB(board,0,True,-math.inf,math.inf)
        else: 
            pos=self.miniMax(board,0,True)
        board[pos]=self.symbol

    def checkGameOver(board,playerSymbol,otherPlayerSymbol):
        if board[0]==playerSymbol and board[1]==playerSymbol and board[2]==playerSymbol or board[3]==playerSymbol and board[4]==playerSymbol and board[5]==playerSymbol or board[6]==playerSymbol and board[7]==playerSymbol and board[8]==playerSymbol or board[0]==playerSymbol and board[3]==playerSymbol and board[6]==playerSymbol or board[1]==playerSymbol and board[4]==playerSymbol and board[7]==playerSymbol or board[2]==playerSymbol and board[5]==playerSymbol and board[8]==playerSymbol or board[2]==playerSymbol and board[4]==playerSymbol and board[6]==playerSymbol or board[0]==playerSymbol and board[4]==playerSymbol and board[8]==playerSymbol:
            return True,True,False
        if board[0]==otherPlayerSymbol and board[1]==otherPlayerSymbol and board[2]==otherPlayerSymbol or board[3]==otherPlayerSymbol and board[4]==otherPlayerSymbol and board[5]==otherPlayerSymbol or board[6]==otherPlayerSymbol and board[7]==otherPlayerSymbol and board[8]==otherPlayerSymbol or board[0]==otherPlayerSymbol and board[3]==otherPlayerSymbol and board[6]==otherPlayerSymbol or board[1]==otherPlayerSymbol and board[4]==otherPlayerSymbol and board[7]==otherPlayerSymbol or board[2]==otherPlayerSymbol and board[5]==otherPlayerSymbol and board[8]==otherPlayerSymbol or board[2]==otherPlayerSymbol and board[4]==otherPlayerSymbol and board[6]==otherPlayerSymbol or board[0]==otherPlayerSymbol and board[4]==otherPlayerSymbol and board[8]==otherPlayerSymbol:
            return True,False,True
        for i in range(9):
            if board[i]==' ':
                return False,False,False
        return True,False,False

    def miniMax(self,board,depth,isMax):
        config.counter+=1
        playerSymbol=self.symbol
        otherPlayerSymbol='X' if playerSymbol=='O' else 'O'
        winner,player,otherPlayer = aiPlayer.checkGameOver(board,playerSymbol,otherPlayerSymbol)

        if winner:
            if player:
                return 10- depth
            elif otherPlayer:
                return -10 +depth
            else:
                return 0

        if isMax:
            maxEval=-math.inf
            for i in range(9):
                boardCopy=np.copy(board)
                if boardCopy[i]==' ':
                    boardCopy[i]=playerSymbol
                    eval=self.miniMax(boardCopy,depth+1,False)
                    if eval> maxEval:
                        maxEval=eval
                        bestIndex=i
                    
            if depth==0:
                return bestIndex
            return maxEval
        else:
            minEval=math.inf
            for i in range(9):
                boardCopy=np.copy(board)
                if boardCopy[i]==' ':
                    boardCopy[i]=otherPlayerSymbol
                    eval=self.miniMax(boardCopy,depth+1,True)
                    minEval=min(eval,minEval)
            return minEval
            
    def miniMaxAB(self,board,depth,isMax,alpha,beta):
        config.counter+=1
        playerSymbol=self.symbol
        otherPlayerSymbol='X' if playerSymbol=='O' else 'O'
        winner,player,otherPlayer = aiPlayer.checkGameOver(board,playerSymbol,otherPlayerSymbol)

        if winner:
            if player:
                return 10- depth
            elif otherPlayer:
                return -10 +depth
            else:
                return 0

        if isMax:
            maxEval=-math.inf
            for i in range(9):
                boardCopy=np.copy(board)
                if boardCopy[i]==' ':
                    boardCopy[i]=playerSymbol
                    eval=self.miniMax(boardCopy,depth+1,False,alpha,beta)
                    if eval> maxEval:
                        maxEval=eval
                        bestIndex=i
                    alpha=max(alpha,eval)
                    if beta<=alpha:
                        break
            if depth==0:
                return bestIndex
            return maxEval
        else:
            minEval=math.inf
            for i in range(9):
                boardCopy=np.copy(board)
                if boardCopy[i]==' ':
                    boardCopy[i]=otherPlayerSymbol
                    eval=self.miniMax(boardCopy,depth+1,True,alpha,beta)
                    minEval=min(eval,minEval)
                    beta=min(beta,eval)
                    if beta<=alpha:
                        break
            return minEval
            
            
    
