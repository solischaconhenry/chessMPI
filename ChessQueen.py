from ChessTable import ChessTable

class queen:

    x = ChessTable()
    def defensaQueen(self, toTuple, table):
        counter = 0.0
        row = toTuple[0]
        col = toTuple[1]
        color = table[row][col][0]



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


        # Adelante
        r = toTuple[0] + 1
        c = toTuple[1]

        while r < 8:
            if table[r][c][0] == color:
                counter += 1.0
                r += 1

            else:
                break


        # Atras
        r = toTuple[0] - 1
        c = toTuple[1]

        while r >= 0:
            if table[r][c][0] == color:
                counter += 1.0
                r -= 1

            else:
                break


        # Derecha
        r = toTuple[0]
        c = toTuple[1]+1

        while c < 8:
            if table[r][c][0] == color:
                counter += 1.0
                c += 1

            else:
                break

        # Izquierda
        r = toTuple[0]
        c = toTuple[1] - 1

        while c >= 0:
            if table[r][c][0] == color:
                counter += 1.0
                c -= 1

            else:
                break


        return counter


    #Get the number of moves than the queen can move
    def movilityQueen(self, toTuple, table,actualPlayer):
        data = self.x.GetMovesChooser4Points(toTuple,actualPlayer, table)
        return len(data)

    def getPointsQueen(self, toTuple, table, actualPlayer):
        defense = float(self.defensaQueen(toTuple,table))
        print "Defense: " + repr(defense)
        movility = float(self.movilityQueen(toTuple, table, actualPlayer))
        print "\n Movility: " + repr(movility)
        valor = repr(float(9 + ((defense * 0.05) + (movility * 0.1))))
        print "\n Points Q: " + valor
        return valor