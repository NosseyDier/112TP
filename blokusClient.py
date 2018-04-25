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

HOST = "128.237.214.127" # put your IP address here if playing on multiple computers
PORT = 50110

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
	data.bluePieces = getBluePieces(data)
	data.yellowPieces = getYellowPieces(data)
	data.redPieces = getRedPieces(data)
	data.greenPieces = getGreenPieces(data)
	data.pieces = [data.bluePieces, data.yellowPieces, data.redPieces, data.greenPieces]
	data.namePositions = [(data.width - data.sideMargin + 5 * data.cellSize, data.topMargin//2),
						  (data.width - data.sideMargin //2, data.topMargin),
						  (data.width - data.sideMargin + 5 * data.cellSize, data.height - data.topMargin//2),
						  (data.sideMargin//2, data.topMargin)]
	data.colors = ["Blue", "Yellow", "Red", "Green"]
	data.otherPlayers = []
	data.me = Player("Ike", data.yellowPieces, "green")
	data.board = make2dList(data.rows, data.cols)
	data.message = "KeyboardInterrupt"
	data.whoseTurn = 0

def getPieceClickedOnSide(event, data):
	for piece in data.me.piecesLeft:
		if event.x > piece.x and event.x < piece.x + (len(piece.profile[0])*data.cellSize):
			col = (event.x - piece.x) // data.cellSize
			if event.y > piece.y and event.y < piece.y + (len(piece.profile)*data.cellSize): 
				row = (event.y - piece.y) // data.cellSize
				if piece.profile[row][col] == True:
					return piece
	return None

def moveSelectedPieceToSide(data):
	data.me.selectedPiece.x = data.me.oldXCoordOfSelected
	data.me.selectedPiece.y = data.me.oldYCoordOfSelected

def mousePressed(event, data):
	if checkIfClickedOnInstructions(event, data):
			data.me.instructionScreen = True
		elif checkIfClickedOnControls(event, data):
			data.me.controlsScreen = True
		elif data.me.instructionScreen == True:
			if checkIfClickedBackButton(event, data):
				data.me.instructionScreen = False
		elif data.me.controlsScreen == True:
			if checkIfClickedBackButton(event, data):
				data.me.controlsScreen = False
	if len(data.otherPlayers) == 3 and data.me.name == getWhoseTurnItIs(data, data.whoseTurn):
		result = getPieceClickedOnSide(event, data)
		if data.me.selectedPiece == None:
			if result != None:
			#and data.me.selectedPiece.placedOnBoard == False:
				data.me.oldXCoordOfSelected = result.x
				data.me.oldYCoordOfSelected = result.y
				data.me.selectedPiece = result

		if data.me.selectedPiece != None:
			if event.x >= data.sideMargin and event.x <= data.width - data.sideMargin and \
				event.y >= data.topMargin and event.y <= data.height - data.topMargin:
					boardX = event.x - ((event.x - data.sideMargin) % data.cellSize)
					data.me.selectedPiece.x = boardX
					boardY = event.y - ((event.y - data.topMargin) % data.cellSize)
					data.me.selectedPiece.y = boardY
					data.me.selectedPiece.placedOnBoard = True
			
			elif data.me.selectedPiece.placedOnBoard:
				if result != None:
					boardLocX = data.me.selectedPiece.x
					boardLocY = data.me.selectedPiece.y
					moveSelectedPieceToSide(data)
					data.me.oldXCoordOfSelected = result.x
					data.me.oldYCoordOfSelected = result.y
					data.me.selectedPiece = result
					data.me.selectedPiece.x = boardLocX
					data.me.selectedPiece.y = boardLocY
			else:
				if result == None:
					moveSelectedPieceToSide(data)
					data.me.selectedPiece = None

def mouseMoved(event, data):
	if len(data.otherPlayers) == 3:
		if data.me.selectedPiece != None:
			data.me.selectedPiece.x = event.x
			data.me.selectedPiece.y = event.y

def isLegalPlay(data, boardRow, boardCol):
	cornerSeen = False
	inBoardCorner = False
	for row in range(len(data.me.selectedPiece.profile)):
		for col in range(len(data.me.selectedPiece.profile[0])):
			if row + boardRow < 0 or row + boardRow >= data.rows:
				data.message = "Off the board!"
				return False
			if col + boardCol < 0 or col + boardCol >= data.cols:
				data.message = "Off the board!"
				return False
			if data.board[row + boardRow][col + boardCol] != 'grey' and data.me.selectedPiece.profile[row][col] == True:
				data.message = "Already a piece here!"
				return False
			if data.me.turn == 0:
				if data.me.selectedPiece.profile[row][col] == True:
					if row + boardRow == 0 and boardCol + col == 0:
						inBoardCorner = True
					if row + boardRow == 0 and boardCol + col == data.cols - 1:
						inBoardCorner = True
					if row + boardRow == data.rows - 1 and boardCol + col == 0:
						inBoardCorner = True
					if row + boardRow == data.rows - 1 and boardCol + col == data.cols - 1:
						inBoardCorner = True
			elif data.me.selectedPiece.profile[row][col] == True:
				if row + boardRow - 1 >= 0:
					if data.board[row + boardRow - 1][col + boardCol] == data.me.selectedPiece.color:
						data.message = "Only at corners!"
						return False
				if row + boardRow <= data.rows - 2:
					if data.board[row + boardRow + 1][col + boardCol] == data.me.selectedPiece.color:
						data.message = "Only at corners!"
						return False
				if col + boardCol - 1 >= 0:
					if data.board[row + boardRow][col + boardCol - 1] == data.me.selectedPiece.color:
						data.message = "Only at corners!"
						return False
				if col + boardCol <= data.cols - 2:
					if data.board[row + boardRow][col + boardCol + 1] == data.me.selectedPiece.color:
						data.message = "Only at corners!"
						return False
				if cornerSeen == False:
					if row + boardRow - 1 >= 0 and col + boardCol <= data.cols - 2:
						if data.board[row + boardRow - 1][col + boardCol + 1] == data.me.electedPiece.color:
							cornerSeen = True
					if row + boardRow <= data.rows - 2 and col + boardCol <= data.cols - 2:
						if data.board[row + boardRow + 1][col + boardCol + 1] == data.me.selectedPiece.color:
							cornerSeen = True
					if col + boardCol - 1 >= 0 and row + boardRow - 1 >= 0:
						if data.board[row + boardRow - 1][col + boardCol - 1] == data.me.selectedPiece.color:
							cornerSeen = True
					if row + boardRow <= data.rows - 2 and col + boardCol - 1 >= 0:
						if data.board[row + boardRow + 1][col + boardCol - 1] == data.me.selectedPiece.color:
							cornerSeen = True
	if data.me.turn == 0 and inBoardCorner == False:
		return False
	if data.me.turn != 0 and cornerSeen == False:
		return False
	return True

def getWhichColor(data, piece):
	setNum = None
	for i in range(len(data.pieces)):
		if piece in data.pieces[i]:
			setNum = i
			break
	return setNum

def getWhichColorPosition(data, setNum, piece):
	colorNum = None
	for i in range(len(data.pieces[setNum])):
		if data.me.selectedPiece == data.pieces[setNum][i]:
			colorNum = i
			break
	return colorNum

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.connect((HOST,PORT))
print("connected to server")

def handleServerMsg(server, serverMsg):
  server.setblocking(1)
  msg = ""
  command = ""
  while True:
    msg += server.recv(10).decode("UTF-8")
    command = msg.split("\n")
    while (len(command) > 1):
      readyMsg = command[0]
      msg = "\n".join(command[1:])
      serverMsg.put(readyMsg)
      command = msg.split("\n")

def timerFired(data):
	while (serverMsg.qsize() > 0):
		msg = serverMsg.get(False)
		#try:
		print("received: ", msg, "\n")
		msg = msg.split()
		command = msg[0]
		if (command == "myIDis"):
			numPlayer = int(msg[1])
			newPID = msg[2]
			color = data.pieces[numPlayer][0].color
			data.me.changeName(newPID)
			data.me.changePieces(data.pieces[numPlayer])
			data.me.color = color
			if numPlayer == 0:
				data.message = "It's " + data.me.name + "'s turn!"

		elif (command == "newPlayer"):
			numPlayer = int(msg[1])
			newPID = msg[2]
			color = data.pieces[numPlayer][0].color
			data.otherPlayers.append(Player(newPID, data.pieces[numPlayer], color))
			if numPlayer == 0:
				data.message = "It's " + newPID + "'s turn!"

		elif (command == "restart"):
			init(data)

		elif (command == "placeAndRemove"):
			data.me.selectedPiece = data.pieces[int(msg[4])][int(msg[5])]
			addMyPieceToOthersBoard(data, int(msg[2]), int(msg[3]), int(msg[4]), int(msg[5]))
			changeOtherPlayersScore(data, msg[1], int(msg[6]))
			name = getWhoseTurnItIs(data, int(msg[7]))
			data.whoseTurn += 1
			data.whoseTurn %= 4
			data.message = "It's " + name + "'s turn!"

		elif (command == "rotate"):
			rotateOthersPiece(data, msg[1], int(msg[2]), int(msg[3]), int(msg[4]))
		#except:
			#print("failed")
		serverMsg.task_done()

def rotateOthersPiece(data, name, rotateNum, setNum, colorNum):
	for player in data.otherPlayers:
		if player.name == name:
			if rotateNum == 1:
				newProfile = player.piecesLeft[colorNum].rotateLeft()
				player.piecesLeft[colorNum].profile = newProfile
				data.pieces[setNum][colorNum].profile = newProfile
			if rotateNum == 2:
				newProfile = player.piecesLeft[colorNum].rotateRight()
				player.piecesLeft[colorNum].profile = newProfile
				data.pieces[setNum][colorNum].profile = newProfile
			if rotateNum == 3:
				newProfile = player.piecesLeft[colorNum].flipUpDown()
				player.piecesLeft[colorNum].profile = newProfile
				data.pieces[setNum][colorNum].profile = newProfile
			if rotateNum == 4:
				newProfile = player.piecesLeft[colorNum].flipLR()
				player.piecesLeft[colorNum].profile = newProfile
				data.pieces[setNum][colorNum].profile = newProfile

def keyPressed(event, data):
	print(data.me.name)
	print(getWhoseTurnItIs(data, data.whoseTurn))
	if len(data.otherPlayers) == 3 and data.me.name == getWhoseTurnItIs(data, data.whoseTurn):
		msg = ""
		if event.keysym == "n":
			init(data)
			msg = "restart"

		if data.me.selectedPiece != None:
			setNum = getWhichColor(data, data.me.selectedPiece)
			colorNum = getWhichColorPosition(data, setNum, data.me.selectedPiece)
			if event.keysym == "Left":
				x = data.me.selectedPiece.rotateLeft()
				msg = "rotate 1 %d %d\n" % (setNum, colorNum)
				#data.me.selectedPiece.profile = newProf
				#data.pieces[setNum][colorNum].profile = newProf

			if event.keysym == "Right":
				x = data.me.selectedPiece.rotateRight()
				msg = "rotate 2 %d %d\n" % (setNum, colorNum)
				#data.me.selectedPiece.profile = newProf
				#data.pieces[setNum][colorNum].profile = newProf

			if event.keysym == "Up":
				x = data.me.selectedPiece.flipUpDown()
				msg = "rotate 3 %d %d\n" % (setNum, colorNum)
				#data.me.selectedPiece.profile = newProf
				#data.pieces[setNum][colorNum].profile = newProf

			if event.keysym == "Down":
				x = data.me.selectedPiece.flipLR()
				msg = "rotate 4 %d %d\n" % (setNum, colorNum)
				#data.me.selectedPiece.profile = newProf
				#data.pieces[setNum][colorNum].profile = newProf

			if event.keysym == "w" and data.me.selectedPiece.placedOnBoard:
				data.me.selectedPiece.y -= data.cellSize
				if data.me.selectedPiece.y < data.topMargin:
					data.me.selectedPiece.y += data.cellSize

			if event.keysym == "s" and data.me.selectedPiece.placedOnBoard:
				data.me.selectedPiece.y += data.cellSize
				if data.me.selectedPiece.y > data.height - data.topMargin:
					data.me.selectedPiece.y -= data.cellSize

			if event.keysym == "a" and data.me.selectedPiece.placedOnBoard:
				data.me.selectedPiece.x -= data.cellSize
				if data.me.selectedPiece.x < data.sideMargin:
					data.me.selectedPiece.x += data.cellSize

			if event.keysym == "d" and data.me.selectedPiece.placedOnBoard:
				data.me.selectedPiece.x += data.cellSize
				if data.me.selectedPiece.x > data.width - data.sideMargin:
					data.me.selectedPiece.x -= data.cellSize		

		if event.keysym == "Return":
			print("hayay")
			if data.me.selectedPiece != None:
				if data.me.selectedPiece.placedOnBoard:
					colBoard = (data.me.selectedPiece.x - data.sideMargin) // data.cellSize
					rowBoard = (data.me.selectedPiece.y - data.topMargin) // data.cellSize
					if isLegalPlay(data, rowBoard, colBoard):
						setNum = getWhichColor(data, data.me.selectedPiece)
						colorNum = getWhichColorPosition(data, setNum, data.me.selectedPiece)
						addMyPieceToMyBoard(data, rowBoard, colBoard)
						data.me.dontDrawPiece(colorNum)
						numBlocks = data.me.selectedPiece.blocks
						data.me.addToScore(numBlocks)
						data.me.turn += 1
						data.me.selectedPiece = None
						data.whoseTurn += 1
						data.whoseTurn %= 4
						name = getWhoseTurnItIs(data, data.whoseTurn)
						data.message = "It's " + name + "'s turn!"
						msg = "placeAndRemove %d %d %d %d %d %d\n" % (rowBoard, colBoard, setNum, colorNum, numBlocks, data.whoseTurn)
					else:
						moveSelectedPieceToSide(data)
						data.oldXCoordOfSelected, data.oldXCoordOfSelected = None, None
					data.me.selectedPiece = None
					data.me.placedOnBoard = False
				else:
					data.message = "Place piece on the board!"
			else:
				data.message  = "No piece to place!"

		if (msg != ""):
			print ("sending: ", msg)
			data.server.send(msg.encode())

def getWhoseTurnItIs(data, whoseTurn):
	color = data.colors[whoseTurn]
	#print(color)
	name = ""
	for player in data.otherPlayers:
		if player.color == color:
			name = player.name
	if data.me.color == color:
		name = data.me.name
	#print(name)
	return name

def addMyPieceToMyBoard(data, rowBoard, colBoard):
	for row in range(len(data.me.selectedPiece.profile)):
		for col in range(len(data.me.selectedPiece.profile[0])):
			if data.me.selectedPiece.profile[row][col]:
				data.board[rowBoard + row][colBoard + col] = data.me.selectedPiece.color

def addMyPieceToOthersBoard(data, rowBoard, colBoard, pieceIndex, colorIndex):
	piece = data.pieces[pieceIndex][colorIndex]
	for row in range(len(piece.profile)):
		for col in range(len(piece.profile[0])):
			if piece.profile[row][col]:
				data.board[rowBoard + row][colBoard + col] = piece.color
	piece.toDraw = False

def changeOtherPlayersScore(data, name, dScore):
	for player in data.otherPlayers:
		if player.name == name:
			player.addToScore(dScore)

def drawGreyBackground(canvas, data):
	topX = data.sideMargin - data.cellSize
	topY = data.topMargin - data.cellSize
	botX = data.width - data.sideMargin + data.cellSize
	botY = data.height - data.topMargin + data.cellSize
	canvas.create_rectangle(topX, topY, botX, botY, fill = 'grey', width = 2)

def checkIfClickedOnInstructions(event, data):
	x1 = data.width - data.sideMargin//3
	y1 = data.height - data.topMargin
	x2 = data.width - data.cellSize
	y2 = y1 + 6 * data.cellSize
	clicked = False
	if event.x >= x1 and event.x <= x2:
		if event.y >= y1 and event.y <= y2:
			clicked = True
	return clicked

def checkIfClickedOnControls(event, data):
	x1 = data.width - data.sideMargin//3
	y1 = data.height - data.topMargin + 7 * data.cellSize
	x2 = data.width - data.cellSize
	y2 = y1 + 6 * data.cellSize
	clicked = False
	if event.x >= x1 and event.x <= x2:
		if event.y >= y1 and event.y <= y2:
			clicked = True
	return clicked

def drawInstructionsButton(canvas, data):
	x1 = data.width - data.sideMargin//3
	y1 = data.height - data.topMargin
	x2 = data.width - data.cellSize
	y2 = y1 + 6 * data.cellSize
	canvas.create_rectangle(x1, y1, x2, y2, fill = "grey")
	canvas.create_text((x1 + x2)//2, (y1 + y2)//2, text = "Instructions", fill = "black")

def drawControlsButton(canvas, data):
	x1 = data.width - data.sideMargin//3
	y1 = data.height - data.topMargin + 7 * data.cellSize
	x2 = data.width - data.cellSize
	y2 = y1 + 6 * data.cellSize
	canvas.create_rectangle(x1, y1, x2, y2, fill = "grey")
	canvas.create_text((x1 + x2)//2, (y1 + y2)//2, text = "Controls", fill = "black")

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

def drawMyPieces(canvas, data):
	for piece in data.me.piecesLeft:
		if piece.toDraw == True:
			for row in range(len(piece.profile)):
				for col in range(len(piece.profile[0])):
					if piece.profile[row][col] == True:
						topX = piece.x + col*data.cellSize
						topY = piece.y + row*data.cellSize
						canvas.create_rectangle(topX, topY, topX + data.cellSize, topY + data.cellSize, fill = piece.color)

def drawOthersPieces(canvas, data):
	for player in data.otherPlayers:
		for piece in player.piecesLeft:
			if piece.toDraw == True:
				for row in range(len(piece.profile)):
					for col in range(len(piece.profile[0])):
						if piece.profile[row][col] == True:
							topX = piece.x + col*data.cellSize
							topY = piece.y + row*data.cellSize
							canvas.create_rectangle(topX, topY, topX + data.cellSize, topY + data.cellSize, fill = piece.color)

def drawMyNameAndScore(canvas, data):
	pieceIndex = data.pieces.index(data.me.piecesLeft)
	posX = data.namePositions[pieceIndex][0]
	posY = data.namePositions[pieceIndex][1]
	canvas.create_text(posX, posY, 
						text = data.me.name + ": " + str(data.me.score), fill = data.colors[pieceIndex],
						font = "Helvetica %d underline" % 26)

def drawOthersNamesAndScores(canvas, data):
	for player in data.otherPlayers:
		pieceIndex = data.pieces.index(player.piecesLeft)
		posX = data.namePositions[pieceIndex][0]
		posY = data.namePositions[pieceIndex][1]
		canvas.create_text(posX, posY, 
						text = player.name + ": " + str(player.score), fill = data.colors[pieceIndex],
						font = "Helvetica %d bold" % 26)

def drawControlsScreen(canvas, data):
	canvas.create_rectangle(0, 0, data.width, data.height,
								fill='black', width=0)
	canvas.create_text(100, 100, text = "controls ayy", fill = "white")
	x1 = data.width//2 - data.sideMargin//6
	y1 = data.height - 6 * data.cellSize
	x2 = data.width//2 + data.sideMargin//6
	y2 = data.height - data.cellSize
	canvas.create_rectangle(x1, y1, x2, y2, fill = "grey")
	canvas.create_text((x1 + x2)//2, (y1 + y2)//2, text = "Back", fill = "black")

def drawMessageBox(canvas, data):
	x1 = 5 + data.cellSize
	y1 = 5 + data.cellSize
	x2 = x1 + 20 * data.cellSize
	y2 = y1 + 5 * data.cellSize
	canvas.create_rectangle(x1, y1, x2, y2, fill = "grey")
	canvas.create_text((x1 + x2)//2, (y1 + y2)//2, text = data.message, fill = "black", font = "Helvetica %d bold" % 26)

def drawInstructionsScreen(canvas, data):
	canvas.create_rectangle(0, 0, data.width, data.height,
								fill='black', width=0)
	canvas.create_text(100, 100, text = "instructions ayy", fill = "white")
	x1 = data.width//2 - data.sideMargin//6
	y1 = data.height - 6 * data.cellSize
	x2 = data.width//2 + data.sideMargin//6
	y2 = data.height - data.cellSize
	canvas.create_rectangle(x1, y1, x2, y2, fill = "grey")
	canvas.create_text((x1 + x2)//2, (y1 + y2)//2, text = "Back", fill = "black")

def checkIfClickedBackButton(event, data):
	x1 = data.width//2 - data.sideMargin//6
	y1 = data.height - 6 * data.cellSize
	x2 = data.width//2 + data.sideMargin//6
	y2 = data.height - data.cellSize
	clicked = False
	if event.x >= x1 and event.x <= x2:
		if event.y >= y1 and event.y <= y2:
			clicked = True
	return clicked

def redrawAll(canvas, data):
	if len(data.otherPlayers) == 3:
		if data.me.instructionScreen == True:
			drawInstructionsScreen(canvas, data)
		elif data.me.controlsScreen == True:
			drawControlsScreen(canvas, data)
		else:
			drawGreyBackground(canvas, data)
			drawBoard(canvas, data)
			drawMyNameAndScore(canvas, data)
			drawInstructionsButton(canvas, data)
			drawControlsButton(canvas, data)
			drawOthersNamesAndScores(canvas, data)
			drawMessageBox(canvas, data)
			drawMyPieces(canvas, data)
			drawOthersPieces(canvas, data)

# Run function courtesy of 15-112 animations section and Kyle Chin and Rohan Varma's server code
def run(width, height, serverMsg=None, server=None):
	def redrawAllWrapper(canvas, data):
		canvas.delete(ALL)
		canvas.create_rectangle(0, 0, data.width, data.height,
								fill='black', width=0)
		canvas.create_text(data.width/2, data.height/2, text = "Waiting for other players...", fill = "White", font = "Helvetica %d bold" % 26)
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
	data.server = server
	data.serverMsg = serverMsg
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

serverMsg = Queue(100)
threading.Thread(target = handleServerMsg, args = (server, serverMsg)).start()

run((2 * 360) + (20 * 15), (2 * 250) + (20 * 15), serverMsg, server)
