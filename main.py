import tictactoe
import players
import config
def main():
    usePruning=False
    player1=str(input("Do you want go to first (y or n): ")).upper()
    player2=str(input("Do you want computer as opponent (y or n): ")).upper()

    if player1=='y'.upper():
        p1= players.HumanPlayer('X')
        if player2=='y'.upper():
            p2=players.aiPlayer('O')
            usePruning=str(input("Do you want pruning (y or n): "))
            if usePruning=='y'.upper():
                usePruning=True
            else:
                usePruning=False
        else:
            p2=players.HumanPlayer('O')
    else:
        p2= players.HumanPlayer('O')
        if player2=='y'.upper():
            p1=players.aiPlayer('X')
            usePruning=str(input("Do you want pruning (y or n): "))
            if usePruning=='y'.upper():
                usePruning=True
            else:
                usePruning=False     
        else:
            p1=players.HumanPlayer('X')
    tictactoe.printBoard()

    while True:    
        p1.enterSymbol(tictactoe.board,usePruning)
        tictactoe.printBoard()
        tictactoe.checkDraw()
        p1.checkWin(tictactoe.board)
        print(config.counter) 
        config.counter=0
        p2.enterSymbol(tictactoe.board,usePruning)
        print(config.counter) 
        config.counter=0
        tictactoe.printBoard()
        tictactoe.checkDraw()
        p2.checkWin(tictactoe.board)

if __name__ == "__main__":
    main()