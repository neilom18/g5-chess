
example = 'bw14'
def bispo(allPieces,piece):
     if piece[0] == 'b':
        possibleMoves = []
        color = piece[1]
        col = int(piece[2])
        row = int(piece[3])
        cont = 1
        #direita pra cima
        while col+cont < 8 and row+cont < 8:
            if allPieces[col+cont][row+cont] == '----':
                possibleMoves.append('b'+color+str(col+cont)+str(row+cont))
            elif allPieces[col+cont][row+cont][1] != color:
                possibleMoves.append('b'+color+str(col+cont)+str(row+cont))
                break
            else:
                break
            cont += 1

        #esquerda pra cima
        #reseta o valor de cont
        cont = 1
        while col+cont < 8 and row-cont >= 0:
            if allPieces[col+cont][row-cont] == '----':
                possibleMoves.append('b'+color+str(col+cont)+str(row-cont))
            elif allPieces[col+cont][row-cont][1] != color:
                possibleMoves.append('b'+color+str(col+cont)+str(row-cont))
                break
            else:
                break
            cont+= 1
        #esquerda para baixo
        #reseta o valor de cont
        cont = 1
        while col-cont >= 0 and row-cont >= 0:
            if allPieces[col-cont][row-cont] == '----':
                possibleMoves.append('b'+color+str(col-cont)+str(row-cont))
            elif allPieces[col-cont][row-cont][1] != color:
                possibleMoves.append('b'+color+str(col-cont)+str(row-cont))
                break
            else:
                break
            cont+= 1
        #direita para baixo
        #reseta o valor de cont
        cont = 1
        while col-cont >= 0 and row+cont <8:
            if allPieces[col-cont][row+cont] == '----':
                possibleMoves.append('b'+color+str(col-cont)+str(row+cont))
            elif allPieces[col-cont][row+cont][1] != color:
                possibleMoves.append('b'+color+str(col-cont)+str(row+cont))
                break
            else:
                break
            cont+= 1

        return possibleMoves



