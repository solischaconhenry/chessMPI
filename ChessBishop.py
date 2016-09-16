from ChessTable import ChessTable

class Bishop:

    x = ChessTable()

    def bothBishop(self, tablero, color):
        counter = 0.0
        row = 0
        while row < 8:
            col = 0
            while col < 8:
                if tablero[row][col] != 'e':
                    if tablero[row][col][0] == color and tablero[row][col][1] == 'B':
                        counter += 0.25
                col += 1
            row += 1

        return counter


    def defenseBishop(self, toTuple, table):
        row =  toTuple[0]
        col =  toTuple[1]
        color = table[row][col][0]
        counter = 0.0
        
        # Adelante derecha
        r = toTuple[0] + 1
        c = toTuple[1] + 1

        while r < 8 and c < 8:
            if table[r][c][0] == color:
                counter += 1.0
                r += 1
                c += 1

            else:
                break

        # Atras izquierda
        r = toTuple[0] - 1
        c = toTuple[1] - 1

        while r >= 0 and c >= 0:
            if table[r][c][0] == color:
                counter += 1.0
                r -= 1
                c -= 1

            else:
                break

        # Atras derecha
        r = toTuple[0] - 1
        c = toTuple[1] + 1

        while r >= 0 and c < 8:
            if table[r][c][0] == color:
                counter += 1.0
                r -= 1
                c += 1

            else:
                break

        # Adelante izquierda
        r = toTuple[0] + 1
        c = toTuple[1] - 1

        while r < 8 and c >= 0:
            if table[r][c][0] == color:
                counter += 1.0
                r += 1
                c -= 1

            else:
                break
        return counter

    # Get the number of moves than the bishop can move
    def movilityBishop(self, toTuple, table, actualPlayer):
        data = self.x.GetMovesChooser4Points(toTuple, actualPlayer, table)
        return len(data)

    def getPointsBishop(self, toTuple, table, actualPlayer):
        color = actualPlayer
        defense = float(self.defenseBishop(toTuple,table))
        movility = float(self.movilityBishop(toTuple, table,actualPlayer))
        pairs = self.bothBishop(table, actualPlayer)
        value = float(3 + float(movility * 0.1) + float(defense*0.05) + pairs)
        return value