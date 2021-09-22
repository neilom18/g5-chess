
from ConvertStringArray import arrayTostring, stringToArray, ArrayToDisplay
from pieces.pawn import Pawn
from pieces.cavalo import cavalo
from pieces.bispo import bispo
from pieces.queen import queen
from pieces.torre import torre
from pieces.king import king


start = ' rw00 cw01 bw02 qw03 kw04 bw05 cw06 rw07 pw10 pw11 pw12 pw13 pw14 pw15 pw16 pw17 pb60 pb61 pb62 pb63 pb64 pb65 pb66 pb67 rb70 cb71 bb72 qb73 kb74 bb75 cb76 rb77'

commands = {
    'p':Pawn,
    'c':cavalo,
    'b':bispo,
    'q':queen,
    'r':torre,
    'k':king
}

teste = stringToArray(start)
teste = commands['k'](teste,'kw01')
teste = ArrayToDisplay(teste)
print(teste)