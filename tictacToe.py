"""write a code for tictactoe """
import random

class TicTacToe:
    
    def __init__(self):
        self.board = []
        
    def createBoard(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append("-")
            self.board.append(row)
            
            
    
    


tic_tic_toe = TicTacToe()
tic_tic_toe.board()