

def king(allPieces,piece):
    if piece[0] == 'k':
        possibleMoves = []
        color = piece[1]
        col = int(piece[2])
        row = int(piece[3])
        #cima
        if col+1 < 8:
            if allPieces[col+1][row] == '----':
                possibleMoves.append('k'+color+str(col+1)+str(row))
            elif allPieces[col+1][row][1] != color:
                possibleMoves.append('k'+color+str(col+1)+str(row))
        #cima direita
        if col+1 < 8 and row + 1 < 8:
            if allPieces[col+1][row+1] == '----':
                possibleMoves.append('k'+color+str(col+1)+str(row+1))
            elif allPieces[col+1][row+1][1] != color:
                possibleMoves.append('k'+color+str(col+1)+str(row+1))
        #cima esquerda
        if col+1 < 8 and row -1 >= 0:
            if allPieces[col+1][row-1] == '----':
                possibleMoves.append('k'+color+str(col+1)+str(row-1))
            elif allPieces[col+1][row-1][1] != color:
                possibleMoves.append('k'+color+str(col+1)+str(row-1))
        #direita
        if row+1 < 8:
            if allPieces[col][row+1] == '----':
                possibleMoves.append('k'+color+str(col)+str(row+1))
            elif allPieces[col][row+1][1] != color:
                possibleMoves.append('k'+color+str(col)+str(row+1))
        #esquerda
        if row-1 >= 0:
            if allPieces[col][row-1] == '----':
                possibleMoves.append('k'+color+str(col)+str(row-1))     
            elif allPieces[col][row-1][1] != color:
                possibleMoves.append('k'+color+str(col)+str(row-1))       
        #baixo
        if col-1 >= 0:
            if allPieces[col-1][row] == '----':
                possibleMoves.append('k'+color+str(col-1)+str(row))
            elif allPieces[col-1][row][1] != color:
                possibleMoves.append('k'+color+str(col-1)+str(row))
        #baixo direita
        if col-1 >= 0 and row + 1 < 8:
            if allPieces[col-1][row+1] == '----':
                possibleMoves.append('k'+color+str(col-1)+str(row+1))
            elif allPieces[col-1][row+1][1] != color:
                possibleMoves.append('k'+color+str(col-1)+str(row+1))
        #baixo esquerda
        if col-1 >= 0 and row -1 >= 0:
            if allPieces[col-1][row-1] == '----':
                possibleMoves.append('k'+color+str(col-1)+str(row-1))    
            elif allPieces[col-1][row-1][1] != color:
                possibleMoves.append('k'+color+str(col-1)+str(row-1))        

        return [piece,possibleMoves]

