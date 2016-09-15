from ChessTable import ChessTable

class Hourse:

    x = ChessTable()

    def hourseMoves(self, toTuple, table):
        color = table[0][1][0]
        data = ChessTable.GetMovesChooser(toTuple,color)
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


    def getPointsHourse(self, toTuple, table):
        value = float(3 + (self.hourseMoves(toTuple,table)) + (self.defense(toTuple,table)))
        return value