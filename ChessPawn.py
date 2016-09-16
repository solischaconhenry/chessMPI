class ChessPawn:
    def __init__(self):
        self.value = 0.0
        self.movilidad = []
        self.piezasComibles = []

    def getPointsPawn(self,toTuple,table,color):
        self.value = 1.0
        self.getCenterPawn(toTuple)
        self.getAdvancedPawn(toTuple,color)


        self.getPawnDOP(toTuple,table,color)
        return  self.value

    #                      (a,a)square  b o w
    def getPawnDOP(self,toTuple,table,color):

        obstacleSide = False
        obstacleFrontal = False
        fila = toTuple[0]
        columna = toTuple[1]
        if color == "w":
            i = fila - 1
            while i > 0:

                if table[i][columna] != "e":
                    if  table[i][columna][0] == color:

                        self.value = self.value - 0.25
                        obstaculoFrontal = True

                    else:

                        obstaculoFrontal = True


                if columna+1 < 8:
                     if table[i][columna + 1] != "e":

                        if table[i][columna][0] != color:

                            obstacleSide = True



                if columna - 1 >= 0:

                    if table[i][columna - 1] != "e":

                        if table[i][columna - 1]!= color:
                            obstacleSide = True
                i = i-1

        else:

            i = fila + 1
            while i < 7:

                if table[i][columna] != "e":

                    if table[i][columna][0] == color:

                        self.value = self.value - 0.25
                        color = True

                    else:
                        obstaculoFrontal = True


                if columna + 1 < 8:

                    if table[i][columna + 1] != "e":

                        if table[i][columna + 1][0] != color:

                            obstacleSide = True


                if columna - 1 > 0:

                    if table[i][columna - 1][0] != "e":

                        if table[i][columna - 1]!= color:

                            obstacleSide = True

                i = i + 1

        if obstacleFrontal == False:
            self.value = self.value + 0.25

            if obstacleSide == False:
                self.value = self.value + 0.25


    def getAdvancedPawn(self,toTuple,color):
        fila = toTuple[0]

        if color == "b":

            if fila >= 5:

                self.value = (self.self.value - 1) + ((fila - 4) * 1.5)


        else:

            if fila <= 2:
                self.value = (self.value - 1) + (((fila - 3) * -1) * 1.5)

    def getCenterPawn(self, toTuple):
        columna = toTuple[1]

        if columna == 0:
            self.value =self.value - 0.25;
        elif columna == 2:
            self.value = self.value + 0.25;
        elif columna == 3:
            self.value = self.value + 0.5;
        elif columna == 4:
            self.value = self.value + 0.5;
        elif columna == 5:
            self.value = self.value + 0.25;
        elif columna == 7:
            self.value =self.value - 0.25;



    def advance(self,toTople, tempF,tempF2, posIni, table):
        fila = toTople[0]
        columna = toTople[1]
        if table[tempF][columna] == "e":
            mov = [tempF, columna]
            self.movilidad.append(mov)

        if fila == posIni:

            if table[tempF2][columna] == "e":
                mov = [tempF2, columna]
                self.movilidad.append(mov);


    def eatRight(self, tempF, toTople, table,color):
        columna = toTople[1]

        if columna + 1 < 8:

            if table[tempF][columna + 1] != "e":


                 if table[tempF][columna + 1]!= color:

                    mov = [tempF, columna + 1]
                    self.movilidad.append(mov)
                    self.piezasComibles.append(mov)

    def  eatLeft(self,tempF,toTople,table,color):
        columna = toTople[1]
        if columna - 1 >= 0:

            if table[tempF][columna - 1] != "e":


                if table[tempF][columna - 1]!=color:

                    mov = [tempF, columna - 1]
                    self.movilidad.append(mov)
                    self.piezasComibles.append(mov)



    def refreshMov( self,toTople, table,color):
        fila = toTople[1]
        columna = toTople[1]

        self.movilidad = []
        self.piezasComibles = []

        if color == "w":
            tempF = fila - 1
            tempF2 = fila - 2
            posIni = 6

        else:
            tempF = fila + 1
            tempF2 = fila + 2
            posIni = 1



        if (tempF <= 7 and tempF >= 0) and (tempF2 <= 7 and tempF2 >= 0):
            self.advance(toTople, tempF, tempF2, posIni, table)

            self.eatLeft(tempF, toTople, table,color)

            self.eatRight(tempF, toTople, table,color)