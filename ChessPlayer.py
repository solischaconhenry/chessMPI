class ChessPlayer:

    def __init__(self,name,color):
        self.name = name
        self.color = color
        self.piecesWon = []

    def GetName(self):
        return self.name

    def GetColor(self):
        return self.color

    def GetPiecesWon(self):
        return self.piecesWon

   # def AddPiecesWon(piece):

