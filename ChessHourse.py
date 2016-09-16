from ChessTable import ChessTable

class Hourse:

    x = ChessTable()

    def hourseMoves(self, toTuple, table,actualPlayer):

        data = self.x.GetMovesChooser4Points(toTuple,actualPlayer, table)
        return len(data)

    def defense(self, toTuple, table):
        row = toTuple[0]
        col = toTuple[1]
        color = table[row][col][0]
        counter = 0.0

        if self.x.NumInRange(toTuple[0] + 2, toTuple[1] - 1):
            if table[toTuple[0] + 2][toTuple[1] - 1][0] == color:
                counter += 1.0

        if self.x.NumInRange(toTuple[0] + 2, toTuple[1] + 1):
            if table[toTuple[0] + 2][toTuple[1] + 1][0] == color:
                counter += 1.0

        if self.x.NumInRange(toTuple[0] + 1, toTuple[1] - 2):
            if table[toTuple[0] + 1][toTuple[1] - 2][0] == color:
                counter+= 1.0

        if self.x.NumInRange(toTuple[0] + 1, toTuple[1] + 2):
            if table[toTuple[0] + 1][toTuple[1] + 2][0] == color:
                counter += 1.0

        if self.x.NumInRange(toTuple[0] - 1, toTuple[1] + 2):
            if table[toTuple[0] - 1][toTuple[1] + 2][0] == color:
                counter += 1.0

        if self.x.NumInRange(toTuple[0] - 1, toTuple[1] - 2):
            if table[toTuple[0] - 1][toTuple[1] - 2][0] == color:
                counter += 1.0

        if self.x.NumInRange(toTuple[0] - 2, toTuple[1] - 1):
            if table[toTuple[0] - 2][toTuple[1] - 1][0] == color:
                counter += 1.0

        if self.x.NumInRange(toTuple[0] - 2, toTuple[1] + 1):
            if table[toTuple[0] - 2][toTuple[1] + 1] == color:
                counter += 1.0

        return counter


    def getPointsHourse(self, toTuple, table, actualPlayer):
        defense = float(self.defense(toTuple,table))
        movility = float(self.hourseMoves(toTuple,table, actualPlayer))
        value = repr(float(3 + (defense * 0.05) + (movility * 0.1)))
        return value