from ChessTable import ChessTable

class Bishop:

    def parejaALfiles(self, tablero, color):
        counter = 0.0
        row = 0
        col = 0
        while row < 8 and col < 8:
            if tablero[row][col] != 'e':
                if tablero[row][col][0] == color and tablero[row][col][1] == 'B':
                    counter += 0.25
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

    def getPointsBishop(self, toTuple, table):
        row = toTuple[0]
        col = toTuple[1]
        color = table[row][col][0]

        value = float(3 + (self.parejaALfiles(table,color)) + (self.defenseBishop(toTuple,table)))
        return value