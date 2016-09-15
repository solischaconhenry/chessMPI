from ChessBishop import Bishop
from ChessHourse import Hourse
from ChessKing import king
from ChessQueen import queen
from ChessRook import rook

class ChessAI:
    def __init__(self):
        self.CBishop = Bishop()
        self.CQueen = queen()
        self.CHourse = Hourse()
        self.CKing = king()
        self.CRook = rook()

    #def EvaluationMin()

    #def EvaluationMax()

    '''
    def GetPoints(self,piece):
        if piece == "P":
            return 1

        elif piece == "H":
            return 3

        elif piece == "B":
            return 3

        elif piece == "R":
            return 5

        elif piece == "Q":
            return 9

        else:
            return 11

    def NumInRange(self, num1, num2):
        if num1 >= 0 and num1 <= 7 and num2 >= 0 and num2 <= 7:
            return True
        else:
            return False

    def EvaluateMove(self,table,actualPlayer,toTupleInt,piece):
        colorC = ""
        take = False
        if actualPlayer.color == "w":
            colorC = "b"
        elif actualPlayer.color == "b":
            colorC = "w"

        r = toTupleInt[0]
        c = toTupleInt[1]

        points = 0

        if table[r][c] != "e":

            if table[r][c][1] == "P":
                points = points + 1

            elif table[r][c][1] == "H":
                points = points + 3


            elif table[r][c][1] == "B":
                points = points + 3


            elif table[r][c][1] == "R":
                points = points + 6


            elif table[r][c][1] == "Q":
                points = points + 9

            else:
                points = points + 11



        #CABALLO

        if self.NumInRange(toTupleInt[0] + 2,toTupleInt[1] - 1) and table[toTupleInt[0] + 2][toTupleInt[1] - 1]!= "e" :
            if  table[toTupleInt[0] + 2][toTupleInt[1] - 1][0] == colorC and table[toTupleInt[0] + 2][toTupleInt[1] - 1][1] == "H":
                points = points - self.GetPoints(piece)
                take = True

        if self.NumInRange(toTupleInt[0] + 2, toTupleInt[1] + 1)and table[toTupleInt[0] + 2][toTupleInt[1] - 1]!= "e" :
            if  table[toTupleInt[0] + 2][toTupleInt[1] + 1][0] == colorC and table[toTupleInt[0] + 2][toTupleInt[1] - 1][1] == "H":

                points = points - self.GetPoints(piece)
                take = True

        if self.NumInRange(toTupleInt[0] + 1, toTupleInt[1] - 2)and table[toTupleInt[0] + 2][toTupleInt[1] - 1]!= "e" :
            if table[toTupleInt[0] + 1][toTupleInt[1] - 2][0] == colorC and table[toTupleInt[0] + 2][toTupleInt[1] - 1][1] == "H":

                points = points - self.GetPoints(piece)
                take = True

        if self.NumInRange(toTupleInt[0] + 1, toTupleInt[1] + 2)and table[toTupleInt[0] + 2][toTupleInt[1] - 1]!= "e" :
            if  table[toTupleInt[0] + 1][toTupleInt[1] + 2][0] == colorC and table[toTupleInt[0] + 2][toTupleInt[1] - 1][1] == "H":

                points = points - self.GetPoints(piece)
                take = True

        if self.NumInRange(toTupleInt[0] - 1, toTupleInt[1] + 2) and table[toTupleInt[0] + 2][toTupleInt[1] - 1]!= "e" :
            if  table[toTupleInt[0] - 1][toTupleInt[1] + 2][0] == colorC and table[toTupleInt[0] + 2][toTupleInt[1] - 1][1] == "H":

                points = points - self.GetPoints(piece)
                take = True

        if self.NumInRange(toTupleInt[0] - 1, toTupleInt[1] - 2)and table[toTupleInt[0] + 2][toTupleInt[1] - 1]!= "e" :
            if table[toTupleInt[0] - 1][toTupleInt[1] - 2][0] == colorC and table[toTupleInt[0] + 2][toTupleInt[1] - 1][1] == "H":

                points = points - self.GetPoints(piece)
                take = True

        if self.NumInRange(toTupleInt[0] - 2, toTupleInt[1] - 1)and table[toTupleInt[0] + 2][toTupleInt[1] - 1]!= "e" :
            if table[toTupleInt[0] - 2][toTupleInt[1] - 1][0] == colorC and table[toTupleInt[0] + 2][toTupleInt[1] - 1][1] == "H":

                points = points - self.GetPoints(piece)
                take = True

        if self.NumInRange(toTupleInt[0] - 2, toTupleInt[1] + 1)and table[toTupleInt[0] + 2][toTupleInt[1] - 1]!= "e" :
            if table[toTupleInt[0] - 2][toTupleInt[1] + 1] == colorC and table[toTupleInt[0] + 2][toTupleInt[1] - 1][1] == "H":

                points = points - self.GetPoints(piece)
                take = True




        # Adelante derecha
        r = toTupleInt[0] + 1
        c = toTupleInt[1] + 1

        if self.NumInRange(r,c)  == True and table[r][c] != "e":
            if (table[r][c][1] == "K" and table[r][c][0] == colorC ) or (table[r][c][1] == "P" and colorC == "w"):
                points =  points - self.GetPoints(piece)
                take = True

        while r < 8 and c < 8:
            if table[r][c] == "e":
                r += 1
                c += 1

            elif  table[r][c][0] == colorC:
                if table[r][c][1] == "B":
                    points = points - self.GetPoints(piece)
                    take = True
                    break

                elif table[r][c][1] == "Q":
                    points = - 9
                    take = True
                    break
                else:
                    break
            else:

                break




        if take == False:
            # Atras izquierda
            r = toTupleInt[0] - 1
            c = toTupleInt[1] - 1

            if self.NumInRange(r, c) == True and table[r][c] != "e":
                if (table[r][c][1] == "K" and table[r][c][0] == colorC) or (table[r][c][1] == "P" and colorC == "b"):
                    points = points - self.GetPoints(piece)
                    take = True


            while r >= 0 and c >= 0:
                if table[r][c] == "e":
                    r -= 1
                    c -= 1

                elif table[r][c][0] == colorC:
                    if table[r][c][1] == "B":
                        points = points - self.GetPoints(piece)
                        take = True
                        break

                    elif table[r][c][1] == "Q":
                        points = - self.GetPoints(piece)
                        take = True
                        break
                    else:
                        break
                else:

                    break

        if take == False:
            # Atras derecha
            r = toTupleInt[0] - 1
            c = toTupleInt[1] + 1

            if self.NumInRange(r, c) == True and table[r][c]!= "e":

                if (table[r][c][1] == "K" and table[r][c][0] == colorC) or  (table[r][c][1] == "P" and colorC == "b"):
                    points = points - self.GetPoints(piece)
                    take = True

            while r >= 0 and c < 8:
                if table[r][c] == "e":
                    r -= 1
                    c += 1

                elif table[r][c][0] == colorC:
                    if table[r][c][1] == "B":
                        points = points - self.GetPoints(piece)
                        take = True
                        break

                    elif table[r][c][1] == "Q":
                        points = - self.GetPoints(piece)
                        take = True
                        break
                    else:
                        break
                else:

                    break

        if take == False:
            # Adelante izquierda
            r = toTupleInt[0] + 1
            c = toTupleInt[1] - 1

            if self.NumInRange(r, c) == True and table[r][c]!= "e":

                if (table[r][c][1] == "K" and table[r][c][0] == colorC) or (table[r][c][1] == "P" and colorC == "w"):
                    points = points - self.GetPoints(piece)
                    take = True

            while r < 8 and c >= 0:
                if table[r][c] == "e":
                    r += 1
                    c -= 1

                elif table[r][c][0] == colorC:
                    if table[r][c][1] == "B":
                        points = points - self.GetPoints(piece)
                        take = True
                        break

                    elif table[r][c][1] == "Q":
                        points = - self.GetPoints(piece)
                        take = True
                        break
                    else:
                        break
                else:

                    break

        if take == False:
            # Adelante
            r = toTupleInt[0] + 1
            c = toTupleInt[1]

            if self.NumInRange(r, c) == True and table[r][c] != "e":

                if table[r][c][1] == "K" and table[r][c][0] == colorC:
                    points = points - self.GetPoints(piece)
                    take = True

            while r < 8:
                if table[r][c] == "e":
                    r += 1

                elif table[r][c][0] == colorC:
                    if table[r][c][1] == "R":
                        points = points - self.GetPoints(piece)
                        take = True
                        break

                    elif table[r][c][1] == "Q":
                        points = - self.GetPoints(piece)
                        take = True
                        break
                    else:
                        break
                else:

                    break

        if take == False:
            # Atras
            r = toTupleInt[0] - 1
            c = toTupleInt[1]

            if self.NumInRange(r, c) == True and table[r][c] != "e":

                if table[r][c][1] == "K" and table[r][c][0] == colorC:
                    points = points - self.GetPoints(piece)
                    take = True

            while r >= 0:
                if table[r][c] == "e":
                    r -= 1


                elif table[r][c][0] == colorC:
                    if table[r][c][1] == "R":
                        points = points - self.GetPoints(piece)
                        take = True
                        break

                    elif table[r][c][1] == "Q":
                        points = - self.GetPoints(piece)
                        take = True
                        break
                    else:
                        break
                else:

                    break

        if take == False:

            # Derecha
            r = toTupleInt[0]
            c = toTupleInt[1] + 1

            if self.NumInRange(r, c) == True and table[r][c] != "e":
                if table[r][c][1] == "K" and table[r][c][0] == colorC:
                    points = points - self.GetPoints(piece)
                    take = True

            while c < 8:
                if table[r][c] == "e":
                    c += 1

                elif table[r][c][0] == colorC:
                    if table[r][c][1] == "R":
                        points = points - self.GetPoints(piece)
                        take = True
                        break

                    elif table[r][c][1] == "Q":
                        points = - self.GetPoints(piece)
                        take = True
                        break
                    else:
                        break
                else:

                    break

        if take == False:
            # Izquierda
            r = toTupleInt[0]
            c = toTupleInt[1] - 1

            if self.NumInRange(r, c) == True and table[r][c] != "e":

                if table[r][c][1] == "K" and table[r][c][0] == colorC:
                    points = points - self.GetPoints(piece)
                    take = True

            while c >= 0:
                if table[r][c] == "e":
                    c -= 1

                elif table[r][c][0] == colorC:
                    if table[r][c][1] == "R":
                        points = points - self.GetPoints(piece)
                        take = True
                        break

                    elif table[r][c][1] == "Q":
                        points = - self.GetPoints(piece)
                        take = True
                        break
                    else:
                        break
                else:

                    break

        return points



    def OneBestMove(self,table,actualPlater,fromTuple,toTuple):
        toTupleInt = [8 - int(fromTuple[1]), int(self.getNumberPos(fromTuple[0]))]
       # if actualPlater.color == "w":
         #   moves = self.GetMovesFromPawn(fromTupleInt, actualPlater)




      #  else:






    #def BestMove(self,table,playerColor):

    '''


    def EvaluatePiece(self, toTupleInt, table, actualPlayer, originalTuple):
        if table[toTupleInt[0]][toTupleInt[1]][1] == "P":
            return
        if table[toTupleInt[0]][toTupleInt[1]][1] == "H":
            self.CHourse.getPointsHourse(toTupleInt,table)
        if table[toTupleInt[0]][toTupleInt[1]][1] == "R":
            self.CRook.getPointsRook(toTupleInt,table,actualPlayer)
        if table[toTupleInt[0]][toTupleInt[1]][1] == "B":
            self.CBishop.getPointsBishop(toTupleInt,table)
        if table[toTupleInt[0]][toTupleInt[1]][1] == "Q":
            self.CQueen.getPointsQueen(toTupleInt,table, originalTuple)
        if table[toTupleInt[0]][toTupleInt[1]][1] == "K":
            self.CKing.getKingPoints()