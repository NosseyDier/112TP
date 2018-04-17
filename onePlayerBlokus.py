import math
import string
import copy
import random
from tkinter import *
from piece import Piece

# From 15-112 Website, 2D Lists section
def make2dList(rows, cols):
	a=[]
	for row in range(rows): a += [["grey"]*cols]
	return a

tPc = [[True, True, True],[False, True, False], [False, True, False]]
twoThreePc = [[False, True],[False,True], [True, True],[True, False]]
stepPc = [[False, True, True], [True, True, False], [True, False, False]]
zPc = [[True, True, False], [False, True, False], [False, True, True]]
cPc = [[True, True], [True, False], [True, True]]
bPc = [[True, False], [True, True], [True, True]]
plusPc = [[False, True, False], [True, True, True], [False, True, False]]
fiveLongPc = [[True],[True],[True],[True],[True]]
bigLPc = [[False, False, True],[False, False, True], [True, True, True]]
weirdPc = [[True, True, False], [False, True, True], [False, True, False]]
oneFivePc = [[False, True], [True, True], [False, True], [False, True]]
tallLPc = [[True, False], [True, False], [True, False],[True, True]]

fourLPc = [[True, True], [False, True], [False, True]]
sPc = [[True, False], [True, True], [False, True]]
fourTallPc = [[True],[True],[True],[True]]
squarePc = [[True, True], [True, True]]
fourTPc = [[True, False], [True, True], [True, False]]

threeTallPc = [[True],[True],[True]]
threeLPc = [[True, False], [True, True]]

twoPc = [[True], [True]]

onePc = [[True]]

def addYellowPieces(data):
	top = 5
	mid = top+ 4*data.cellSize
	bot = mid + 4*data.cellSize
	data.allOutsidePieces.append(Piece(tPc, 5, (data.sideMargin, top), "Yellow"))
	data.allOutsidePieces.append(Piece(twoThreePc, 5, (data.sideMargin+4*data.cellSize, top), "Yellow"))
	data.allOutsidePieces.append(Piece(stepPc, 5,  (data.sideMargin + 7*data.cellSize, top), "Yellow"))
	data.allOutsidePieces.append(Piece(zPc, 5, (data.sideMargin+11*data.cellSize, top), "Yellow"))
	data.allOutsidePieces.append(Piece(cPc, 5, (data.sideMargin + 15*data.cellSize, top), "Yellow"))
	data.allOutsidePieces.append(Piece(bPc, 5, (data.sideMargin+18*data.cellSize,top), "Yellow"))
	data.allOutsidePieces.append(Piece(plusPc, 5, (data.sideMargin, mid), "Yellow"))
	data.allOutsidePieces.append(Piece(bigLPc, 5, (data.sideMargin+4*data.cellSize, mid), "Yellow"))
	data.allOutsidePieces.append(Piece(twoPc, 2, (data.sideMargin + 8*data.cellSize, mid+data.cellSize), "Yellow"))
	data.allOutsidePieces.append(Piece(fiveLongPc, 5, (data.sideMargin + 10*data.cellSize, mid-data.cellSize), "Yellow"))
	data.allOutsidePieces.append(Piece(onePc, 1, (data.sideMargin + 12*data.cellSize, mid+ 2 *data.cellSize), "Yellow"))
	data.allOutsidePieces.append(Piece(weirdPc, 5, (data.sideMargin + 13*data.cellSize, mid), "Yellow"))
	data.allOutsidePieces.append(Piece(oneFivePc, 5, (data.sideMargin + 17*data.cellSize, mid), "Yellow"))
	data.allOutsidePieces.append(Piece(tallLPc, 5, (data.sideMargin, bot), "Yellow"))
	data.allOutsidePieces.append(Piece(fourLPc, 4, (data.sideMargin+2*data.cellSize, bot), "Yellow"))
	data.allOutsidePieces.append(Piece(sPc, 4, (data.sideMargin+5*data.cellSize, bot), "Yellow"))
	data.allOutsidePieces.append(Piece(fourTallPc, 4, (data.sideMargin+8*data.cellSize, bot), "Yellow"))
	data.allOutsidePieces.append(Piece(squarePc, 4, (data.sideMargin+10*data.cellSize, bot + data.cellSize), "Yellow"))
	data.allOutsidePieces.append(Piece(fourTPc, 4, (data.sideMargin+13*data.cellSize, bot), "Yellow"))
	data.allOutsidePieces.append(Piece(threeTallPc, 3, (data.sideMargin+16*data.cellSize, bot), "Yellow"))
	data.allOutsidePieces.append(Piece(threeLPc, 3, (data.sideMargin+18*data.cellSize, bot + data.cellSize), "Yellow"))

def addBluePieces(data):
	top = data.height - data.topMargin + (3 * data.cellSize)
	mid = top+ 4*data.cellSize
	bot = mid + 4*data.cellSize
	data.allOutsidePieces.append(Piece(tPc, 5, (data.sideMargin, top), "Blue"))
	data.allOutsidePieces.append(Piece(twoThreePc, 5, (data.sideMargin+4*data.cellSize, top), "Blue"))
	data.allOutsidePieces.append(Piece(stepPc, 5, (data.sideMargin + 7*data.cellSize, top), "Blue"))
	data.allOutsidePieces.append(Piece(zPc, 5, (data.sideMargin+11*data.cellSize, top), "Blue"))
	data.allOutsidePieces.append(Piece(cPc, 5, (data.sideMargin + 15*data.cellSize, top), "Blue"))
	data.allOutsidePieces.append(Piece(bPc, 5, (data.sideMargin+18*data.cellSize,top), "Blue"))
	data.allOutsidePieces.append(Piece(plusPc, 5,(data.sideMargin, mid), "Blue"))
	data.allOutsidePieces.append(Piece(bigLPc, 5, (data.sideMargin+4*data.cellSize, mid), "Blue"))
	data.allOutsidePieces.append(Piece(twoPc, 2, (data.sideMargin + 8*data.cellSize, mid+data.cellSize), "Blue"))
	data.allOutsidePieces.append(Piece(fiveLongPc, 5, (data.sideMargin + 10*data.cellSize, mid-data.cellSize), "Blue"))
	data.allOutsidePieces.append(Piece(onePc, 1, (data.sideMargin + 12*data.cellSize, mid+ 2 *data.cellSize), "Blue"))
	data.allOutsidePieces.append(Piece(weirdPc, 5, (data.sideMargin + 13*data.cellSize, mid), "Blue"))
	data.allOutsidePieces.append(Piece(oneFivePc, 5,(data.sideMargin + 17*data.cellSize, mid), "Blue"))
	data.allOutsidePieces.append(Piece(tallLPc, 5, (data.sideMargin, bot), "Blue"))
	data.allOutsidePieces.append(Piece(fourLPc, 4, (data.sideMargin+2*data.cellSize, bot), "Blue"))
	data.allOutsidePieces.append(Piece(sPc, 4, (data.sideMargin+5*data.cellSize, bot), "Blue"))
	data.allOutsidePieces.append(Piece(fourTallPc, 4, (data.sideMargin+8*data.cellSize, bot), "Blue"))
	data.allOutsidePieces.append(Piece(squarePc, 4, (data.sideMargin+10*data.cellSize, bot + data.cellSize), "Blue"))
	data.allOutsidePieces.append(Piece(fourTPc, 4, (data.sideMargin+13*data.cellSize, bot), "Blue"))
	data.allOutsidePieces.append(Piece(threeTallPc, 3, (data.sideMargin+16*data.cellSize, bot), "Blue"))
	data.allOutsidePieces.append(Piece(threeLPc, 3, (data.sideMargin+18*data.cellSize, bot + data.cellSize), "Blue"))

def addRedPieces(data):
	top = data.topMargin + 5 * data.cellSize
	mid = top+ 4*data.cellSize
	bot = mid + 4*data.cellSize
	data.allOutsidePieces.append(Piece(tPc, 5, (5, top), "Red"))
	data.allOutsidePieces.append(Piece(twoThreePc, 5, (5+4*data.cellSize, top), "Red"))
	data.allOutsidePieces.append(Piece(stepPc, 5, (5 + 7*data.cellSize, top), "Red"))
	data.allOutsidePieces.append(Piece(zPc, 5, (5+11*data.cellSize, top), "Red"))
	data.allOutsidePieces.append(Piece(cPc, 5, (5 + 15*data.cellSize, top), "Red"))
	data.allOutsidePieces.append(Piece(bPc, 5, (5+18*data.cellSize,top), "Red"))
	data.allOutsidePieces.append(Piece(plusPc, 5,(5, mid), "Red"))
	data.allOutsidePieces.append(Piece(bigLPc, 5, (5+4*data.cellSize, mid), "Red"))
	data.allOutsidePieces.append(Piece(twoPc, 2, (5 + 8*data.cellSize, mid+data.cellSize), "Red"))
	data.allOutsidePieces.append(Piece(fiveLongPc, 5, (5 + 10*data.cellSize, mid-data.cellSize), "Red"))
	data.allOutsidePieces.append(Piece(onePc, 1, (5 + 12*data.cellSize, mid+ 2 *data.cellSize), "Red"))
	data.allOutsidePieces.append(Piece(weirdPc, 5, (5 + 13*data.cellSize, mid), "Red"))
	data.allOutsidePieces.append(Piece(oneFivePc, 5,(5 + 17*data.cellSize, mid), "Red"))
	data.allOutsidePieces.append(Piece(tallLPc, 5, (5, bot), "Red"))
	data.allOutsidePieces.append(Piece(fourLPc, 4, (5+2*data.cellSize, bot), "Red"))
	data.allOutsidePieces.append(Piece(sPc, 4, (5+5*data.cellSize, bot), "Red"))
	data.allOutsidePieces.append(Piece(fourTallPc, 4, (5+8*data.cellSize, bot), "Red"))
	data.allOutsidePieces.append(Piece(squarePc, 4, (5+10*data.cellSize, bot + data.cellSize), "Red"))
	data.allOutsidePieces.append(Piece(fourTPc, 4, (5+13*data.cellSize, bot), "Red"))
	data.allOutsidePieces.append(Piece(threeTallPc, 3, (5+16*data.cellSize, bot), "Red"))
	data.allOutsidePieces.append(Piece(threeLPc, 3, (5+18*data.cellSize, bot + data.cellSize), "Red"))

def addGreenPieces(data):
	top = data.topMargin + 5 * data.cellSize
	mid = top+ 4*data.cellSize
	bot = mid + 4*data.cellSize
	side = data.width - data.sideMargin + 3 * data.cellSize
	data.allOutsidePieces.append(Piece(tPc, 5, (side, top), "Green"))
	data.allOutsidePieces.append(Piece(twoThreePc, 5, (side+4*data.cellSize, top), "Green"))
	data.allOutsidePieces.append(Piece(stepPc, 5, (side + 7*data.cellSize, top), "Green"))
	data.allOutsidePieces.append(Piece(zPc, 5, (side+11*data.cellSize, top), "Green"))
	data.allOutsidePieces.append(Piece(cPc, 5, (side + 15*data.cellSize, top), "Green"))
	data.allOutsidePieces.append(Piece(bPc, 5, (side+18*data.cellSize,top), "Green"))
	data.allOutsidePieces.append(Piece(plusPc, 5,(side, mid), "Green"))
	data.allOutsidePieces.append(Piece(bigLPc, 5, (side+4*data.cellSize, mid), "Green"))
	data.allOutsidePieces.append(Piece(twoPc, 2, (side + 8*data.cellSize, mid+data.cellSize), "Green"))
	data.allOutsidePieces.append(Piece(fiveLongPc, 5, (side + 10*data.cellSize, mid-data.cellSize), "Green"))
	data.allOutsidePieces.append(Piece(onePc, 1, (side + 12*data.cellSize, mid+ 2 *data.cellSize), "Green"))
	data.allOutsidePieces.append(Piece(weirdPc, 5, (side + 13*data.cellSize, mid), "Green"))
	data.allOutsidePieces.append(Piece(oneFivePc, 5,(side + 17*data.cellSize, mid), "Green"))
	data.allOutsidePieces.append(Piece(tallLPc, 5, (side, bot), "Green"))
	data.allOutsidePieces.append(Piece(fourLPc, 4, (side+2*data.cellSize, bot), "Green"))
	data.allOutsidePieces.append(Piece(sPc, 4, (side+5*data.cellSize, bot), "Green"))
	data.allOutsidePieces.append(Piece(fourTallPc, 4, (side+8*data.cellSize, bot), "Green"))
	data.allOutsidePieces.append(Piece(squarePc, 4, (side+10*data.cellSize, bot + data.cellSize), "Green"))
	data.allOutsidePieces.append(Piece(fourTPc, 4, (side+13*data.cellSize, bot), "Green"))
	data.allOutsidePieces.append(Piece(threeTallPc, 3, (side+16*data.cellSize, bot), "Green"))
	data.allOutsidePieces.append(Piece(threeLPc, 3, (side+18*data.cellSize, bot + data.cellSize), "Green"))

def init(data):
	data.cellSize = 15
	data.rows = 20
	data.cols = 20
	data.topMargin = 230
	data.sideMargin = 360
	data.allOutsidePieces = []
	addYellowPieces(data)
	addBluePieces(data)
	addRedPieces(data)
	addGreenPieces(data)
	data.board = make2dList(data.rows, data.cols)
	data.selectedPiece = None
	data.oldXCoordOfSelected = None
	data.oldYCoordOfSelected = None
	data.placedOnBoard = False

def playBlokus(rows = 20, cols = 20):
	cellSize = 15
	topMargin = 230
	sideMargin = 360
	# calculates necessary window width and height and passes to run()
	windowWidth = (2 * sideMargin) + (cols * cellSize)
	windowHeight = (2 * topMargin) + (rows * cellSize)
	run(windowWidth, windowHeight)

def drawGreyBackground(canvas, data):
	topX = data.sideMargin - data.cellSize
	topY = data.topMargin - data.cellSize
	botX = data.width - data.sideMargin + data.cellSize
	botY = data.height - data.topMargin + data.cellSize
	canvas.create_rectangle(topX, topY, botX, botY, fill = 'grey', width = 2)

def drawBoard(canvas, data):
	for row in range(len(data.board)):
		for col in range(len(data.board[0])):
			drawCell(canvas, data, row, col, data.board[row][col])

def drawCell(canvas, data, row, col, color):
	# calculates to top left and bottom right coordinates and draws 
	topX = data.sideMargin + (data.cellSize * col)
	botX = data.sideMargin + (data.cellSize * (col + 1))
	topY = data.topMargin + (data.cellSize * row)
	botY = data.topMargin + (data.cellSize * (row + 1))
	canvas.create_rectangle(topX, topY, botX, botY, fill = color, width = 1)

def drawRemainingPieces(canvas, data):
	for piece in data.allOutsidePieces:
		for row in range(len(piece.profile)):
			for col in range(len(piece.profile[0])):
				if piece.profile[row][col] == True:
					topX = piece.x + col*data.cellSize
					topY = piece.y + row*data.cellSize
					canvas.create_rectangle(topX, topY, topX + data.cellSize, topY + data.cellSize, fill = piece.color)

def timerFired(data):
	pass

def checkIfPieceClickedOnSide(event, data):
	for i in range(len(data.allOutsidePieces)):
		piece = data.allOutsidePieces[i]
		if event.x > piece.x and event.x < piece.x + (len(piece.profile[0])*data.cellSize):
			if event.y > piece.y and event.y < piece.y + (len(piece.profile)*data.cellSize): 
				return (piece, i)
	return None

def moveSelectedPieceToSide(data):
	data.selectedPiece[0].x = data.oldXCoordOfSelected
	data.selectedPiece[0].y = data.oldYCoordOfSelected

def mousePressed(event, data):
	result = checkIfPieceClickedOnSide(event, data)
	if result != None and data.placedOnBoard == False:
		data.oldXCoordOfSelected = result[0].x
		data.oldYCoordOfSelected = result[0].y
		data.selectedPiece = result

	if data.selectedPiece != None:
		if event.x >= data.sideMargin and event.x <= data.width - data.sideMargin and \
			event.y >= data.topMargin and event.y <= data.height - data.topMargin:
				boardX = event.x - ((event.x - data.sideMargin) % data.cellSize)
				data.selectedPiece[0].x = boardX
				boardY = event.y - ((event.y - data.topMargin) % data.cellSize)
				data.selectedPiece[0].y = boardY
				data.placedOnBoard = True
		elif data.placedOnBoard:
			result = checkIfPieceClickedOnSide(event, data)
			if result != None:
				boardLocX = data.selectedPiece[0].x
				boardLocY = data.selectedPiece[0].y
				moveSelectedPieceToSide(data)
				data.oldXCoordOfSelected = result[0].x
				data.oldYCoordOfSelected = result[0].y
				data.selectedPiece = result
				data.selectedPiece[0].x = boardLocX
				data.selectedPiece[0].y = boardLocY

def isLegalPlay(data, boardRow, boardCol):
	for row in range(len(data.selectedPiece[0].profile)):
		for col in range(len(data.selectedPiece[0].profile[0])):
			if row + boardRow < 0 or row + boardRow >= data.rows:
				return False
			elif col + boardCol < 0 or col + boardCol >= data.cols:
				return False
			elif data.board[row + boardRow][col + boardCol] != 'grey' and data.selectedPiece[0].profile[row][col] == True:
				print("Already a piece here!")
				return False
	return True

def keyPressed(event, data):
	if event.keysym == "r":
		init(data)

	if data.selectedPiece != None:
		if event.keysym == "Left":
			data.selectedPiece[0].rotateLeft()

		if event.keysym == "Right":
			data.selectedPiece[0].rotateRight()

		if event.keysym == "Up":
			data.selectedPiece[0].flipUpDown()

		if event.keysym == "Down":
			data.selectedPiece[0].flipLR()

	if event.keysym == "Return":
		if data.selectedPiece != None:
			if data.placedOnBoard:
				colBoard = (data.selectedPiece[0].x - data.sideMargin) // data.cellSize
				rowBoard = (data.selectedPiece[0].y - data.topMargin) // data.cellSize
				if isLegalPlay(data, rowBoard, colBoard):
					drawPieceOnBoard(data, rowBoard, colBoard)
					data.allOutsidePieces.pop(data.selectedPiece[1])
				else:
					moveSelectedPieceToSide(data)
					data.oldXCoordOfSelected, data.oldXCoordOfSelected = None, None
				data.selectedPiece = None
				data.placedOnBoard = False
			else:
				print("place the piece on the board!")
		else:
			print("No piece to place!")

def drawPieceOnBoard(data, rowBoard, colBoard):
	for row in range(len(data.selectedPiece[0].profile)):
		for col in range(len(data.selectedPiece[0].profile[0])):
			if data.selectedPiece[0].profile[row][col]:
				data.board[rowBoard + row][colBoard + col] = data.selectedPiece[0].color

def redrawAll(canvas, data):
	drawGreyBackground(canvas, data)
	drawBoard(canvas, data)
	drawRemainingPieces(canvas, data)

def run(width=300, height=300):
	def redrawAllWrapper(canvas, data):
		canvas.delete(ALL)
		canvas.create_rectangle(0, 0, data.width, data.height,
								fill='white', width=0)
		redrawAll(canvas, data)
		canvas.update()    

	def mousePressedWrapper(event, canvas, data):
		mousePressed(event, data)
		redrawAllWrapper(canvas, data)

	def keyPressedWrapper(event, canvas, data):
		keyPressed(event, data)
		redrawAllWrapper(canvas, data)

	def timerFiredWrapper(canvas, data):
		timerFired(data)
		redrawAllWrapper(canvas, data)
		# pause, then call timerFired again
		canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
		
	# Set up data and call init
	class Struct(object): pass
	data = Struct()
	data.width = width
	data.height = height
	data.timerDelay = 200 # milliseconds
	root = Tk()
	init(data)
	# create the root and the canvas
	canvas = Canvas(root, width=data.width, height=data.height)
	canvas.pack()
	# set up events
	root.bind("<Button-1>", lambda event:
							mousePressedWrapper(event, canvas, data))
	root.bind("<Key>", lambda event:
							keyPressedWrapper(event, canvas, data))
	timerFiredWrapper(canvas, data)
	# and launch the app
	root.mainloop()  # blocks until window is closed
	("bye!")

playBlokus()
