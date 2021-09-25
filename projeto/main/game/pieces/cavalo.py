
def cavalo(allPieces,piece):
    if piece[0] == 'c':
        possibleMoves = []
        color = piece[1]
        col = int(piece[2]) # y
        row = int(piece[3]) # x

        if col+1 < 8 and row+2 < 8:
            if allPieces[col+1][row+2] == '----':
                possibleMoves.append('c'+color+str(col+1)+str(row+2))
        if col+1 < 8 and row-2 >= 0:
            if allPieces[col+1][row-2] == '----':
                possibleMoves.append('c'+color+str(col+1)+str(row-2))
        if col-1 >= 0 and row+2 < 8:
            if allPieces[col-1][row+2] == '----':
                possibleMoves.append('c'+color+str(col-1)+str(row+2))
        if col-1 >= 0 and row-2 >= 0:
            if allPieces[col-1][row-2] == '----':
                possibleMoves.append('c'+color+str(col-1)+str(row-2))
        if col+2 < 8 and row+1 < 8:
            if allPieces[col+2][row+1] == '----':
                possibleMoves.append('c'+color+str(col+2)+str(row+1))
        if col+2 < 8 and row-1 >= 0:
            if allPieces[col+2][row-1] == '----':
                possibleMoves.append('c'+color+str(col+2)+str(row-1))
        if col-2 >= 0 and row+1 < 8:
            if allPieces[col-2][row+1] == '----':
                possibleMoves.append('c'+color+str(col-2)+str(row+1))
        if col-2 >= 0 and row-1 >= 0:
            if allPieces[col-2][row-1] == '----':
                possibleMoves.append('c'+color+str(col-2)+str(row-1))

        if col+1 < 8 and row+2 < 8:
            if allPieces[col+1][row+2] != '----':
                if allPieces[col+1][row+2][1] != color:
                    possibleMoves.append('c'+color+str(col+1)+str(row+2))
        if col+1 < 8 and row-2 >= 0:
            if allPieces[col+1][row-2] != '----':
                if allPieces[col+1][row-2][1] != color:
                    possibleMoves.append('c'+color+str(col+1)+str(row-2))
        if col-1 >= 0 and row+2 < 8:
            if allPieces[col-1][row+2] != '----':
                if allPieces[col-1][row+2][1] != color:
                    possibleMoves.append('c'+color+str(col-1)+str(row+2))
        if col-1 >= 0 and row-2 >= 0:
            if allPieces[col-1][row-2] != '----':
                if allPieces[col-1][row-2][1] != color:
                    possibleMoves.append('c'+color+str(col-1)+str(row-2))
        if col+2 < 8 and row+1 < 8:
            if allPieces[col+2][row+1] != '----':
             if allPieces[col+2][row+1][1] != color:
                possibleMoves.append('c'+color+str(col+2)+str(row+1))
        if col+2 < 8 and row-1 >= 0:
            if allPieces[col+2][row-1] != '----':
                if allPieces[col+2][row-1][1] != color:
                    possibleMoves.append('c'+color+str(col+2)+str(row-1))
        if col-2 >= 0 and row+1 < 8:
            if allPieces[col-2][row+1] != '----':
                if allPieces[col-2][row+1][1] != color:
                 possibleMoves.append('c'+color+str(col-2)+str(row+1))
        if col-2 >= 0 and row-1 >= 0:
            if allPieces[col-2][row-1] != '----':
                if allPieces[col-2][row-1][1] != color:
                 possibleMoves.append('c'+color+str(col-2)+str(row-1))
        return [piece,possibleMoves]

