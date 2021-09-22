
start = ' rw00 cw01 bw02 qw03 kw04 bw05 cw06 rw07 pw10 pw11 pw12 pw13 pw14 pw15 pw16 pw17 pb60 pb61 pb62 pb63 pb64 pb65 pb66 pb67 rb70 cb71 bb72 qb73 kb74 bb75 cb76 rb77'

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
    for pieceCol in piecesArray:
        for piece in pieceCol:
            if piece != '----' :
                piecesString += piece + ' '
    return piecesString

