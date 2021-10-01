
from main.game.verifyCheck import verificarCheck
from main.game.ConvertStringArray import arrayTostring, stringToArray, ArrayToDisplay
from main.game.pieces.pawn import Pawn
from main.game.pieces.cavalo import cavalo
from main.game.pieces.bispo import bispo
from main.game.pieces.queen import queen
from main.game.pieces.torre import torre
from main.game.pieces.king import king
from main.game.especialMoves import especialMove


start = 'rw00 cw01 bw02 qw03 kw04 bw05 cw06 rw07 pw10 pw11 pw12 pw13 pw14 pw15 pw16 pw17 pb60 pb61 pb62 pb63 pb64 pb65 pb66 pb67 rb70 cb71 bb72 qb73 kb74 bb75 cb76 rb77'

commands = {
    'p':Pawn,
    'c':cavalo,
    'b':bispo,
    'q':queen,
    'r':torre,
    'k':king
}

def selectPiece(allPieces,piece,room):
    moves = commands[piece[0]](allPieces,piece)
    checkEspecialmoves = especialMove(allPieces,piece,room.history)
    moves = verificarCheck(allPieces,moves)
    moves = arrayTostring(moves)
    if checkEspecialmoves:
        moves = moves + checkEspecialmoves
    return moves
#pega as posições antes de se movimentar

