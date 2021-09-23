#Peão está funcional teoricamente e praticamente


# esse start é simualdo não utilizar ele no oficial (possui peças deslocadas)

from ConvertStringArray import arrayTostring, stringToArray


def Pawn(allPieces,piece):
    if piece[0] == 'p':
        possibleMoves = []
        color = piece[1]
        col = int(piece[2]) # y
        row = int(piece[3]) # x

        if color == 'w':
            # movimento coluna + 1
            if col+1 < 8:
                if allPieces[col+1][row] == '----':
                    possibleMoves.append('pw'+str(col+1)+str(row))
            #primeiro movimento pode mover duas casas
            if col == 1:
                if allPieces[col+2][row] == '----':
                    possibleMoves.append('pw'+str(col+2)+str(row))
            #coluna +1 e linha + 1
            if col+1 < 8 and row+1 < 8:
                if allPieces[col+1][row+1] != '----':
                    if allPieces[col+1][row+1][1] == 'b':
                        possibleMoves.append('pw'+str(col+1)+str(row+1))
            #coluna +1 e linha - 1 
            if col+1 >= 0 and row-1 < 8:
                if allPieces[col+1][row-1] != '----':
                    if allPieces[col+1][row-1][1] == 'b':
                        possibleMoves.append('pw'+str(col+1)+str(row-1))



        elif color == 'b':
        #movimento coluna - 1
            if col-1 >= 0:
                if allPieces[col-1][row] == '----':
                    possibleMoves.append('pb'+str(col-1)+str(row))
        #primeiro movimento pode mover duas casas
            if col == 6:
                if allPieces[col-2][row] == '----':
                    possibleMoves.append('pb'+str(col-2)+str(row))
        # coluna -1 e linha +1
            if col-1 >= 0 and row +1 < 8:
                if allPieces[col-1][row+1] != '----':
                    if allPieces[col-1][row+1][1] == 'w':
                        possibleMoves.append('pb'+str(col-1)+str(row+1))
        # coluna -1 e linha -1
            if col-1 >= 0 and row -1 >= 0:
                if allPieces[col-1][row-1] != '----':
                    if allPieces[col-1][row-1][1] == 'w':
                        possibleMoves.append('pb'+str(col-1)+str(row-1))
        return [piece,possibleMoves]



                    

