class ChessTable:

    def __init__(self):
        self.squares = [['bR', 'bH', 'bB', 'bQ', 'bK', 'bB', 'bH', 'bR'],\
                        ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],\
                        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],\
                        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],\
                        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],\
                        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],\
                        ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],\
                        ['wR', 'wH', 'wB', 'wQ', 'wK', 'wB', 'wH', 'wR']]
        self.colL = ["a", "b", "c", "d", "e", "f", "g", "h"]
        self.arr = [0, 1, 2, 3, 4, 5, 6, 7]

    #*******************************************************************************************************************

    #row and colum
    #Obtener el tablero
    def GetTable(self):
        return self.squares

    #*******************************************************************************************************************

    #Obtiene el numero equivalente a la letra ingresada
    def getNumberPos(self,elem):
        for x in self.arr:
            if self.colL[x] == elem:
                return x
                # Obtiene el numero equivalente a la letra ingresada



                # *********************
    # *******************************************************************************************************************
    # Movimientos del caballo

    def ValidateMovesHourse(self, fromTupleInt, toTupleInt, actualPlayer):
        # Valida que el campo al que se va a mover este vacio o con fichas del jugador contrario
        if actualPlayer.color != self.squares[toTupleInt[0]][toTupleInt[1]][0] and \
            self.squares[toTupleInt[0]][toTupleInt[1]] == "e":

            # Se mueve hacia adelante
            #Si la columna aumenta en 1 la fila y se mueve hacia adelante
            if  toTupleInt[0] == fromTupleInt[0]+1 and \
                (toTupleInt[1] == fromTupleInt[1] + 2 or toTupleInt[1] == fromTupleInt[1] - 2):
                return True


            #Si la columna aumenta en 2 la fila y se mueve hacia adelante
            elif toTupleInt[0] == fromTupleInt[0]+2 and \
                    (toTupleInt[1] == fromTupleInt[1] + 1 or toTupleInt[1] == fromTupleInt[1] - 1):
                return True

            # Se mueve hacia atras
            # Si la columna aumenta en 1 la fila y se mueve hacia atras
            elif toTupleInt[0] == fromTupleInt[0] - 1 and \
                    (toTupleInt[1] == fromTupleInt[1] - 2 or toTupleInt[1] == fromTupleInt[1] + 2):
                return True


            # Si la columna aumenta en 2 la fila y se mueve hacia atras
            elif toTupleInt[0] == fromTupleInt[0] - 2 and \
                    (toTupleInt[1] == fromTupleInt[1] - 1 or toTupleInt[1] == fromTupleInt[1] + 1):
                return True

            else:
                return False


        else:
            return False

    #ARREGLAR PARA HACERLO MAS PEQUENO
    # *******************************************************************************************************************
    # Movimientos de la torre
    def ValidateMovesTower(self, fromTupleInt, toTupleInt, actualPlayer):
         # __________________ NEGRO ____________________________

         # Si es el jugador 2
        if actualPlayer.color == "b":

            # Valida que el campo al que se va a mover este vacio o con fichas del jugador contrario
            if self.squares[toTupleInt[0]][toTupleInt[1]] == "e" or self.squares[toTupleInt[0]][toTupleInt[1]][0] == "w":
                # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                # Se mueve hacia adelante

                #Se mueve en la fila
                if (toTupleInt[0] > fromTupleInt[0] and toTupleInt[1] == fromTupleInt[1]) :

                        indexRow =  fromTupleInt[0]+1;
                        #Se valida que no hallan piezas en medio del origen y destino
                        while indexRow < toTupleInt[0]: # desde la posicion de fila actual a las posicion de fila requerida
                            #Si se encuentra una ficha se retorna false para saber que la jugada no es valida
                            if self.squares [indexRow] [toTupleInt[1]] != "e":
                                # print "Hay fichas en medio"
                                return False
                            #Si no hay fichas sigue verificando
                            else:
                                indexRow+=1
                        return True




                # Se mueve en la columna
                elif (toTupleInt[1] > fromTupleInt[1] and toTupleInt[0] == fromTupleInt[0]):

                    indexColum = fromTupleInt[1] + 1;
                    # Se valida que no hallan piezas en medio del origen y destino
                    while indexColum < toTupleInt[1]:  # desde la posicion de fila actual a las posicion de fila requerida
                        # Si se encuentra una ficha se retorna false para saber que la jugada no es valida
                        if self.squares[toTupleInt[0]][indexColum] != "e":
                            # print "Hay fichas en medio"
                            return False
                        # Si no hay fichas sigue verificando
                        else:
                            indexColum += 1
                    return True


                #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                #Se mueve hacia atras

                #Se mueve en la fila                                                     #Se mueve hacia adelante
                elif (toTupleInt[0] < fromTupleInt[0] and toTupleInt[1] == fromTupleInt[1]):

                    indexRow = fromTupleInt[0] - 1;
                    # Se valida que no hallan piezas en medio del origen y destino
                    while indexRow > toTupleInt[0]:  # desde la posicion de fila actual a las posicion de fila requerida
                        # Si se encuentra una ficha se retorna false para saber que la jugada no es valida
                        if self.squares[indexRow][toTupleInt[1]] != "e":
                            # print "Hay fichas en         # Si es el jugador 1 medio"
                            return False
                        # Si no hay fichas sigue verificando
                        else:
                            indexRow -= 1
                    return True

                #Se mueve en la columna
                elif (toTupleInt[1] < fromTupleInt[1] and  toTupleInt[0] == fromTupleInt[0]):

                    indexColum = fromTupleInt[1] - 1;
                    # Se valida que no hallan piezas en medio del origen y destino
                    while indexColum > toTupleInt[1]:  # desde la posicion de fila actual a las posicion de fila requerida
                        # Si se encuentra una ficha se retorna false para saber que la jugada no es valida
                        if self.squares[toTupleInt[0]][indexColum] != "e":
                            # print "Hay fichas en medio"
                            return False
                        # Si no hay fichas sigue verificando
                        else:
                            indexColum -= 1
                    return True

            else:
                # print "No esta vacia o con ficha del jugador contrario"
                return False


            # __________________ BLANCO ____________________________
        else:
             # Valida que el campo al que se va a mover este vacio o con fichas del jugador contrario
             if self.squares[toTupleInt[0]][toTupleInt[1]] == "e" or self.squares[toTupleInt[0]][toTupleInt[1]][0] == "b":
                 # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                 # Se mueve hacia adelante

                 # Se mueve en la fila
                 if (toTupleInt[0] > fromTupleInt[0] and toTupleInt[1] == fromTupleInt[1]):

                     indexRow = fromTupleInt[0] + 1;
                     # Se valida que no hallan piezas en medio del origen y destino
                     while indexRow < toTupleInt[0]:  # desde la posicion de fila actual a las posicion de fila requerida
                         # Si se encuentra una ficha se retorna false para saber que la jugada no es valida
                         if self.squares[indexRow][toTupleInt[1]] != "e":
                             # print "Hay fichas en medio"
                             return False
                         # Si no hay fichas sigue verificando
                         else:
                             indexRow += 1
                     return True




                 # Se mueve en la columna
                 elif (toTupleInt[1] < fromTupleInt[1] and toTupleInt[0] == fromTupleInt[0]):

                     indexColum = fromTupleInt[1] - 1;
                     # Se valida que no hallan piezas en medio del origen y destino
                     while indexColum > toTupleInt[
                         1]:  # desde la posicion de fila actual a las posicion de fila requerida
                         # Si se encuentra una ficha se retorna false para saber que la jugada no es valida
                         if self.squares[toTupleInt[0]][indexColum] != "e":
                             # print "Hay fichas en medio"
                             return False
                         # Si no hay fichas sigue verificando
                         else:
                             indexColum -= 1
                     return True


                 # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                 # Se mueve hacia atras

                 # Se mueve en la fila                                                     #Se mueve hacia adelante
                 elif (toTupleInt[0] < fromTupleInt[0] and toTupleInt[1] == fromTupleInt[1]):

                     indexRow = fromTupleInt[0] - 1;
                     # Se valida que no hallan piezas en medio del origen y destino
                     while indexRow > toTupleInt[
                         0]:  # desde la posicion de fila actual a las posicion de fila requerida
                         # Si se encuentra una ficha se retorna false para saber que la jugada no es valida
                         if self.squares[indexRow][toTupleInt[1]] != "e":
                             # print "Hay fichas en medio"
                             return False
                         # Si no hay fichas sigue verificando
                         else:
                             indexRow -= 1
                     return True

                 # Se mueve en la columna
                 elif (toTupleInt[1] > fromTupleInt[1] and toTupleInt[0] == fromTupleInt[0]):

                     indexColum = fromTupleInt[1] + 1;
                     # Se valida que no hallan piezas en medio del origen y destino
                     while indexColum < toTupleInt[
                         1]:  # desde la posicion de fila actual a las posicion de fila requerida
                         # Si se encuentra una ficha se retorna false para saber que la jugada no es valida
                         if self.squares[toTupleInt[0]][indexColum] != "e":
                             # print "Hay fichas en medio"
                             return False
                         # Si no hay fichas sigue verificando
                         else:
                             indexColum += 1
                     return True

             else:
                 # print "No esta vacia o con ficha del jugador contrario"
                 return False
    # *******************************************************************************************************************

    #Movimientos del peon
    def ValidateMovesPawn(self,fromTupleInt,toTupleInt,actualPlayer):

        # __________________ NEGRO ____________________________

       #Si es el jugador 2
        if  actualPlayer.color == "b":
            # si esta en la primera fila puede hacer dos movimientos
            if fromTupleInt[0] == 1:
                # Si hace solo un movimiento y no hay nada adelante
                if toTupleInt[0] == fromTupleInt[0] + 1 and toTupleInt[1] == fromTupleInt[1] and \
                                self.squares[toTupleInt[0]][toTupleInt[1]] == "e":#--------------
                    return True
                # Si hace dos movimientosy no hay nada dos posiciones adelante
                elif toTupleInt[0] == fromTupleInt[0] + 2 and toTupleInt[1] == fromTupleInt[1] and \
                        self.squares[fromTupleInt[0]+1][toTupleInt[1]] == "e" and self.squares[toTupleInt[0]][toTupleInt[1]] == "e":
                    return True

                else:
                    return False

            #si ya ha hecho algun movimiento
            else:
                if toTupleInt[0] == fromTupleInt[0] + 1 and toTupleInt[1] == fromTupleInt[1] and self.squares[toTupleInt[0]+1][toTupleInt[1]] == "e":
                    return True
                #Si va a comer
                #Que solo aumente un espacio en la fila        #se mueva hacia atras en la columna      #se mueva hacia adelante en la columna
                elif toTupleInt[0] == fromTupleInt[0] + 1 and (toTupleInt[1] == fromTupleInt[1] - 1 or toTupleInt[1] == fromTupleInt[1] + 1) and \
                                self.squares[toTupleInt[0]][toTupleInt[1]][0] == "w":
                    return True

                else:
                    return False

        #__________________ BLANCO ____________________________

        # Si es el jugador 1
        else:
            # si esta en la primera fila puede hacer dos movimientos
            if fromTupleInt[0] == 6:
                # Si hace solo un movimiento y no hay nada adelante
                if toTupleInt[0] == fromTupleInt[0] - 1 and toTupleInt[1] == fromTupleInt[1] and \
                                self.squares[toTupleInt[0]][toTupleInt[1]] == "e":
                    return True
                # Si hace dos movimientosy no hay nada dos posiciones adelante
                elif toTupleInt[0] == fromTupleInt[0] - 2 and toTupleInt[1] == fromTupleInt[1] and \
                                self.squares[fromTupleInt[0] - 1][toTupleInt[1]] == "e" and \
                                self.squares[toTupleInt[0]][toTupleInt[1]] == "e":
                    return True
                else:
                    return False

            # si ya ha hecho algun movimiento
            else:
                if toTupleInt[0] == fromTupleInt[0] - 1 and toTupleInt[1] == fromTupleInt[1] and self.squares[toTupleInt[0]][toTupleInt[1]] == "e":
                    return True
                # Si va a comer
                elif toTupleInt[0] == fromTupleInt[0] - 1 and (
                    toTupleInt[1] == fromTupleInt[1] - 1 or toTupleInt[1] == fromTupleInt[1] + 1) and self.squares[toTupleInt[0]][toTupleInt[1]][0] == "b":
                    return True

                else:
                    return False

                    # ******************************************/Queen Moves/************************************************************

    #PROBLEMAS
    def ValidateQueenMoves(self, fromTupleInt, toTupleInt, actualPlayer):
        # __________________ NEGRO ____________________________

        # Si es el jugador 2
        if actualPlayer.color == "b":

            # Valida que el campo al que se va a mover este vacio o con fichas del jugador contrario
            if self.squares[toTupleInt[0]][toTupleInt[1]] == "e" or \
                            self.squares[toTupleInt[0]][toTupleInt[1]][0] == "w":
                # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                # Se mueve hacia adelante

                # Se mueve en la fila
                if (toTupleInt[0] > fromTupleInt[0] and toTupleInt[1] == fromTupleInt[1]):

                    indexRow = fromTupleInt[0] + 1
                    # Se valida que no hallan piezas en medio del origen y destino
                    while indexRow < toTupleInt[
                        0]:  # desde la posicion de fila actual a las posicion de fila requerida
                        # Si se encuentra una ficha se retorna false para saber que la jugada no es valida
                        if self.squares[indexRow][toTupleInt[1]] != "e":
                            # print "Hay fichas en medio"
                            return False
                            # Si no hay fichas sigue verificando
                        else:
                            indexRow += 1
                    return True

                # Se mueve en la columna
                elif (toTupleInt[1] > fromTupleInt[1] and toTupleInt[0] == fromTupleInt[0]):

                    indexColum = fromTupleInt[1] + 1;
                    # Se valida que no hallan piezas en medio del origen y destino
                    while indexColum < toTupleInt[
                        1]:  # desde la posicion de fila actual a las posicion de fila requerida
                        # Si se encuentra una ficha se retorna false para saber que la jugada no es valida
                        if self.squares[toTupleInt[0]][indexColum] != "e":
                            # print "Hay fichas en medio"
                            return False
                        # Si no hay fichas sigue verificando
                        else:
                            indexColum += 1
                    return True


                # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                # Se mueve hacia atras

                # Se mueve en la fila                                                     #Se mueve hacia adelante
                elif (toTupleInt[0] < fromTupleInt[0] and toTupleInt[1] == fromTupleInt[1]):

                    indexRow = fromTupleInt[0] - 1;
                    # Se valida que no hallan piezas en medio del origen y destino
                    while indexRow > toTupleInt[
                        0]:  # desde la posicion de fila actual a las posicion de fila requerida
                        # Si se encuentra una ficha se retorna false para saber que la jugada no es valida
                        if self.squares[indexRow][toTupleInt[1]] != "e":
                            # print "Hay fichas en         # Si es el jugador 1 medio"
                            return False
                        # Si no hay fichas sigue verificando
                        else:
                            indexRow -= 1
                    return True

                # Se mueve en la columna
                elif (toTupleInt[1] < fromTupleInt[1] and toTupleInt[0] == fromTupleInt[0]):

                    indexColum = fromTupleInt[1] - 1
                    # Se valida que no hallan piezas en medio del origen y destino
                    while indexColum > toTupleInt[
                        1]:  # desde la posicion de fila actual a las posicion de fila requerida
                        # Si se encuentra una ficha se retorna false para saber que la jugada no es valida
                        if self.squares[toTupleInt[0]][indexColum] != "e":
                            # print "Hay fichas en medio"
                            return False
                        # Si no hay fichas sigue verificando
                        else:
                            indexColum -= 1
                    return True

                    # Se mueve en diagonales

                    # Se mueve en diagonales

                    # valida si la fila o columna a la que va a es diferente al origen para saber si es movimiento en diagonal
                elif (toTupleInt[0] != fromTupleInt[0] and toTupleInt[1] != fromTupleInt[1] ):
                    # dependiendo del color de pieza los movimientos hacias las diagonales varia en cuento a contadores

                    # ToRow es menor a FromRow y ToCol es mayor a FromRow
                    if (toTupleInt[0] < fromTupleInt[0] and toTupleInt[1] > fromTupleInt[1]):

                        indexRow = fromTupleInt[0] - 1
                        indexColum = fromTupleInt[1] + 1

                        # hasta que se encuentre en la columna y fila correcta
                        while (indexColum < 8 and indexRow >= 0):
                            # verificar diagonal libre
                            if self.squares[indexRow][indexColum] != 'e':
                                return False
                            if (indexRow == toTupleInt[0] and indexColum == toTupleInt[1]):
                                return True

                            indexColum += 1
                            indexRow -= 1

                    # ToRow es menor a FromRow y ToCol es menor a FromCol
                    elif (toTupleInt[0] < fromTupleInt[0] and toTupleInt[1] < fromTupleInt[1]):

                        indexRow = fromTupleInt[0] - 1
                        indexColum = fromTupleInt[1] - 1

                        # hasta que se encuentre en la columna y fila correcta
                        while (indexColum >= 0 and indexRow >= 0):
                            # verificar diagonal libre
                            if self.squares[indexRow][indexColum] != 'e':
                                return False
                            if (indexRow == toTupleInt[0] and indexColum == toTupleInt[1]):
                                return True

                            indexColum -= 1
                            indexRow -= 1

                    # ToRow es mayor a FromRow y ToCol es mayor a FromCol
                    elif (toTupleInt[0] > fromTupleInt[0] and toTupleInt[1] > fromTupleInt[1]):

                        indexRow = fromTupleInt[0] + 1
                        indexColum = fromTupleInt[1] + 1

                        # hasta que se encuentre en la columna y fila correcta
                        while (indexColum < 8 and indexRow < 8):
                            # verificar diagonal libre
                            if self.squares[indexRow][indexColum] != 'e':
                                return False
                            if (indexRow == toTupleInt[0] and indexColum == toTupleInt[1]):
                                return True

                            indexColum += 1
                            indexRow += 1

                    # ToRow es mayor a FromRow y ToCol es mayor a FromCol
                    elif (toTupleInt[0] > fromTupleInt[0] and toTupleInt[1] < fromTupleInt[1]):

                        indexRow = fromTupleInt[0] + 1
                        indexColum = fromTupleInt[1] - 1

                        # hasta que se encuentre en la columna y fila correcta
                        while (indexColum >= 0 and indexRow < 8):
                            # verificar diagonal libre
                            if self.squares[indexRow][indexColum] != 'e':
                                return False
                            if (indexRow == toTupleInt[0] and indexColum == toTupleInt[1]):
                                return True

                            indexColum -= 1
                            indexRow += 1
                else:
                    # print "No esta vacia o con ficha del jugador contrario"
                    return False


                    # __________________ BLANCO ____________________________
        else:
            # Valida que el campo al que se va a mover este vacio o con fichas del jugador contrario
            if self.squares[toTupleInt[0]][toTupleInt[1]] == "e" or \
                            self.squares[toTupleInt[0]][toTupleInt[1]][0] == "b":
                # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                # Se mueve hacia adelante

                # Se mueve en la fila
                if (toTupleInt[0] > fromTupleInt[0] and toTupleInt[1] == fromTupleInt[1]):

                    indexRow = fromTupleInt[0] + 1;
                    # Se valida que no hallan piezas en medio del origen y destino
                    while indexRow < toTupleInt[
                        0]:  # desde la posicion de fila actual a las posicion de fila requerida
                        # Si se encuentra una ficha se retorna false para saber que la jugada no es valida
                        if self.squares[indexRow][toTupleInt[1]] != "e":
                            # print "Hay fichas en medio"
                            return False
                        # Si no hay fichas sigue verificando
                        else:
                            indexRow += 1
                    return True

                # Se mueve en la columna
                elif (toTupleInt[1] < fromTupleInt[1] and toTupleInt[0] == fromTupleInt[0]):

                    indexColum = fromTupleInt[1] - 1;
                    # Se valida que no hallan piezas en medio del origen y destino
                    while indexColum > toTupleInt[
                        1]:  # desde la posicion de fila actual a las posicion de fila requerida
                        # Si se encuentra una ficha se retorna false para saber que la jugada no es valida
                        if self.squares[toTupleInt[0]][indexColum] != "e":
                            # print "Hay fichas en medio"
                            return False
                        # Si no hay fichas sigue verificando
                        else:
                            indexColum -= 1
                    return True


                # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                # Se mueve hacia atras

                # Se mueve en la fila                                                     #Se mueve hacia adelante
                elif (toTupleInt[0] < fromTupleInt[0] and toTupleInt[1] == fromTupleInt[1]):

                    indexRow = fromTupleInt[0] - 1;
                    # Se valida que no hallan piezas en medio del origen y destino
                    while indexRow > toTupleInt[
                        0]:  # desde la posicion de fila actual a las posicion de fila requerida
                        # Si se encuentra una ficha se retorna false para saber que la jugada no es valida
                        if self.squares[indexRow][toTupleInt[1]] != "e":
                            # print "Hay fichas en medio"
                            return False
                        # Si no hay fichas sigue verificando
                        else:
                            indexRow -= 1
                    return True

                # Se mueve en la columna
                elif (toTupleInt[1] > fromTupleInt[1] and toTupleInt[0] == fromTupleInt[0]):

                    indexColum = fromTupleInt[1] + 1;
                    # Se valida que no hallan piezas en medio del origen y destino
                    while indexColum < toTupleInt[
                        1]:  # desde la posicion de fila actual a las posicion de fila requerida
                        # Si se encuentra una ficha se retorna false para saber que la jugada no es valida
                        if self.squares[toTupleInt[0]][indexColum] != "e":
                            # print "Hay fichas en medio"
                            return False
                        # Si no hay fichas sigue verificando
                        else:
                            indexColum += 1
                    return True

                    # Se mueve en diagonales

                    # valida si la fila o columna a la que va a es diferente al origen para saber si es movimiento en diagonal
                elif (toTupleInt[0] != fromTupleInt[0] and toTupleInt[1] != fromTupleInt[1]):
                    # dependiendo del color de pieza los movimientos hacias las diagonales varia en cuento a contadores

                    # ToRow es menor a FromRow y ToCol es mayor a FromRow
                    if (toTupleInt[0] < fromTupleInt[0] and toTupleInt[1] > fromTupleInt[1]):

                        indexRow = fromTupleInt[0] - 1
                        indexColum = fromTupleInt[1] + 1

                        # hasta que se encuentre en la columna y fila correcta
                        while (indexColum <8 and indexRow >= 0):
                            # verificar diagonal libre
                            if self.squares[indexRow][indexColum] != 'e':
                                return False
                            if(indexRow == toTupleInt[0] and indexColum == toTupleInt[1]):
                                return True

                            indexColum +=1
                            indexRow -=1

                    # ToRow es menor a FromRow y ToCol es menor a FromCol
                    elif (toTupleInt[0] < fromTupleInt[0] and toTupleInt[1] < fromTupleInt[1]):

                        indexRow = fromTupleInt[0] - 1
                        indexColum = fromTupleInt[1] - 1

                        # hasta que se encuentre en la columna y fila correcta
                        while (indexColum >= 0 and indexRow >= 0):
                            # verificar diagonal libre
                            if self.squares[indexRow][indexColum] != 'e':
                                return False
                            if (indexRow == toTupleInt[0] and indexColum == toTupleInt[1]):
                                return True

                            indexColum -= 1
                            indexRow -= 1

                    # ToRow es mayor a FromRow y ToCol es mayor a FromCol
                    elif (toTupleInt[0] > fromTupleInt[0] and toTupleInt[1] > fromTupleInt[1]):

                        indexRow = fromTupleInt[0] + 1
                        indexColum = fromTupleInt[1] + 1

                        # hasta que se encuentre en la columna y fila correcta
                        while (indexColum < 8 and indexRow < 8):
                            # verificar diagonal libre
                            if self.squares[indexRow][indexColum] != 'e':
                                return False
                            if (indexRow == toTupleInt[0] and indexColum == toTupleInt[1]):
                                return True

                            indexColum += 1
                            indexRow += 1

                    # ToRow es mayor a FromRow y ToCol es mayor a FromCol
                    elif (toTupleInt[0] > fromTupleInt[0] and toTupleInt[1] < fromTupleInt[1]):

                        indexRow = fromTupleInt[0] + 1
                        indexColum = fromTupleInt[1] - 1

                        # hasta que se encuentre en la columna y fila correcta
                        while (indexColum >=0 and indexRow < 8):
                            # verificar diagonal libre
                            if self.squares[indexRow][indexColum] != 'e':
                                return False
                            if (indexRow == toTupleInt[0] and indexColum == toTupleInt[1]):
                                return True

                            indexColum -= 1
                            indexRow += 1

            else:
                # print "No esta vacia o con ficha del jugador contrario"
                return False

    def ValidateBishopMoves(self, fromTupleInt, toTupleInt, actualPlayer):
        # __________________ NEGRO ____________________________

         # Si es el jugador 2
         if actualPlayer.color == "b":

             # Valida que el campo al que se va a mover este vacio o con fichas del jugador contrario
             if self.squares[toTupleInt[0]][toTupleInt[1]] == "e" or self.squares[toTupleInt[0]][toTupleInt[1]][0] == "w":
                 # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

                 # Se mueve en diagonales

                 # valida si la fila o columna a la que va a es diferente al origen para saber si es movimiento en diagonal
                 if (toTupleInt[0] != fromTupleInt[0] and toTupleInt[1] != fromTupleInt[1]):
                     # dependiendo del color de pieza los movimientos hacias las diagonales varia en cuento a contadores


                     # ToRow es menor a FromRow y ToCol es mayor a FromRow
                     if (toTupleInt[0] < fromTupleInt[0] and toTupleInt[1] > fromTupleInt[1]):

                         indexRow = fromTupleInt[0] - 1
                         indexColum = fromTupleInt[1] + 1

                         # hasta que se encuentre en la columna y fila correcta
                         while (indexColum < 8 and indexRow >= 0):
                             # verificar diagonal libre
                             if self.squares[indexRow][indexColum] != 'e':
                                 return False
                             if (indexRow == toTupleInt[0] and indexColum == toTupleInt[1]):
                                 return True

                             indexColum += 1
                             indexRow -= 1

                     # ToRow es menor a FromRow y ToCol es menor a FromCol
                     elif (toTupleInt[0] < fromTupleInt[0] and toTupleInt[1] < fromTupleInt[1]):

                         indexRow = fromTupleInt[0] - 1
                         indexColum = fromTupleInt[1] - 1

                         # hasta que se encuentre en la columna y fila correcta
                         while (indexColum >= 0 and indexRow >= 0):
                             # verificar diagonal libre
                             if self.squares[indexRow][indexColum] != 'e':
                                 return False
                             if (indexRow == toTupleInt[0] and indexColum == toTupleInt[1]):
                                 return True

                             indexColum -= 1
                             indexRow -= 1

                     # ToRow es mayor a FromRow y ToCol es mayor a FromCol
                     elif (toTupleInt[0] > fromTupleInt[0] and toTupleInt[1] > fromTupleInt[1]):

                         indexRow = fromTupleInt[0] + 1
                         indexColum = fromTupleInt[1] + 1

                         # hasta que se encuentre en la columna y fila correcta
                         while (indexColum < 8 and indexRow < 8):
                             # verificar diagonal libre
                             if self.squares[indexRow][indexColum] != 'e':
                                 return False
                             if (indexRow == toTupleInt[0] and indexColum == toTupleInt[1]):
                                 return True

                             indexColum += 1
                             indexRow += 1

                     # ToRow es mayor a FromRow y ToCol es mayor a FromCol
                     elif (toTupleInt[0] > fromTupleInt[0] and toTupleInt[1] < fromTupleInt[1]):

                         indexRow = fromTupleInt[0] + 1
                         indexColum = fromTupleInt[1] - 1

                         # hasta que se encuentre en la columna y fila correcta
                         while (indexColum >= 0 and indexRow < 8):
                             # verificar diagonal libre
                             if self.squares[indexRow][indexColum] != 'e':
                                 return False
                             if (indexRow == toTupleInt[0] and indexColum == toTupleInt[1]):
                                 return True

                             indexColum -= 1
                             indexRow += 1


             else:
                # print "No esta vacia o con ficha del jugador contrario"
                return False


                         # __________________ BLANCO ____________________________
         else:
             # Valida que el campo al que se va a mover este vacio o con fichas del jugador contrario
             if self.squares[toTupleInt[0]][toTupleInt[1]] == "e" or self.squares[toTupleInt[0]][toTupleInt[1]][0] == "b":
                 # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

                 # Se mueve en diagonales

                 # valida si la fila o columna a la que va a es diferente al origen para saber si es movimiento en diagonal
                 if (toTupleInt[0] != fromTupleInt[0] and toTupleInt[1] != fromTupleInt[1]):
                    # dependiendo del color de pieza los movimientos hacias las diagonales varia en cuento a contadores


                    # ToRow es menor a FromRow y ToCol es mayor a FromRow
                    if (toTupleInt[0] < fromTupleInt[0] and toTupleInt[1] > fromTupleInt[1]):

                        indexRow = fromTupleInt[0] - 1
                        indexColum = fromTupleInt[1] + 1

                        # hasta que se encuentre en la columna y fila correcta
                        while (indexColum < 8 and indexRow >= 0):
                            # verificar diagonal libre
                            if self.squares[indexRow][indexColum] != 'e':
                                return False
                            if (indexRow == toTupleInt[0] and indexColum == toTupleInt[1]):
                                return True

                            indexColum += 1
                            indexRow -= 1

                    # ToRow es menor a FromRow y ToCol es menor a FromCol
                    elif (toTupleInt[0] < fromTupleInt[0] and toTupleInt[1] < fromTupleInt[1]):

                        indexRow = fromTupleInt[0] - 1
                        indexColum = fromTupleInt[1] - 1

                        # hasta que se encuentre en la columna y fila correcta
                        while (indexColum >= 0 and indexRow >= 0):
                            # verificar diagonal libre
                            if self.squares[indexRow][indexColum] != 'e':
                                return False
                            if (indexRow == toTupleInt[0] and indexColum == toTupleInt[1]):
                                return True

                            indexColum -= 1
                            indexRow -= 1

                    # ToRow es mayor a FromRow y ToCol es mayor a FromCol
                    elif (toTupleInt[0] > fromTupleInt[0] and toTupleInt[1] > fromTupleInt[1]):

                        indexRow = fromTupleInt[0] + 1
                        indexColum = fromTupleInt[1] + 1

                        # hasta que se encuentre en la columna y fila correcta
                        while (indexColum < 8 and indexRow < 8):
                            # verificar diagonal libre
                            if self.squares[indexRow][indexColum] != 'e':
                                return False
                            if (indexRow == toTupleInt[0] and indexColum == toTupleInt[1]):
                                return True

                            indexColum += 1
                            indexRow += 1

                    # ToRow es mayor a FromRow y ToCol es mayor a FromCol
                    elif (toTupleInt[0] > fromTupleInt[0] and toTupleInt[1] < fromTupleInt[1]):

                        indexRow = fromTupleInt[0] + 1
                        indexColum = fromTupleInt[1] - 1

                        # hasta que se encuentre en la columna y fila correcta
                        while (indexColum >= 0 and indexRow < 8):
                            # verificar diagonal libre
                            if self.squares[indexRow][indexColum] != 'e':
                                return False
                            if (indexRow == toTupleInt[0] and indexColum == toTupleInt[1]):
                                return True

                            indexColum -= 1
                            indexRow += 1
             else:
                 # print "No esta vacia o con ficha del jugador contrario"
                 return False


                 # ****************************************/King Moves/***************************************************************

    def ValidateKingMoves(self, fromTupleInt, toTupleInt, actualPlayer):
        # __________________ NEGRO ____________________________

        # Si es el jugador 2
        if actualPlayer.color == "b":

            # Valida que el campo al que se va a mover este vacio o con fichas del jugador contrario
            if self.squares[toTupleInt[0]][toTupleInt[1]] == "e" or self.squares[toTupleInt[0]][toTupleInt[1]][0] == "w":

                # hacia misma columna,1 espacio
                if (toTupleInt[1] == fromTupleInt[1] + 1 or toTupleInt[1] == fromTupleInt[1] - 1):
                    return True

                # hacia la misma fila, 1 espacio
                elif (toTupleInt[0] == fromTupleInt[0] + 1 or toTupleInt[0] == fromTupleInt[0] - 1):
                    return True

                # desde perspectiva blanca
                # sobre diagonal izq sup, 1 espacio
                elif (toTupleInt[0] == fromTupleInt[0] - 1 and toTupleInt[1] == fromTupleInt[1] - 1):
                    return True

                # desde perspectiva blanca
                # sobre diagonal der sup, 1 espacio
                elif (toTupleInt[0] == fromTupleInt[0] - 1 and toTupleInt[1] == fromTupleInt[1] + 1):
                    return True

                # desde perspectiva blanca
                # sobre diagonal izq inf, 1 espacio
                elif (toTupleInt[0] == fromTupleInt[0] + 1 and toTupleInt[1] == fromTupleInt[1] - 1):
                    return True

                # desde perspectiva blanca
                # sobre diagonal der inf, 1 espacio
                elif (toTupleInt[0] == fromTupleInt[0] + 1 and toTupleInt[1] == fromTupleInt[1] + 1):
                    return True

                else:
                    return False

                # __________________ BLANCO ____________________________
        else:

            # Valida que el campo al que se va a mover este vacio o con fichas del jugador contrario
            if self.squares[toTupleInt[0]][toTupleInt[1]] == "e" or self.squares[toTupleInt[0]][toTupleInt[1]][0] == "b":

                # hacia misma columna,1 espacio
                if (toTupleInt[1] == fromTupleInt[1] + 1 or toTupleInt[1] == fromTupleInt[1] - 1):
                    return True

                # hacia la misma fila, 1 espacio
                elif (toTupleInt[0] == fromTupleInt[0] + 1 or toTupleInt[0] == fromTupleInt[0] - 1):
                    return True

                # desde perspectiva blanca
                # sobre diagonal izq sup, 1 espacio
                elif (toTupleInt[0] == fromTupleInt[0] - 1 and toTupleInt[1] == fromTupleInt[1] - 1):
                    return True

                # desde perspectiva blanca
                # sobre diagonal der sup, 1 espacio
                elif (toTupleInt[0] == fromTupleInt[0] - 1 and toTupleInt[1] == fromTupleInt[1] + 1):
                    return True

                # desde perspectiva blanca
                # sobre diagonal izq inf, 1 espacio
                elif (toTupleInt[0] == fromTupleInt[0] + 1 and toTupleInt[1] == fromTupleInt[1] - 1):
                    return True

                # desde perspectiva blanca
                # sobre diagonal der inf, 1 espacio
                elif (toTupleInt[0] == fromTupleInt[0] + 1 and toTupleInt[1] == fromTupleInt[1] + 1):
                    return True

                else:
                    return False

    def ValidateMoves(self,fromTupleInt,toTupleInt,actualPlayer):
        if actualPlayer.color == self.squares[fromTupleInt[0]][fromTupleInt[1]][0]:  # si el color es el mismo a la primera letra de la pieza
            if self.squares[fromTupleInt[0]][fromTupleInt[1]][1] == "P":
                return self.ValidateMovesPawn(fromTupleInt,toTupleInt,actualPlayer)

            elif self.squares[fromTupleInt[0]][fromTupleInt[1]][1] == "R":
                return self.ValidateMovesTower(fromTupleInt, toTupleInt, actualPlayer)

            elif self.squares[fromTupleInt[0]][fromTupleInt[1]][1] == "H":
                return self.ValidateMovesHourse(fromTupleInt, toTupleInt, actualPlayer)

            elif self.squares[fromTupleInt[0]][fromTupleInt[1]][1] == "B":
                return self.ValidateBishopMoves(fromTupleInt, toTupleInt, actualPlayer)

            elif self.squares[fromTupleInt[0]][fromTupleInt[1]][1] == "Q":
                return self.ValidateQueenMoves(fromTupleInt, toTupleInt, actualPlayer)

            elif self.squares[fromTupleInt[0]][fromTupleInt[1]][1] == "K":
                return self.ValidateKingMoves(fromTupleInt, toTupleInt, actualPlayer)

            else:
                return False
        else:
            return False



    #*******************************************************************************************************************

    def SetPositionTable(self,fromTuple,toTuple,actualPlayer):
        fromTupleInt = [8-int(fromTuple[1]),int(self.getNumberPos(fromTuple[0]))]
        toTupleInt = [8-int(toTuple[1]),int(self.getNumberPos(toTuple[0]))]

        if self.ValidateMoves(fromTupleInt,toTupleInt,actualPlayer) == True:
            self.squares[8 - int(toTuple[1])][int(self.getNumberPos(toTuple[0]))] = self.squares[8 - int(fromTuple[1])][
                int(self.getNumberPos(fromTuple[0]))]
            self.squares[8 - int(fromTuple[1])][int(self.getNumberPos(fromTuple[0]))] = 'e'
          #  check = self.WatchMove_Check(self.GetMovesChooser(fromTuple,actualPlayer),actualPlayer)
           # if check != "":
          #      print 'check: ' + check
            return True
        else:
            return False


    #busca en el arreglo de jugadas posibles de una pieza, si alguna tiene al Rey contrario en la mira para indicar jaque
    def WatchMove_Check(self, PosibleMoves, CurrentColor):
        index = 0

        while(index <= len(PosibleMoves)):
            raw = PosibleMoves[index][1]
            col = self.getNumberPos(PosibleMoves[index][0])

            if self.squares[raw][col][1] == 'K' and self.squares[raw][col][0] == CurrentColor:
                pos = raw+col
                return pos
            index += 1

        return ""



    # *******************************************************************************************************************
    def GetMovesFromPawn(self,fromTupleInt,actualPlayer):
        possibleMoves = []
        index = 0
        if actualPlayer.color == "b":
            # si esta en la primera fila puede hacer dos movimientos

            #Agregar la primera posicion si no hay nada
            if  self.NumInRange(fromTupleInt[0] + 1,fromTupleInt[1]): #Revisa que no se pase de los indices
                if self.squares[fromTupleInt[0]+1][fromTupleInt[1]] == "e":

                        #possibleMoves[index] = [[fromTupleInt[0] + 1][fromTupleInt[1]]]
                        # Se convierte de nuevo
                        strPawn = "" + self.colL[fromTupleInt[1]] + "" + str(8 - fromTupleInt[0] - 1)
                        possibleMoves.append(strPawn)

                        # Agregar la primera posicion si no hay nada y si esta en la primera jugada
                        if self.NumInRange(fromTupleInt[0] + 1, fromTupleInt[1]):
                            if self.squares[fromTupleInt[0]+2][fromTupleInt[1]] == "e":

                                 #possibleMoves[index] = [[fromTupleInt[0] + 2][fromTupleInt[1]]]
                                 #Se convierte de nuevo
                                 strPawn = "" + self.colL[fromTupleInt[1]] + "" + str(8 - fromTupleInt[0]-2)
                                 possibleMoves.append(strPawn)

                #Si se puede comer a la izquierda
                if self.NumInRange(fromTupleInt[0] + 1, fromTupleInt[1]-1):
                    if self.squares[fromTupleInt[0]+1][fromTupleInt[1]-1] != "e" and self.squares[fromTupleInt[0]+1][fromTupleInt[1]-1][0] == "w":
                       # possibleMoves[index] = [fromTupleInt[0]+1][fromTupleInt[1]-1]
                        # Se convierte de nuevo
                        strPawn = "" + self.colL[fromTupleInt[1]-1] + "" + str(8 - fromTupleInt[0] - 1)
                        possibleMoves.append(strPawn)
                # Si se puede comer a la derecha

                if self.NumInRange(fromTupleInt[0] + 1, fromTupleInt[1]+1):
                    if self.squares[fromTupleInt[0]+1][fromTupleInt[1]+1] != "e" and self.squares[fromTupleInt[0]+1][fromTupleInt[1]+1][0] == "w":
                        #possibleMoves[index] = [fromTupleInt[0]+1][fromTupleInt[1]+1]
                        # Se convierte de nuevo
                        strPawn = "" + self.colL[fromTupleInt[1]-1] + "" + str(8 - fromTupleInt[0] - 1)
                        possibleMoves.append(strPawn)

        else:
            # si esta en la primera fila puede hacer dos movimientos

            # Agregar la primera posicion si no hay nada
            if self.NumInRange(fromTupleInt[0] - 1, fromTupleInt[1]):
                if self.squares[fromTupleInt[0] - 1][fromTupleInt[1]] == "e":
                    #possibleMoves[index] = [[fromTupleInt[0] - 1][fromTupleInt[1]]] #Se convierte de nuevo
                    strPawn = "" + self.colL[fromTupleInt[1]] + "" + str(8 - fromTupleInt[0] + 1)
                    possibleMoves.append(strPawn)
                    # Agregar la primera posicion si no hay nada y si esta en la primera jugada
                    if self.NumInRange(fromTupleInt[0] - 2, fromTupleInt[1]):
                        if self.squares[fromTupleInt[0] - 2][fromTupleInt[1]] == "e" and fromTupleInt[0] == 6:
                            # possibleMoves[index] = [[fromTupleInt[0] - 2][fromTupleInt[1]]]
                            # Se convierte de nuevo
                            strPawn = "" + self.colL[fromTupleInt[1]] + "" + str(8 - fromTupleInt[0] + 2)
                            possibleMoves.append(strPawn)

            # Si se puede comer a la izquierda
            if self.NumInRange(fromTupleInt[0] - 1, fromTupleInt[1]-1):
                if self.squares[fromTupleInt[0] - 1][fromTupleInt[1] - 1] != "e" and \
                                self.squares[fromTupleInt[0] - 1][fromTupleInt[1] - 1][0] == "b":
                    #possibleMoves[index] = [fromTupleInt[0] - 1][fromTupleInt[1] - 1]
                    # Se convierte de nuevo
                    strPawn = "" + self.colL[fromTupleInt[1] - 1 ] + "" + str(8 - fromTupleInt[0] + 1)
                    possibleMoves.append(strPawn)
                # Si se puede comer a la derecha
            if self.NumInRange(fromTupleInt[0] - 1, fromTupleInt[1] + 1):
                if self.squares[fromTupleInt[0] - 1][fromTupleInt[1] + 1] != "e" and \
                                self.squares[fromTupleInt[0] - 1][fromTupleInt[1] + 1][0] == "b":
                    #possibleMoves[index] = [fromTupleInt[0] - 1][fromTupleInt[1] + 1]
                    # Se convierte de nuevo
                    strPawn = "" + self.colL[fromTupleInt[1] + 1] + "" + str(8 - fromTupleInt[0] + 1)
                    possibleMoves.append(strPawn)

        return possibleMoves

        # *******************************************************************************************************************

    # *******************************************************************************************************************
    def NumInRange(self,num1,num2):
        if num1 >= 0 and num1 <=7 and num2 >= 0 and num2 <=7:
            return True
        else:
            return False

    # *******************************************************************************************************************
    def GetMovesFromHourse(self, fromTupleInt, actualPlayer):
        possibleMoves = []
        index = 0

        colorC = ""
        if actualPlayer.color == "w":
            colorC = "b"
        elif actualPlayer.color == "b":
            colorC = "w"

        if self.NumInRange(fromTupleInt[0] + 2,fromTupleInt[1] - 1):
            if self.squares[fromTupleInt[0] + 2][fromTupleInt[1] - 1]== "e" or self.squares[fromTupleInt[0] + 2][fromTupleInt[1] - 1][0] == colorC:

                strPawn = "" + self.colL[fromTupleInt[1] - 1] + "" + str(8 - fromTupleInt[0] - 2)
                possibleMoves.append(strPawn)

        if self.NumInRange(fromTupleInt[0] + 2, fromTupleInt[1] + 1):
            if self.squares[fromTupleInt[0] + 2][fromTupleInt[1] + 1] == "e" or self.squares[fromTupleInt[0] + 2][fromTupleInt[1] + 1][0] == colorC\
            :

                strPawn = "" + self.colL[fromTupleInt[1] + 1] + "" + str(8 - fromTupleInt[0] - 2)
                possibleMoves.append(strPawn)

        if self.NumInRange(fromTupleInt[0] + 1, fromTupleInt[1] - 2):
            if self.squares[fromTupleInt[0] + 1][fromTupleInt[1] - 2] == "e" or self.squares[fromTupleInt[0] + 1][fromTupleInt[1] - 2][0] == colorC\
            :
                strPawn = "" + self.colL[fromTupleInt[1] - 2] + "" + str(8 - fromTupleInt[0] - 1)
                possibleMoves.append(strPawn)

        if self.NumInRange(fromTupleInt[0] + 1, fromTupleInt[1] + 2):
            if self.squares[fromTupleInt[0] + 1][fromTupleInt[1] + 2] == "e" or self.squares[fromTupleInt[0] + 1][fromTupleInt[1] + 2][0] == colorC\
            :
                strPawn = "" + self.colL[fromTupleInt[1] +2 ] + "" + str(8 - fromTupleInt[0] - 1)
                possibleMoves.append(strPawn)

        if self.NumInRange(fromTupleInt[0] - 1, fromTupleInt[1] + 2):
            if self.squares[fromTupleInt[0] - 1][fromTupleInt[1] + 2] == "e" or self.squares[fromTupleInt[0] - 1][fromTupleInt[1] + 2][0] == colorC\
           :
                strPawn = "" + self.colL[fromTupleInt[1] + 2] + "" + str(8 - fromTupleInt[0] + 1)
                possibleMoves.append(strPawn)

        if self.NumInRange(fromTupleInt[0] - 1, fromTupleInt[1] - 2):
            if self.squares[fromTupleInt[0] - 1][fromTupleInt[1] - 2] == "e" or self.squares[fromTupleInt[0] - 1][fromTupleInt[1] - 2][0] == colorC\
            :
                strPawn = "" + self.colL[fromTupleInt[1] - 2] + "" + str(8 - fromTupleInt[0] + 1)
                possibleMoves.append(strPawn)

        if self.NumInRange(fromTupleInt[0] - 2, fromTupleInt[1] - 1):
            if self.squares[fromTupleInt[0] - 2][fromTupleInt[1] - 1] == "e" or self.squares[fromTupleInt[0] - 2][fromTupleInt[1] - 1][0] == colorC\
            :

                strPawn = "" + self.colL[fromTupleInt[1] - 1] + "" + str(8 - fromTupleInt[0] + 2)
                possibleMoves.append(strPawn)

        if self.NumInRange(fromTupleInt[0] - 2, fromTupleInt[1] + 1):
            if self.squares[fromTupleInt[0] - 2][fromTupleInt[1] + 1] == "e" or self.squares[fromTupleInt[0] - 2][fromTupleInt[1] + 1] == colorC\
            :

                strPawn = "" + self.colL[fromTupleInt[1] + 1] + "" + str(8 - fromTupleInt[0] + 2)
                possibleMoves.append(strPawn)

        return possibleMoves

    # *******************************************************************************************************************
    def GetMovesFromRook(self, fromTupleInt, actualPlayer):
        PossibleMoves = []
        colorC = ""
        if actualPlayer.color == "w":
            colorC = "b"
        elif actualPlayer.color == "b":
            colorC = "w"

        if (self.squares[fromTupleInt[0]][fromTupleInt[1]][0]) != colorC:

            # Adelante derecha
            row = fromTupleInt[0]
            col = fromTupleInt[1] + 1

            while col < 8:
                if self.squares[row][col] == "e" or self.squares[row][col][0] == colorC:
                    strw = "" + self.colL[col] + "" + str(8 - row)
                    PossibleMoves.append(strw)
                    col += 1

                else:
                    break

            # Arriba por col 0
            row = fromTupleInt[0] - 1
            col = fromTupleInt[1]

            while row >= 0:
                if self.squares[row][col] == "e" or self.squares[row][col][0] == colorC:
                    strw =  "" + self.colL[col] + "" + str(8 - row)
                    PossibleMoves.append(strw)
                    row -= 1

                else:
                    break

            # atras sobre fila
            # Atras izquierda
            row = fromTupleInt[0]
            col = fromTupleInt[1] - 1

            while col < 8:
                if self.squares[row][col] == "e" or self.squares[row][col][0] == colorC:
                    strw = "" + self.colL[col] + "" + str(8 - row)
                    PossibleMoves.append(strw)
                    col -= 1

                else:
                    break

            # atras en columna
            # Adelante izquierda
            row = fromTupleInt[0] + 1
            col = fromTupleInt[1]
            while row < 8 and col >= 0:
                if self.squares[row][col] == "e" or self.squares[row][col][0] == colorC:
                    strw =  self.colL[col] + "" + str(8 - row)
                    PossibleMoves.append(strw)
                    row += 1
                else:
                    break
            return PossibleMoves

    # *******************************************************************************************************************
    def GetMovesFromBishopMoves(self, fromTupleInt, actualPlayer):
        PossibleMoves = []
        colorC = ""
        if actualPlayer.color == "w":
            colorC = "b"
        elif actualPlayer.color == "b":
            colorC = "w"

        if(self.squares[fromTupleInt[0]][fromTupleInt[1]][0]) != colorC:

            #Adelante derecha
            r = fromTupleInt[0] + 1
            c = fromTupleInt[1] + 1

            while r<8 and c<8:
                if self.squares[r][c] == "e" or self.squares[r][c][0]== colorC:
                    strw = "" + self.colL[c] + "" + str(8 - r)
                    PossibleMoves.append(strw)
                    r+=1
                    c+=1

                else:
                    break

            #Atras izquierda
            r = fromTupleInt[0] - 1
            c = fromTupleInt[1] - 1


            while r>=0 and c>=0:
                if self.squares[r][c] == "e" or self.squares[r][c][0]== colorC:
                    strw = "" + self.colL[c] + "" + str(8 - r)
                    PossibleMoves.append(strw)
                    r-=1
                    c-=1

                else:
                    break

            #Atras derecha
            r = fromTupleInt[0] - 1
            c = fromTupleInt[1] + 1

            while r >= 0 and c < 8:
                if self.squares[r][c] == "e" or self.squares[r][c][0] == colorC:
                    strw = "" + self.colL[c] + "" + str(8 - r)
                    PossibleMoves.append(strw)
                    r -= 1
                    c += 1

                else:
                    break

            # Adelante izquierda
            r = fromTupleInt[0] + 1
            c = fromTupleInt[1] - 1

            while r < 8  and c >= 0:
                if self.squares[r][c] == "e" or self.squares[r][c][0] == colorC:
                    strw = "" + self.colL[c] + "" + str(8 - r)
                    PossibleMoves.append(strw)
                    r += 1
                    c -= 1

                else:
                    break
            return PossibleMoves

    # *******************************************************************************************************************
    def GetMovesFromQueen (self, fromTupleInt, actualPlayer):
        PossibleMoves = []
        colorC = ""
        if actualPlayer.color == "w":
            colorC = "b"
        elif actualPlayer.color == "b":
            colorC = "w"

        if (self.squares[fromTupleInt[0]][fromTupleInt[1]][0]) != colorC:

            # Adelante derecha
            r = fromTupleInt[0] + 1
            c = fromTupleInt[1] + 1

            while r < 8 and c < 8:
                if self.squares[r][c] == "e" or self.squares[r][c][0] == colorC:
                    strw = "" + self.colL[c] + "" + str(8 - r)
                    PossibleMoves.append(strw)
                    r += 1
                    c += 1

                else:
                    break

            # Atras izquierda
            r = fromTupleInt[0] - 1
            c = fromTupleInt[1] - 1


            while r >= 0 and c >= 0:
                if self.squares[r][c] == "e" or self.squares[r][c][0] == colorC:
                    strw = "" + self.colL[c] + "" + str(8 - r)
                    PossibleMoves.append(strw)
                    r -= 1
                    c -= 1

                else:
                    break

            # Atras derecha
            r = fromTupleInt[0] - 1
            c = fromTupleInt[1] + 1

            while r >= 0 and c < 8:
                if self.squares[r][c] == "e" or self.squares[r][c][0] == colorC:
                    strw = "" + self.colL[c] + "" + str(8 - r)
                    PossibleMoves.append(strw)
                    r -= 1
                    c += 1

                else:
                    break

            # Adelante izquierda
            r = fromTupleInt[0] + 1
            c = fromTupleInt[1] - 1

            while r < 8 and c >= 0:
                if self.squares[r][c] == "e" or self.squares[r][c][0] == colorC:
                    strw = "" + self.colL[c] + "" + str(8 - r)
                    PossibleMoves.append(strw)
                    r += 1
                    c -= 1

                else:
                    break


            # Adelante
            r = fromTupleInt[0] + 1
            c = fromTupleInt[1]

            while r < 8:
                if self.squares[r][c] == "e" or self.squares[r][c][0] == colorC:
                    strw = "" + self.colL[c] + "" + str(8 - r)
                    PossibleMoves.append(strw)
                    r += 1

                else:
                    break


            # Atras
            r = fromTupleInt[0] - 1
            c = fromTupleInt[1]

            while r >= 0:
                if self.squares[r][c] == "e" or self.squares[r][c][0] == colorC:
                    strw = "" + self.colL[c] + "" + str(8 - r)
                    PossibleMoves.append(strw)
                    r -= 1

                else:
                    break


            # Derecha
            r = fromTupleInt[0]
            c = fromTupleInt[1]+1

            while c < 8:
                if self.squares[r][c] == "e" or self.squares[r][c][0] == colorC:
                    strw = "" + self.colL[c] + "" + str(8 - r)
                    PossibleMoves.append(strw)
                    c += 1

                else:
                    break

            # Izquierda
            r = fromTupleInt[0]
            c = fromTupleInt[1] - 1

            while c >= 0:
                if self.squares[r][c] == "e" or self.squares[r][c][0] == colorC:
                    strw = "" + self.colL[c] + "" + str(8 - r)
                    PossibleMoves.append(strw)
                    c -= 1

                else:
                    break


            return PossibleMoves

    # *******************************************************************************************************************
    def GetMovesFromKing(self, fromTupleInt, actualPlayer):
        PossibleMoves = ""
        colorC = ""
        if actualPlayer.color == "w":
            colorC = "b"
        elif actualPlayer.color == "b":
            colorC = "w"

        if (self.squares[fromTupleInt[0]][fromTupleInt[1]][0]) != colorC:

            # Adelante derecha
            r = fromTupleInt[0] + 1
            c = fromTupleInt[1] + 1

            if c < 8 and r < 8 and (self.squares[r][c] == "e" or self.squares[r][c][0] == colorC):
                PossibleMoves.append(self.colL[c] + "" + str(8 - r))


            # Atras izquierda
            r = fromTupleInt[0] - 1
            c = fromTupleInt[1] - 1


            if c >= 0 and r >= 0 and (self.squares[r][c] == "e" or self.squares[r][c][0] == colorC):
                PossibleMoves.append(self.colL[c] + "" + str(8 - r))


            # Atras derecha
            r = fromTupleInt[0] - 1
            c = fromTupleInt[1] + 1


            if r >= 0 and  c < 8 and (self.squares[r][c] == "e" or self.squares[r][c][0] == colorC):
                PossibleMoves.append(self.colL[c] + "" + str(8 - r))


            # Adelante izquierda
            r = fromTupleInt[0] + 1
            c = fromTupleInt[1] - 1

            if r < 8 and  c >= 0 and (self.squares[r][c] == "e" or self.squares[r][c][0] == colorC):
                PossibleMoves.append(self.colL[c] + "" + str(8 - r))


            # Adelante
            r = fromTupleInt[0] + 1
            c = fromTupleInt[1]


            if r < 8 and (self.squares[r][c] == "e" or self.squares[r][c][0] == colorC):
                PossibleMoves.append(self.colL[c] + "" + str(8 - r))



            # Atras
            r = fromTupleInt[0] - 1
            c = fromTupleInt[1]


            if r >= 0 and (self.squares[r][c] == "e" or self.squares[r][c][0] == colorC):
                PossibleMoves.append(self.colL[c] + "" + str(8 - r))

            # Derecha
            r = fromTupleInt[0]
            c = fromTupleInt[1] + 1


            if c < 8 and (self.squares[r][c] == "e" or self.squares[r][c][0] == colorC):
                PossibleMoves.append(self.colL[c] + "" + str(8 - r))


            # Izquierda
            r = fromTupleInt[0]
            c = fromTupleInt[1] - 1


            if c >= 0 and (self.squares[r][c] == "e" or self.squares[r][c][0] == colorC):
                PossibleMoves.append(self.colL[c] + "" + str(8 - r))


            return PossibleMoves

    # *******************************************************************************************************************

    def GetMovesChooser(self, fromTuple, actualPlayer):
            #indica el tipo de pieza de la casilla indicada por el jugador
            fromTupleInt = [8 - int(fromTuple[1]), int(self.getNumberPos(fromTuple[0]))]
            if self.squares[fromTupleInt[0]][fromTupleInt[1]][1] == "P":
                data = self.GetMovesFromPawn(fromTupleInt, actualPlayer)
                print data
                return data
            if self.squares[fromTupleInt[0]][fromTupleInt[1]][1] == "H":
                data = self.GetMovesFromHourse(fromTupleInt, actualPlayer)
                print data
                return data
            if self.squares[fromTupleInt[0]][fromTupleInt[1]][1] == "R":
                data = self.GetMovesFromRook(fromTupleInt, actualPlayer)
                print data
                return data
            if self.squares[fromTupleInt[0]][fromTupleInt[1]][1] == "B":
                data =  self.GetMovesFromBishopMoves(fromTupleInt, actualPlayer)
                print data
                return data
            if self.squares[fromTupleInt[0]][fromTupleInt[1]][1] == "Q":
                data =  self.GetMovesFromQueen(fromTupleInt, actualPlayer)
                print data
                return data
            if self.squares[fromTupleInt[0]][fromTupleInt[1]][1] == "K":
                data = self.GetMovesFromKing(fromTupleInt, actualPlayer)
                print data
                return data

#*******************************************GET MOVES FOR GET POINTS***************************************************

    def GetMovesChooser4Points(self, fromTuple, actualPlayer, table):
            #indica el tipo de pieza de la casilla indicada por el jugador
            fromTupleInt = [8 - int(fromTuple[1]), int(self.getNumberPos(fromTuple[0]))]
            if table[fromTupleInt[0]][fromTupleInt[1]][1] == "P":
                data = self.GetMovesFromPawn(fromTupleInt, actualPlayer)
                print data
                return data
            if table[fromTupleInt[0]][fromTupleInt[1]][1] == "H":
                data = self.GetMovesFromHourse(fromTupleInt, actualPlayer)
                print data
                return data
            if table[fromTupleInt[0]][fromTupleInt[1]][1] == "R":
                data = self.GetMovesFromRook(fromTupleInt, actualPlayer)
                print data
                return data
            if table[fromTupleInt[0]][fromTupleInt[1]][1] == "B":
                data =  self.GetMovesFromBishopMoves(fromTupleInt, actualPlayer)
                print data
                return data
            if table[fromTupleInt[0]][fromTupleInt[1]][1] == "Q":
                data =  self.GetMovesFromQueen(fromTupleInt, actualPlayer)
                print data
                return data
            if table[fromTupleInt[0]][fromTupleInt[1]][1] == "K":
                data = self.GetMovesFromKing(fromTupleInt, actualPlayer)
                print data
                return data

    # *******************************************************************************************************************


    def PrintChessTable(self):
        strComplete = "   "
        arr = [0, 1, 2, 3, 4, 5, 6, 7]
        for row in arr:
            print "\n"
            for colum in arr:
                if self.GetTable()[row][colum] == 'e':
                    strComplete = strComplete + self.GetTable()[row][colum] + "(" + self.colL[colum] + str(
                        8 - row) + "),   "
                else:
                    strComplete = strComplete + self.GetTable()[row][colum] + "(" + self.colL[colum] + str(8 - row) + "),  "
            print strComplete
            strComplete = "   "
