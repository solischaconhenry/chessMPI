from ChessTable import ChessTable

class rook:

    x = ChessTable()
    def movilidadRook(self, toTuple, table):

        row = toTuple[0]
        col = toTuple[1]
        colorC = table[row][col][0]
        availableMoves = self.x.GetMovesChooser(toTuple,colorC)
        return len(availableMoves)

    def defendiendo(self, toTuple, table):
        row = toTuple[0]
        col = toTuple[1]
        color = table[row][col][0]
        counter= 0.0

        # Adelante derecha
        row = toTuple[0]
        col = toTuple[1] + 1

        while col < 8:
            if  table[row][col][0] == color:
                counter += 1.0
                col += 1

            else:
                break

        # Arriba por col 0
        row = toTuple[0] - 1
        col = toTuple[1]

        while row >= 0:
            if table[row][col][0] == color:
                counter += 1.0
                row -= 1

            else:
                break

        # atras sobre fila
        # Atras izquierda
        row = toTuple[0]
        col = toTuple[1] - 1

        while col < 8:
            if table[row][col][0] == color:
                counter += 1.0
                col -= 1

            else:
                break

        # atras en columna
        # Adelante izquierda
        row = toTuple[0] + 1
        col = toTuple[1]
        while row < 8 and col >= 0:
            if table[row][col][0] == color:
                counter += 1.0
                row += 1
            else:
                break
        return counter

    def getPointsRook(self, toTuple, table, actualPlayer):
        value = float(5 + float(self.movilidadRook(toTuple, actualPlayer) * 0.1) + (self.defendiendo(toTuple, table)*0.05))
        return value

