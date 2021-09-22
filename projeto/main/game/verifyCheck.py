from pieces.pawn import Pawn
from pieces.torre import torre
from pieces.queen import queen
from pieces.king import king
from pieces.cavalo import cavalo
from pieces.bispo import bispo
from game import commands
import ConvertStringArray
start = ' rw00 cw01 bw02 qw03 kw04 bw05 cw06 rw07 pw10 pw11 pw12 pw13 pw14 pw15 pw16 pw17 pb60 pb61 pb62 pb63 pb64 pb65 pb66 pb67 rb70 cb71 bb72 qb73 kb74 bb75 cb76 rb77'


def findKing(allPieces,color):
    king = ''
    for line in allPieces:
        for piece in allPieces:
            print(piece[2])

def verificarCheck(allPieces,Moves):
    print(allPieces)
    findKing(allPieces,'w')
    possibleMoves = []
    for move in Moves:
        tempAllPieces = allPieces
        kingPos = tempAllPieces
        col = int(move[2])
        row = int(move[3])
        color = move[1]
        tempAllPieces[col][row] = move
        for line in tempAllPieces:
            for piece in tempAllPieces:
                piecePossibleMoves = commands[piece[0]](tempAllPieces,piece)
                for pieceMoves in piecePossibleMoves:
                    pass

verificarCheck(ConvertStringArray.stringToArray(start),['pb44'])               
