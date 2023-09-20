import os

class Board:
    def __init__(self):
        self.board = ["." for i in range(9)]
        self.currentPlayerMove = 0   # 0 -> X, 1 -> O

    def printBoard(self):
        os.system("cls")
        print("\n")
        for i in range(3):            
            for j in range(3):
                print(self.board[3*i+j]+" "*3, end="")
            print("\n")

    def validMove(self, index):
        if index.isdigit() == 0:
            return 0
        if int(index) < 1 or int(index) > 9:
            return 0
        return self.board[int(index)-1] == "."

    def playerInput(self):
        if self.currentPlayerMove == 0:
            invalidIndex = 0
            while invalidIndex == 0:
                print("Enter an index for placing X. Indexes are 1-9: ")
                index = input()
                if(self.validMove(index) == 1):
                    self.board[int(index)-1] = "X"
                    invalidIndex = 1
                else:
                    self.printBoard()
                    print("You have entered an invalid index. Try again")
            self.currentPlayerMove = 1
        else:
            invalidIndex = 0
            while invalidIndex == 0:
                print("Enter an index for placing O. Indexes are 1-9: ")
                index = input()
                if(self.validMove(index) == 1):
                    self.board[int(index)-1] = "O"
                    invalidIndex = 1
                else:
                    self.printBoard()
                    print("You have entered a wrong index. Try again")
            self.currentPlayerMove = 0


    def status(self):
        # check rows
        for i in range(3): # all() returns True if all elements of an iterable are true
            if all([self.board[3*i+j] == "X" for j in range(3)]):
                return 1
        for i in range(3):
            if all([self.board[3*i+j] == "O" for j in range(3)]):
                return -1

        # check columns
        for j in range(3):
            if all([self.board[3*i+j] == "X" for i in range(3)]):
                return 1
        for j in range(3):
            if all([self.board[3*i+j] == "O" for i in range(3)]):
                return -1

        # check diagonals
        if all([self.board[3*i+i] == "X" for i in range(3)]):
            return 1
        elif all([self.board[3*i+i] == "O" for i in range(3)]):
            return -1
        if all([self.board[3*(i+1)-(i+1)] == "X" for i in range(3)]):
            return 1
        elif all([self.board[3*(i+1)-(i+1)] == "O" for i in range(3)]):
            return -1


        # check if there is a draw
        emptyCells = 0
        for i in range(9):
            if self.board[i] == ".":
                emptyCells += 1
        if emptyCells == 0: 
            return 0

        return 100 # nothing has happened yet


    def declareResult(self, val):
        if val == 100:
            return 0
        elif val == 0:
            self.printBoard()
            print("\nThe game ended in a draw!!\n")
        elif val == 1:
            self.printBoard()
            print("\nX has won the game\n")
        elif val == -1:
            self.printBoard()
            print("\nO has won the game")
        
        return 1


# This if statement is only executed when the program is run directly by the python interpreter.
# If the file is imported as a module then it won't be executed.
if __name__ == "__main__": 
    B = Board()
    while(True): # Nothing = 100, X Win = 1, Draw = 0, O Wins = -1
        B.printBoard()
        B.playerInput()
        val = B.status()
        if B.declareResult(val) == 1:
            break


