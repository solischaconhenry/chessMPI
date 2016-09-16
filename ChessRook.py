from ChessTable import ChessTable

class rook:

    x = ChessTable()
    def movilidadRook(self, toTuple, table,actualPlayer):
        data = self.x.GetMovesChooser4Points(toTuple,actualPlayer, table)
        return len(data)

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

        while col >= 0:
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
        defense = float(self.defendiendo(toTuple, table))
        movility =  float(self.movilidadRook(toTuple, table, actualPlayer))
        value = repr(float(5 + defense* 0.1+ (movility * 0.05)))
        return value

