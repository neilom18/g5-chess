
from ConvertStringArray import arrayTostring, stringToArray
from rules.pawn import Pawn



start = ' rw00 cw01 bw02 qw03 kw04 bw05 cw06 rw07 pw10 pw11 pw12 pw13 pw14 pw15 pw16 pw17 pb60 pb61 pb62 pb63 pb64 pb65 pb66 pb67 rb70 cb71 bb72 qb73 kb74 bb75 cb76 rb77'

commands = {
    'p':Pawn
}

print(commands['p'](stringToArray(start),'pw11'))