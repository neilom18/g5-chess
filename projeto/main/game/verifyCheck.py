from main.game.pieces.pawn import Pawn
from main.game.pieces.torre import torre
from main.game.pieces.queen import queen
from main.game.pieces.king import king
from main.game.pieces.cavalo import cavalo
from main.game.pieces.bispo import bispo
from main.game.ConvertStringArray import arrayTostring,stringToArray,arrayToStringallPieces

def findKing(allPieces,color):
    king = ''
    for line in allPieces:
        for piece in line:
            if piece != '----':
                if piece[0] == 'k':
                    if piece[1] == color:
                        king = piece
                        return king


def passarArray(array):
    return array.copy()
def verificarCheck(allPieces,Moves):
    #vai retornar os movimentos realmente possíveis que não vão te deixar em cheque
    possibleMoves = [Moves[0]]

    commands = {
    'p':Pawn,
    'c':cavalo,
    'b':bispo,
    'q':queen,
    'r':torre,
    'k':king
    }
    #checa a posição do rei
    kingPos = findKing(allPieces,Moves[0][1])
    #checa cada movimento pra ver se é possível realizar
    for move in Moves[1]:
        #booleana que define se está em cheque
        cheque = False
        tempAllPieces = arrayToStringallPieces(allPieces) # cria uma variavel temporaria pra não alterar direto na original
        tempAllPieces = stringToArray(tempAllPieces)
        col = int(move[2])
        row = int(move[3])
        color = move[1]
        # retira a peça na posição antiga dela
        tempAllPieces[int(Moves[0][2])][int(Moves[0][3])] = '----'
         # recebe o movimento que pode ou não ser executado no final dependendo se o rei entra em cheque
        tempAllPieces[col][row] = move

        # se eu estiver movimentando o rei a posição do meu rei muda então preciso rechecar se ele fica em cheque
        if move[0] == 'k':
            kingPos = findKing(tempAllPieces,move[1])
        #verifica a linha da matriz
        for line in tempAllPieces:
            #verifica a peça da linha
            for piece in line:
                # verifica se a peça existe
                if piece != '----':
                    #verifica a cor da peça
                    if piece[1] != color:
                        piecePossibleMoves = commands[piece[0]](tempAllPieces,piece)
                        if piecePossibleMoves:
                            for pieceMove in piecePossibleMoves[1]:
                                if pieceMove[2] == kingPos[2]:
                                    if pieceMove[3] == kingPos[3]:
                                        cheque = True
        if cheque == False:
            possibleMoves.append(move)
    return possibleMoves

