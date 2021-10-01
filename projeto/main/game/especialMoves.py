from main.game.ConvertStringArray import historyToArray



def especialMove(allpieces,piece,history):
    history = historyToArray(history)
    print(history)  
    if history != ['']:
        if piece[0] == 'p':
            return EnPassant(piece,history)
    

def EnPassant(piece,history):
    print(history)
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


