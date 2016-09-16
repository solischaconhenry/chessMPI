from ChessTable import ChessTable
from ChessPlayer import ChessPlayer
from ChessAI import ChessAI

class mainChess:
    def __init__(self):
        self.mainTable = ChessTable()
        self.AI = ChessAI()
        self.name1 = raw_input("ENTER NAME OF PLAYER ONE(WHITE):")
        self.name2 = raw_input("ENTER NAME OF PLAYER TWO(BLACK):")
        self.player1 = ChessPlayer(self.name1,"w")
        self.player2 = ChessPlayer(self.name2,"b")
        self.actualPlayer = self.player1 #arreglar color


    def play(self):
        ori = "Current position of the workpiece:"
        des = "Required piece position:"
        choose = "Choose the piece"
        while True:
            if self.actualPlayer.color == "w":
                print( "YOUR TURN PLAYER 1 (WHITE): " + self.actualPlayer.GetName())
            else:
                print ("YOUR TURN PLAYER 2 (BLACK): " + self.actualPlayer.GetName())

            getOri = raw_input(ori)

            if getOri == "all moves":
               getOri = raw_input(ori)

            elif getOri == "one move":
                getOri = raw_input(choose)
                self.mainTable.GetMovesChooser(getOri, self.actualPlayer)
                getOri = raw_input(ori)
            elif getOri == "points":
                getOri = raw_input(choose)
                toTupleInt = [8 - int(getOri[1]), int(self.mainTable.getNumberPos(getOri[0]))]
                print (self.AI.EvaluatePiece(toTupleInt, self.mainTable.squares,self.actualPlayer, getOri))
                #print self.AI.EvaluateMove(self.mainTable.squares,self.actualPlayer,toTupleInt,"P")
                #getOri = raw_input(choose)




            getDes = raw_input(des)



            move = self.mainTable.SetPositionTable(getOri,getDes,self.actualPlayer)
            main.mainTable.PrintChessTable()

            if move == True:
                if self.actualPlayer == self.player2:
                    self.actualPlayer = self.player1
                else:
                    self.actualPlayer = self.player2
            else:
                print ("Movimiento invalido")



print ("HI")

main = mainChess()
main.mainTable.PrintChessTable()
main.play()

