* class Board:
	- def __init__(self):
		- initialize an empty board as a list
		- currentPlayerMove = 0 (X -> 0 and O -> 1)
	- printBoard()
		- clear the screen and print the current state of the board
	- validMove()
		- checks if a move is possible
	- playerInput()
		- takes moves from players
		- checkValidMove()
		- insert the move into the board
		- printBoard()
	- status()
		- check if X wins
		- check if O wins
		- check if there is a draw
		- other wise return 100
	- declareResult()
		- once the status is win or draw we can print the result

