import math
import string
import copy
import random
from tkinter import *
from piece import Piece
from blokusPlayer import Player

# From Kyle Chin's presentation on sockets
import socket
import threading
from queue import Queue

HOST = "128.237.120.85" # put your IP address here if playing on multiple computers
PORT = 50007

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

def getBluePieces(data):
	top = 5
	mid = top+ 4*data.cellSize
	bot = mid + 4*data.cellSize
	bluePieces = []
	bluePieces.append(Piece(tPc, 5, (data.sideMargin, top), "Blue"))
	bluePieces.append(Piece(twoThreePc, 5, (data.sideMargin+4*data.cellSize, top), "Blue"))
	bluePieces.append(Piece(stepPc, 5,  (data.sideMargin + 7*data.cellSize, top), "Blue"))
	bluePieces.append(Piece(zPc, 5, (data.sideMargin+11*data.cellSize, top), "Blue"))
	bluePieces.append(Piece(cPc, 5, (data.sideMargin + 15*data.cellSize, top), "Blue"))
	bluePieces.append(Piece(bPc, 5, (data.sideMargin+18*data.cellSize,top), "Blue"))
	bluePieces.append(Piece(plusPc, 5, (data.sideMargin, mid), "Blue"))
	bluePieces.append(Piece(bigLPc, 5, (data.sideMargin+4*data.cellSize, mid), "Blue"))
	bluePieces.append(Piece(twoPc, 2, (data.sideMargin + 8*data.cellSize, mid+data.cellSize), "Blue"))
	bluePieces.append(Piece(fiveLongPc, 5, (data.sideMargin + 10*data.cellSize, mid-data.cellSize), "Blue"))
	bluePieces.append(Piece(onePc, 1, (data.sideMargin + 12*data.cellSize, mid+ 2 *data.cellSize), "Blue"))
	bluePieces.append(Piece(weirdPc, 5, (data.sideMargin + 13*data.cellSize, mid), "Blue"))
	bluePieces.append(Piece(oneFivePc, 5, (data.sideMargin + 17*data.cellSize, mid), "Blue"))
	bluePieces.append(Piece(tallLPc, 5, (data.sideMargin, bot), "Blue"))
	bluePieces.append(Piece(fourLPc, 4, (data.sideMargin+2*data.cellSize, bot), "Blue"))
	bluePieces.append(Piece(sPc, 4, (data.sideMargin+5*data.cellSize, bot), "Blue"))
	bluePieces.append(Piece(fourTallPc, 4, (data.sideMargin+8*data.cellSize, bot), "Blue"))
	bluePieces.append(Piece(squarePc, 4, (data.sideMargin+10*data.cellSize, bot + data.cellSize), "Blue"))
	bluePieces.append(Piece(fourTPc, 4, (data.sideMargin+13*data.cellSize, bot), "Blue"))
	bluePieces.append(Piece(threeTallPc, 3, (data.sideMargin+16*data.cellSize, bot), "Blue"))
	bluePieces.append(Piece(threeLPc, 3, (data.sideMargin+18*data.cellSize, bot + data.cellSize), "Blue"))
	return bluePieces

def getRedPieces(data):
	top = data.height - data.topMargin + (3 * data.cellSize)
	mid = top+ 4*data.cellSize
	bot = mid + 4*data.cellSize
	redPieces = []
	redPieces.append(Piece(tPc, 5, (data.sideMargin, top), "Red"))
	redPieces.append(Piece(twoThreePc, 5, (data.sideMargin+4*data.cellSize, top), "Red"))
	redPieces.append(Piece(stepPc, 5, (data.sideMargin + 7*data.cellSize, top), "Red"))
	redPieces.append(Piece(zPc, 5, (data.sideMargin+11*data.cellSize, top), "Red"))
	redPieces.append(Piece(cPc, 5, (data.sideMargin + 15*data.cellSize, top), "Red"))
	redPieces.append(Piece(bPc, 5, (data.sideMargin+18*data.cellSize,top), "Red"))
	redPieces.append(Piece(plusPc, 5,(data.sideMargin, mid), "Red"))
	redPieces.append(Piece(bigLPc, 5, (data.sideMargin+4*data.cellSize, mid), "Red"))
	redPieces.append(Piece(twoPc, 2, (data.sideMargin + 8*data.cellSize, mid+data.cellSize), "Red"))
	redPieces.append(Piece(fiveLongPc, 5, (data.sideMargin + 10*data.cellSize, mid-data.cellSize), "Red"))
	redPieces.append(Piece(onePc, 1, (data.sideMargin + 12*data.cellSize, mid+ 2 *data.cellSize), "Red"))
	redPieces.append(Piece(weirdPc, 5, (data.sideMargin + 13*data.cellSize, mid), "Red"))
	redPieces.append(Piece(oneFivePc, 5,(data.sideMargin + 17*data.cellSize, mid), "Red"))
	redPieces.append(Piece(tallLPc, 5, (data.sideMargin, bot), "Red"))
	redPieces.append(Piece(fourLPc, 4, (data.sideMargin+2*data.cellSize, bot), "Red"))
	redPieces.append(Piece(sPc, 4, (data.sideMargin+5*data.cellSize, bot), "Red"))
	redPieces.append(Piece(fourTallPc, 4, (data.sideMargin+8*data.cellSize, bot), "Red"))
	redPieces.append(Piece(squarePc, 4, (data.sideMargin+10*data.cellSize, bot + data.cellSize), "Red"))
	redPieces.append(Piece(fourTPc, 4, (data.sideMargin+13*data.cellSize, bot), "Red"))
	redPieces.append(Piece(threeTallPc, 3, (data.sideMargin+16*data.cellSize, bot), "Red"))
	redPieces.append(Piece(threeLPc, 3, (data.sideMargin+18*data.cellSize, bot + data.cellSize), "Red"))
	return redPieces

def getGreenPieces(data):
	top = data.topMargin + 5 * data.cellSize
	mid = top+ 4*data.cellSize
	bot = mid + 4*data.cellSize
	greenPieces = []
	greenPieces.append(Piece(tPc, 5, (5, top), "Green"))
	greenPieces.append(Piece(twoThreePc, 5, (5+4*data.cellSize, top), "Green"))
	greenPieces.append(Piece(stepPc, 5, (5 + 7*data.cellSize, top), "Green"))
	greenPieces.append(Piece(zPc, 5, (5+11*data.cellSize, top), "Green"))
	greenPieces.append(Piece(cPc, 5, (5 + 15*data.cellSize, top), "Green"))
	greenPieces.append(Piece(bPc, 5, (5+18*data.cellSize,top), "Green"))
	greenPieces.append(Piece(plusPc, 5,(5, mid), "Green"))
	greenPieces.append(Piece(bigLPc, 5, (5+4*data.cellSize, mid), "Green"))
	greenPieces.append(Piece(twoPc, 2, (5 + 8*data.cellSize, mid+data.cellSize), "Green"))
	greenPieces.append(Piece(fiveLongPc, 5, (5 + 10*data.cellSize, mid-data.cellSize), "Green"))
	greenPieces.append(Piece(onePc, 1, (5 + 12*data.cellSize, mid+ 2 *data.cellSize), "Green"))
	greenPieces.append(Piece(weirdPc, 5, (5 + 13*data.cellSize, mid), "Green"))
	greenPieces.append(Piece(oneFivePc, 5,(5 + 17*data.cellSize, mid), "Green"))
	greenPieces.append(Piece(tallLPc, 5, (5, bot), "Green"))
	greenPieces.append(Piece(fourLPc, 4, (5+2*data.cellSize, bot), "Green"))
	greenPieces.append(Piece(sPc, 4, (5+5*data.cellSize, bot), "Green"))
	greenPieces.append(Piece(fourTallPc, 4, (5+8*data.cellSize, bot), "Green"))
	greenPieces.append(Piece(squarePc, 4, (5+10*data.cellSize, bot + data.cellSize), "Green"))
	greenPieces.append(Piece(fourTPc, 4, (5+13*data.cellSize, bot), "Green"))
	greenPieces.append(Piece(threeTallPc, 3, (5+16*data.cellSize, bot), "Green"))
	greenPieces.append(Piece(threeLPc, 3, (5+18*data.cellSize, bot + data.cellSize), "Green"))
	return greenPieces

def getYellowPieces(data):
	top = data.topMargin + 5 * data.cellSize
	mid = top+ 4*data.cellSize
	bot = mid + 4*data.cellSize
	side = data.width - data.sideMargin + 3 * data.cellSize
	yellowPieces = []
	yellowPieces.append(Piece(tPc, 5, (side, top), "Yellow"))
	yellowPieces.append(Piece(twoThreePc, 5, (side+4*data.cellSize, top), "Yellow"))
	yellowPieces.append(Piece(stepPc, 5, (side + 7*data.cellSize, top), "Yellow"))
	yellowPieces.append(Piece(zPc, 5, (side+11*data.cellSize, top), "Yellow"))
	yellowPieces.append(Piece(cPc, 5, (side + 15*data.cellSize, top), "Yellow"))
	yellowPieces.append(Piece(bPc, 5, (side+18*data.cellSize,top), "Yellow"))
	yellowPieces.append(Piece(plusPc, 5,(side, mid), "Yellow"))
	yellowPieces.append(Piece(bigLPc, 5, (side+4*data.cellSize, mid), "Yellow"))
	yellowPieces.append(Piece(twoPc, 2, (side + 8*data.cellSize, mid+data.cellSize), "Yellow"))
	yellowPieces.append(Piece(fiveLongPc, 5, (side + 10*data.cellSize, mid-data.cellSize), "Yellow"))
	yellowPieces.append(Piece(onePc, 1, (side + 12*data.cellSize, mid+ 2 *data.cellSize), "Yellow"))
	yellowPieces.append(Piece(weirdPc, 5, (side + 13*data.cellSize, mid), "Yellow"))
	yellowPieces.append(Piece(oneFivePc, 5,(side + 17*data.cellSize, mid), "Yellow"))
	yellowPieces.append(Piece(tallLPc, 5, (side, bot), "Yellow"))
	yellowPieces.append(Piece(fourLPc, 4, (side+2*data.cellSize, bot), "Yellow"))
	yellowPieces.append(Piece(sPc, 4, (side+5*data.cellSize, bot), "Yellow"))
	yellowPieces.append(Piece(fourTallPc, 4, (side+8*data.cellSize, bot), "Yellow"))
	yellowPieces.append(Piece(squarePc, 4, (side+10*data.cellSize, bot + data.cellSize), "Yellow"))
	yellowPieces.append(Piece(fourTPc, 4, (side+13*data.cellSize, bot), "Yellow"))
	yellowPieces.append(Piece(threeTallPc, 3, (side+16*data.cellSize, bot), "Yellow"))
	yellowPieces.append(Piece(threeLPc, 3, (side+18*data.cellSize, bot + data.cellSize), "Yellow"))
	return yellowPieces

def init(data):
	data.cellSize = 15
	data.rows = 20
	data.cols = 20
	data.topMargin = 250
	data.sideMargin = 360
	bluePieces = getBluePieces(data)
	yellowPieces = getYellowPieces(data)
	redPieces = getRedPieces(data)
	greenPieces = getGreenPieces(data)
	data.player1 = Player("Reid", bluePieces)
	data.player2 = Player("Abhi", yellowPieces)
	data.player3 = Player("Nico", redPieces)
	data.player4 = Player("Seb", greenPieces)
	data.players = [data.player1, data.player2, data.player3, data.player4]

	data.currentPlayer = 0
	data.board = make2dList(data.rows, data.cols)
	data.selectedPiece = None
	data.oldXCoordOfSelected = None
	data.oldYCoordOfSelected = None
	data.placedOnBoard = False

def playBlokus(rows = 20, cols = 20):
	cellSize = 15
	topMargin = 250
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

def drawOutsidePieces(canvas, data):
	for player in data.players:
		for piece in player.piecesLeft:
			for row in range(len(piece.profile)):
				for col in range(len(piece.profile[0])):
					if piece.profile[row][col] == True:
						topX = piece.x + col*data.cellSize
						topY = piece.y + row*data.cellSize
						canvas.create_rectangle(topX, topY, topX + data.cellSize, topY + data.cellSize, fill = piece.color)

def timerFired(data):
    while (serverMsg.qsize() > 0):
      msg = serverMsg.get(False)
      try:
        print("received: ", msg, "\n")
        msg = msg.split()
        command = msg[0]

        if (command == "myIDis"):
          myPID = msg[1]
          data.me.changePID(myPID)

        elif (command == "newPlayer"):
          newPID = msg[1]
          x = data.width/2
          y = data.height/2
          data.otherStrangers[newPID] = Dot(newPID, x, y)

        elif (command == "playerMoved"):
          PID = msg[1]
          dx = int(msg[2])
          dy = int(msg[3])
          data.otherStrangers[PID].move(dx, dy)

        elif (command == "playerTeleported"):
          PID = msg[1]
          x = int(msg[2])
          y = int(msg[3])
          data.otherStrangers[PID].teleport(x, y)
      except:
        print("failed")
      serverMsg.task_done()

def checkIfPieceClickedOnSide(event, data):
	for i in range(len(data.players[data.currentPlayer].piecesLeft)):
		piece = data.players[data.currentPlayer].piecesLeft[i]
		if event.x > piece.x and event.x < piece.x + (len(piece.profile[0])*data.cellSize):
			col = (event.x - piece.x) // data.cellSize
			if event.y > piece.y and event.y < piece.y + (len(piece.profile)*data.cellSize): 
				row = (event.y - piece.y) // data.cellSize
				if piece.profile[row][col] == True:
					return (piece, i)
	return None

def moveSelectedPieceToSide(data):
	data.selectedPiece[0].x = data.oldXCoordOfSelected
	data.selectedPiece[0].y = data.oldYCoordOfSelected

def mousePressed(event, data):
	result = checkIfPieceClickedOnSide(event, data)
	if data.selectedPiece == None:
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
			if result != None:
				boardLocX = data.selectedPiece[0].x
				boardLocY = data.selectedPiece[0].y
				moveSelectedPieceToSide(data)
				data.oldXCoordOfSelected = result[0].x
				data.oldYCoordOfSelected = result[0].y
				data.selectedPiece = result
				data.selectedPiece[0].x = boardLocX
				data.selectedPiece[0].y = boardLocY
		else:
			if result == None:
				moveSelectedPieceToSide(data)
				data.selectedPiece = None

def mouseMoved(event, data):
	if data.selectedPiece != None:
		data.selectedPiece[0].x = event.x
		data.selectedPiece[0].y = event.y

def isLegalPlay(data, boardRow, boardCol):
	cornerSeen = False
	inBoardCorner = False
	for row in range(len(data.selectedPiece[0].profile)):
		for col in range(len(data.selectedPiece[0].profile[0])):
			if row + boardRow < 0 or row + boardRow >= data.rows:
				print("Off the board!")
				return False
			if col + boardCol < 0 or col + boardCol >= data.cols:
				print("Off the board!")
				return False
			if data.board[row + boardRow][col + boardCol] != 'grey' and data.selectedPiece[0].profile[row][col] == True:
				print("Already a piece here!")
				return False
			if data.players[data.currentPlayer].turn == 0:
				if data.selectedPiece[0].profile[row][col] == True:
					if row + boardRow == 0 and boardCol + col == 0:
						inBoardCorner = True
					if row + boardRow == 0 and boardCol + col == data.cols - 1:
						inBoardCorner = True
					if row + boardRow == data.rows - 1 and boardCol + col == 0:
						inBoardCorner = True
					if row + boardRow == data.rows - 1 and boardCol + col == data.cols - 1:
						inBoardCorner = True
			elif data.selectedPiece[0].profile[row][col] == True:
				if row + boardRow - 1 >= 0:
					if data.board[row + boardRow - 1][col + boardCol] == data.selectedPiece[0].color:
						print("only at corners!")
						return False
				if row + boardRow <= data.rows - 2:
					if data.board[row + boardRow + 1][col + boardCol] == data.selectedPiece[0].color:
						print("only at corners!")
						return False
				if col + boardCol - 1 >= 0:
					if data.board[row + boardRow][col + boardCol - 1] == data.selectedPiece[0].color:
						print("only at corners!")
						return False
				if col + boardCol <= data.cols - 2:
					if data.board[row + boardRow][col + boardCol + 1] == data.selectedPiece[0].color:
						print("only at corners!")
						return False
				if cornerSeen == False:
					if row + boardRow - 1 >= 0 and col + boardCol <= data.cols - 2:
						if data.board[row + boardRow - 1][col + boardCol + 1] == data.selectedPiece[0].color:
							cornerSeen = True
					if row + boardRow <= data.rows - 2 and col + boardCol <= data.cols - 2:
						if data.board[row + boardRow + 1][col + boardCol + 1] == data.selectedPiece[0].color:
							cornerSeen = True
					if col + boardCol - 1 >= 0 and row + boardRow - 1 >= 0:
						if data.board[row + boardRow - 1][col + boardCol - 1] == data.selectedPiece[0].color:
							cornerSeen = True
					if row + boardRow <= data.rows - 2 and col + boardCol - 1 >= 0:
						if data.board[row + boardRow + 1][col + boardCol - 1] == data.selectedPiece[0].color:
							cornerSeen = True
	if data.players[data.currentPlayer].turn == 0 and inBoardCorner == False:
		return False
	if data.players[data.currentPlayer].turn != 0 and cornerSeen == False:
		return False
	return True

def keyPressed(event, data):
	if event.keysym == "n":
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

		if event.keysym == "w" and data.placedOnBoard:
			data.selectedPiece[0].y -= data.cellSize
			if data.selectedPiece[0].y < data.topMargin:
				data.selectedPiece[0].y += data.cellSize

		if event.keysym == "s" and data.placedOnBoard:
			data.selectedPiece[0].y += data.cellSize
			if data.selectedPiece[0].y > data.height - data.topMargin:
				data.selectedPiece[0].y -= data.cellSize

		if event.keysym == "a" and data.placedOnBoard:
			data.selectedPiece[0].x -= data.cellSize
			if data.selectedPiece[0].x < data.sideMargin:
				data.selectedPiece[0].x += data.cellSize

		if event.keysym == "d" and data.placedOnBoard:
			data.selectedPiece[0].x += data.cellSize
			if data.selectedPiece[0].x > data.width - data.sideMargin:
				data.selectedPiece[0].x -= data.cellSize		

	if event.keysym == "Return":
		if data.selectedPiece != None:
			if data.placedOnBoard:
				colBoard = (data.selectedPiece[0].x - data.sideMargin) // data.cellSize
				rowBoard = (data.selectedPiece[0].y - data.topMargin) // data.cellSize
				if isLegalPlay(data, rowBoard, colBoard):
					drawPieceOnBoard(data, rowBoard, colBoard)
					data.players[data.currentPlayer].removePiece(data.selectedPiece[1])
					data.players[data.currentPlayer].addToScore(data.selectedPiece[0].blocks)
					data.players[data.currentPlayer].turn += 1
					data.currentPlayer += 1
					data.currentPlayer %= 4
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

def drawNamesAndScores(canvas, data):
	canvas.create_text(data.width - data.sideMargin + data.cellSize, data.topMargin//2, 
						text = data.players[0].name + ": " + str(data.players[0].score), anchor=W, fill = "blue",
						font = "Helvetica %d bold" % 26)
	canvas.create_text(data.width - data.sideMargin //2, data.topMargin, 
						text = data.players[1].name + ": " + str(data.players[1].score), fill = "yellow",
						font = "Helvetica %d bold" % 26)
	canvas.create_text(data.width - data.sideMargin + data.cellSize, data.height - data.topMargin//2, 
						text = data.players[2].name + ": " + str(data.players[2].score), anchor=W, fill = "red",
						font = "Helvetica %d bold" % 26)
	canvas.create_text(data.sideMargin//2, data.topMargin, 
						text = data.players[3].name + ": " + str(data.players[3].score), fill = "green",
						font = "Helvetica %d bold" % 26)

def helpScreen():
	print("ha gay")

def redrawAll(canvas, data):
	drawGreyBackground(canvas, data)
	drawBoard(canvas, data)
	drawNamesAndScores(canvas, data)
	drawOutsidePieces(canvas, data)

def run(width=300, height=300):
	def redrawAllWrapper(canvas, data):
		canvas.delete(ALL)
		canvas.create_rectangle(0, 0, data.width, data.height,
								fill='black', width=0)
		redrawAll(canvas, data)
		canvas.update()    

	def mousePressedWrapper(event, canvas, data):
		mousePressed(event, data)
		redrawAllWrapper(canvas, data)

	def keyPressedWrapper(event, canvas, data):
		keyPressed(event, data)
		redrawAllWrapper(canvas, data)

	def mouseMovedWrapper(event, canvas, data):
		mouseMoved(event, data)
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
	root.title("Blokus")
	init(data)
	# create the root and the canvas
	canvas = Canvas(root, width=data.width, height=data.height)
	canvas.pack()
	# set up events
	root.bind("<Motion>", lambda event:
							mouseMovedWrapper(event, canvas,data))
	root.bind("<Button-1>", lambda event:
							mousePressedWrapper(event, canvas, data))
	root.bind("<Key>", lambda event:
							keyPressedWrapper(event, canvas, data))
	timerFiredWrapper(canvas, data)
	# and launch the app
	root.mainloop()  # blocks until window is closed
	("bye!")

playBlokus()
