class ChessPawn:
    def __init__(self):
        self.value = 0.0
        self.movilidad = []
        self.piezasComibles = []

    def getPointsPawn(self,toTuple,table,color):
        self.value = 1.0
        self.getCenterPawn(toTuple)
        self.getAdvancedPawn(toTuple)
        self.(toTuple,table,color)
        return  value

    #                      (a,a)square  b o w
    def getPawnDOP(self,toTuple,table,color):

        obstacleSide = False
        obstacleFrontal = False
        fila = toTuple[2]
        columna = toTuple[1]
        if c == "w":
            i = fila - 1
            while i > 0:

                if table[i][columna] != "e":
                    if  table[i][columna][0] == color:

                        valor = valor - 0.25
                        obstaculoFrontal = true

                    else:

                        obstaculoFrontal = true


                if columna+1 < 8:
                     if table[i][columna + 1] != "e":

                        if table[i][columna][0] != color:

                            obstacleSide = true



                if columna - 1 >= 0:

                    if table[i][columna - 1] != "e":

                        if table[i][columna - 1]!= color:
                            obstacleSide = true
                i = i-1

        else:

            i = fila + 1
            while i < 7:

                if table[i][columna] != "e":

                    if table[i][columna][0] == c:

                        valor = valor - 0.25
                        obstaculoFrontal = true

                    else:
                        obstaculoFrontal = true


                if columna + 1 < 8:

                    if table[i][columna + 1] != "e":

                        if table[i][columna + 1][0] != color:

                            obstacleSide = true


                if columna - 1 > 0:

                    if table[i][columna - 1][0] != "e":

                        if table[i][columna - 1]!= color:

                            obstacleSide = true

                i = i + 1

        if obstacleFrontal == False:
            valor = valor + 0.25

            if obstacleSide == False:
                valor = valor + 0.25


    def getAdvancedPawn(self,toTuple):
        fila = toTuple[0]

        if color == "b":

            if fila >= 5:

                valor = (valor - 1) + ((fila - 4) * 1.5)


        else:

            if fila <= 2:

                valor = (valor - 1) + (((fila - 3) * -1) * 1.5)

    def getCenterPawn(self, toTuple):
        columna = toTuple[1]

        if columna == 0:
            this.valor = valor - 0.25;
        elif columna == 2:
            this.valor = valor + 0.25;
        elif columna == 3:
            this.valor = valor + 0.5;
        elif columna == 4:
            this.valor = valor + 0.5;
        elif columna == 5:
            this.valor = valor + 0.25;
        elif columna == 7:
            this.valor = valor - 0.25;



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
                    movilidad.append(mov)
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
            advance(toTople, tempF, tempF2, posIni, table)

            eatLeft(tempF, toTople, table,color)

            eatRight(tempF, toTople, table,color)


