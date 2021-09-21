
start = ' rw00 cw10 bw20 qw30 kw40 bw50 cw60 rw70 pw01 pw11 pw21 pw31 pw41 pw51 pw61 pw71 pb06 pb16 pb26 pb36 pb46 pb56 pb66 pb76 rb07 cb17 bb27 qb37 kb47 bb57 cb67 rb77'

def stringToArray(pieces):
    result = pieces.split()
    return result

piecesArray = stringToArray(start)

singlePiece = piecesArray[0]

print(singlePiece[3])