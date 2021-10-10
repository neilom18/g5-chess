
from main.game.ConvertStringArray import historyToArray
from main.game.verifyCheck import verificarCheck


def especialMove(allpieces,piece,history):
    history = historyToArray(history)
    if history != ['']:
        if piece[0] == 'p':
            return EnPassant(piece,history)
        elif piece[0] == 'k':
            return Castles(allpieces,piece,history)
    

def Castles(allPieces,piece,history):
    rookRightMoved = False
    rookLeftMoved = False
    isMoved = False
    #checa se o rei já se mexeu
    for moved in history:
        if moved:
            if piece[0] == moved[0]:
                if piece[1] == moved[1]:  
                    isMoved = True
    #checa se as torres já se mexeram
    if isMoved == False:
        for rookMoved in history:
            if rookMoved:
                if rookMoved[0] == 'r':
                    if rookMoved[1] == piece[1]:
                        if rookMoved[3]=='7':
                            rookRightMoved = True   
                        elif rookMoved[3] == '0':
                            if rookMoved[1] == piece[1]:
                                rookLeftMoved = True
    myPossibleCastles = ''
    if isMoved == False:
        if rookRightMoved == False:
            if allPieces[int(piece[2])][int(piece[3])+1] == '----':
                if allPieces[int(piece[2])][int(piece[3])+2] == '----':
                    moves = [piece]
                    moves.append(piece[0]+piece[1]+piece[2]+str(int(piece[3])+1))
                    moves.append(piece[0]+piece[1]+piece[2]+str(int(piece[3])+2))
                    realMoves = [piece,moves]
                    movimentosSemCheck = verificarCheck(allPieces,realMoves)
                    if realMoves[1] == movimentosSemCheck[slice(1,4)]:
                        myPossibleCastles = piece[0]+piece[1]+piece[2]+str(int(piece[3])+2)
        if rookLeftMoved == False:
            if allPieces[int(piece[2])][int(piece[3])-1] == '----':
                if allPieces[int(piece[2])][int(piece[3])-2] == '----':
                    if allPieces[int(piece[2])][int(piece[3])-3] == '----':
                        moves = [piece]
                        moves.append(piece[0]+piece[1]+piece[2]+str(int(piece[3])-1))
                        moves.append(piece[0]+piece[1]+piece[2]+str(int(piece[3])-2))
                        realMoves = [piece,moves]
                        movimentosSemCheck = verificarCheck(allPieces,realMoves)
                        if realMoves[1] == movimentosSemCheck[slice(1,4)]:
                            myPossibleCastles += piece[0]+piece[1]+piece[2]+str(int(piece[3])-2)
    return myPossibleCastles


def EnPassant(piece,history):
    lastMove = history[len(history) -2]  #exemplo de resultado pb64pb44
    #checa se o último movimento foi de um peão
    if lastMove[4] == 'p':
        #checa se o peão na casa 6 agora está na casa 4. No caso checa se o peão ao se mover ele mexeu dois quadrados, indicando que era o primeiro movimento dele no jogo. Exemplo pb66 pb46
        if int(lastMove[2]) == int(lastMove[6])+2 or int(lastMove[2]) == int(lastMove[6])-2:
            color = piece[1]
            if color == 'w':
                if piece[2] == '4':
                    return(piece[0]+piece[1]+str(int(lastMove[6])+1)+lastMove[7])
            if color =='b':
                if piece[2] == '3':
                    return(piece[0]+piece[1]+str(int(lastMove[6])-1)+lastMove[7])
