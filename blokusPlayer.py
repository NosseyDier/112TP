class Player(object):
    def __init__(self, name, piecesLeft, color):
        self.name = name
        self.score = 0
        self.turn = 0
        self.piecesLeft = piecesLeft
        self.color = color
        self.wins = False
        self.loses = False

        self.selectedPiece = None
        self.oldXCoordOfSelected = None
        self.oldYCoordOfSelected = None
        self.instructionScreen = False
        self.controlsScreen = False

    def __repr__(self):
        piece = self.piecesLeft[3]
        return self.name + piece.color

    def addToScore(self, dScore):
        self.score += dScore

    def dontDrawPiece(self, index):
        piece = self.piecesLeft[index]
        piece.toDraw = False

    def changeName(self, newName):
        self.name = newName

    def changePieces(self, newPieces):
        self.piecesLeft = newPieces