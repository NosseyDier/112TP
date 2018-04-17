def make2dList(rows, cols):
    a=[]
    for row in range(rows): a += [[0]*cols]
    return a

class Board(object):
	def __init__(self, boardSize):
		board = made2dList(boardSize, boardSize)