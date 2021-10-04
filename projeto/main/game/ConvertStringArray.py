
start = ' rw00 cw01 bw02 qw03 kw04 bw05 cw06 rw07 pw10 pw11 pw12 pw13 pw14 pw15 pw16 pw17 pb60 pb61 pb62 pb63 pb64 pb65 pb66 pb67 rb70 cb71 bb72 qb73 kb74 bb75 cb76 rb77'

def historyToArray(history):
    historyArray = history.split(',')
    return historyArray

def arrayToHistory(array):
    history = ''
    for i in array:
        history += i
    return history

def convertColToDisplay(row):
    indices = ['a','b','c','d','e','f','g','h']
    row = int(row)
    return indices[row]
def ArrayToDisplay(pieces):
    newPieces = []
    for piece in pieces:
        if piece != '----':
            print(piece)
            col = int(piece[2])
            row = int(piece[3])
            colDisplay = convertColToDisplay(int(piece[2]))
            rowDisplay = str(int(piece[3])+1)
            newPieces.append(piece[0]+piece[1]+colDisplay+rowDisplay)
    return newPieces

def stringToArray(pieces):
    initialArray = pieces.split()
    piecesArray = [['----' for _ in range(8)] for _ in range(8)]
    for i in initialArray:
        col = int(i[2])
        row = int(i[3])
        piecesArray[col][row] = i
    return piecesArray

def arrayTostring(piecesArray):
    piecesString = ''
    for piece in piecesArray:
            if piece != '----' :
                piecesString += piece + ' '
    return piecesString

def arrayToStringallPieces(piecesArray):
    piecesString = ''
    for line in piecesArray:
        for piece in line:
            if piece != '----':
                piecesString += piece + ' '
    return piecesString

