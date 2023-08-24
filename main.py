import os

class Board:
    def __init__(self):
        self.board = ["." for i in range(9)]
        self.currentPlayerMove = 0

    def printBoard(self):
        os.system("cls")
        print("\n")
        for i in range(3):            
            for j in range(3):
                print(self.board[3*i+j]+" "*3, end="")
            print("\n")

    def validMove(self, index):
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
                    print("You have entered an invalid index. Try again")
                
    def status(self):
        # check if X - wins
        # check if O - wins


        # check if there is a draw
        emptyCells = 0
        for i in range(9):
            if self.board[i] == ".":
                emptyCells += 1
        if emptyCells == 0: 
            return 0

        return 100


if __name__ == "__main__":
    B = Board()
    while(B.status() == 100): # Nothing = 100, Win = 1, Draw = 0, Loss = -1
        B.printBoard()
        B.playerInput()
        B.status()


