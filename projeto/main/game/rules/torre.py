
def torre(allPieces,piece):
    possibleMoves = []
    color = piece[1]
    col = int(piece[2])
    row = int(piece[3])
    cont = 1

    #movimenta para cima
    while col+cont < 8:
        if allPieces[col+cont][row] == '----':
            possibleMoves.append('r'+color+str(col+cont)+str(row))
        elif allPieces[col+cont][row][1] != color:
            possibleMoves.append('r'+color+str(col+cont)+str(row))
            break
        else:
            break
        cont += 1

    #movimenta para baixo
    cont = 1   
    while col-cont >= 0:
        if allPieces[col-cont][row] == '----':
            possibleMoves.append('r'+color+str(col-cont)+str(row))
        elif allPieces[col-cont][row][1] != color:
            possibleMoves.append('r'+color+str(col-cont)+str(row))
            break
        else:
            break
        cont += 1
 
    #movimenta para esquerda
    cont = 1   
    while row-cont >= 0:
        if allPieces[col][row-cont] == '----':
            possibleMoves.append('r'+color+str(col)+str(row-cont))
        elif allPieces[col][row-cont][1] != color:
            possibleMoves.append('r'+color+str(col)+str(row-cont))
            break
        else:
            break
        cont += 1
    #movimenta para direita
    cont = 1   
    while row+cont < 8:
        if allPieces[col][row+cont] == '----':
            possibleMoves.append('r'+color+str(col)+str(row+cont))
        elif allPieces[col][row+cont][1] != color:
            possibleMoves.append('r'+color+str(col)+str(row+cont))
            break
        else:
            break
        cont += 1
        return possibleMoves

