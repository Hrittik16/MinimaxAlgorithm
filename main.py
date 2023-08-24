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
        # check if X or O wins
        if self.board[0] == self.board[1] and self.board[1] == self.board[2]:
            if self.board[0] == "X":
                return 1
            elif self.board[0] == "O":
                return -1
        elif self.board[3] == self.board[4] and self.board[4] == self.board[5]:
            if self.board[3] == "X":
                return 1
            elif self.board[3] == "O":
                return -1
        elif self.board[6] == self.board[7] and self.board[7] == self.board[8]:
            if self.board[6] == "X":
                return 1
            elif self.board[6] == "O":
                return -1
        elif self.board[0] == self.board[3] and self.board[3] == self.board[6]:
            if self.board[0] == "X":
                return 1
            elif self.board[0] == "O":
                return -1
        elif self.board[1] == self.board[4] and self.board[4] == self.board[7]:
            if self.board[1] == "X":
                return 1
            elif self.board[1] == "O":
                return -1
        elif self.board[2] == self.board[5] and self.board[5] == self.board[8]:
            if self.board[2] == "X":
                return 1
            elif self.board[2] == "O":
                return -1
        elif self.board[0] == self.board[4] and self.board[4] == self.board[8]:
            if self.board[0] == "X": 
                return 1
            elif self.board[0] == "O":
                return -1
        elif self.board[2] == self.board[4] and self.board[4] == self.board[6]:
            if self.board[2] == "X":
                return 1
            elif self.board[2] == "O":
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
            print("\nThe game ended in a draw!!\n")
        elif val == 1:
            print("\nX has won the game\n")
        elif val == -1:
            print("\nO has won the game")
        
        return 1



if __name__ == "__main__":
    B = Board()
    while(True): # Nothing = 100, X Win = 1, Draw = 0, O Wins = -1
        B.printBoard()
        B.playerInput()
        val = B.status()
        if B.declareResult(val) == 1:
            break


