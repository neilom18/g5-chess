let squares = document.querySelectorAll('.quadrado')
const chatButton = document.querySelector("#chat-message-input")
const roomName = JSON.parse(document.getElementById('room-name').textContent);
const aviso = document.querySelector('.aviso').textContent;
const startoooloo = 'rw00 cw01 bw02 qw03 kw04 bw05 cw06 rw07 pw10 pw11 pw12 pw13 pw14 pw15 pw16 pw17 pb60 pb61 pb62 pb63 pb64 pb65 pb66 pb67 rb70 cb71 bb72 qb73 kb74 bb75 cb76 rb77'
let yourColor = ''
const webSocket = new WebSocket(
    'ws://'
    +window.location.host
    +'/ws/room/'
    +roomName
    +'/'
)


const receiveMessage = (e) => {
    const data = JSON.parse(e.data)

    // verifica se existe uma mensagem e atribui ao nosso chat log
    if(data.message){
        console.log(data)
        if(data.usuario){
        document.querySelector("#chat-log").value += (data.usuario + ': ' + data.message + '\n')}

    }
    if(data.user1){ 
        document.querySelector('.user1').textContent = data.user1
    }
    if(data.user2){
        document.querySelector('.user2').textContent = data.user2
        document.querySelector('.versus').textContent = (data.user1 + ' VS ' + data.user2)
        if(aviso){
        document.querySelector('.aviso').remove()}
    }    
    // verficia se tem alguma função startgame que vai ir ao nosso usuario
    if(data.startGame){
        yourColor = data.userColor
        if(yourColor == "w"){
            document.querySelector("#chat-log").value += ('você está logado como: '+data.user1 + '\n')
        }else{
        document.querySelector("#chat-log").value += ('você está logado como: ' + data.user2 + '\n')}
        drawPiecesStart(data.startGame)
    }
    // se não tiver movimentos apenas desenha a peça selecionada
    if(data.piece){
        const piece = data.piece
        const pieceCoord = piece[2]+piece[3]
        squares.map((square) =>{
            if(square.dataset.id == pieceCoord){
                square.classList.add('selected')
                window.addEventListener('click',selectedPieceFunction)
            }
        }) 
    }
    // desenha os possíveis movimentos na tela
    if(data.moves){
        pieceData = data.moves.split(' ')
        const piece = pieceData[0]
        const pieceCoord = piece[2]+piece[3]
        const moves = [...pieceData.slice(1)]
        squares.map((square) => {
            if(square.dataset.id == pieceCoord){
                square.classList.add('selected')
                window.addEventListener('click',selectedPieceFunction)
            }
            //  ve os quadrados que são selecionados que não são a peça a se movimentar
            moves.map((move) => {
                moveCoord = move[2]+move[3]
                if(square.dataset.id == moveCoord){
                    square.classList.add('selectedSquare')
                }
            } )
        })
    }
    // move a peça no front baseado na info do back
    if (data.movePiece){
        positions = data.movePiece
        initialPos = positions[0]
        finalPos = positions[1]
        player = finalPos[1]
        timer(player)
        // pega a peça que sera movida
        document.querySelector(`[data-piece="${initialPos}"]`).remove()
        const squareToMove = document.querySelector(`[data-id="${finalPos[2]}${finalPos[3]}"]`)
        squareToMove.innerHTML = `<img class='square' src='../../main/static/imagens/piece/${finalPos[0]}${finalPos[1]}.png' data-piece="${finalPos}" onclick="selectPiece(this)">`
    }
    if (data.enPassant){
        positions = data.enPassant
        initialPos = positions[0]
        finalPos = positions[1]
        otherPiecePos = positions[2]
        // pega a peça que sera movida
        document.querySelector(`[data-piece="${otherPiecePos}"]`).remove()
        document.querySelector(`[data-piece="${initialPos}"]`).remove()
        const squareToMove = document.querySelector(`[data-id="${finalPos[2]}${finalPos[3]}"]`)
        squareToMove.innerHTML = `<img class='square' src='../../main/static/imagens/piece/${finalPos[0]}${finalPos[1]}.png' data-piece="${finalPos}" onclick="selectPiece(this)">`
    }
    // executa o movimento do castles(roque)
    if (data.castles){
        kingInitialPos = data.castles[0]
        kingFinalPos = data.castles[1]
        rookInitialPos = data.castles[2]
        rookFinalPos = data.castles[3]
        document.querySelector(`[data-piece="${kingInitialPos}"]`).remove()
        document.querySelector(`[data-piece="${rookInitialPos}"]`).remove()
        const squareTomove1 = document.querySelector(`[data-id="${kingFinalPos[2]}${kingFinalPos[3]}"]`)
        const squareTomove2 = document.querySelector(`[data-id="${rookFinalPos[2]}${rookFinalPos[3]}"]`)
        squareTomove1.innerHTML = `<img class='square' src='../../main/static/imagens/piece/${kingFinalPos[0]}${kingFinalPos[1]}.png' data-piece="${kingFinalPos}" onclick="selectPiece(this)">`
        squareTomove2.innerHTML = `<img class='square' src='../../main/static/imagens/piece/${rookFinalPos[0]}${rookFinalPos[1]}.png' data-piece="${rookFinalPos}" onclick="selectPiece(this)">`
    }
    if(data.gameEnd){
        document.querySelector('.termino').classList.add('display');
        if(yourColor === data.whoLost){
            document.querySelector('#mensagem').textContent = 'Você Perdeu';
        }else{
            document.querySelector('#mensagem').textContent = 'Você Ganhou';
        }
        window.clearInterval(timerId)
    }
}
const selectedPieceFunction = (e) => {
    if (e.target.classList.contains('selectedSquare')){
        move = document.querySelector('.selected').firstElementChild.dataset.piece
        move = move +' '+move[0]+move[1]+e.target.dataset.id
        webSocket.send(JSON.stringify({
            'command':'move_piece',
            'move':move
        }))
    }
    else if (e.target.parentElement.classList.contains('selectedSquare')){
        move = document.querySelector('.selected').firstElementChild.dataset.piece
        move = move +' '+move[0]+move[1]+e.target.parentElement.dataset.id
        webSocket.send(JSON.stringify({
            'command':'move_piece',
            'move':move
        }))
    }
    // remove a seleção da peça
    document.querySelector('.selected').classList.remove('selected')
    // remove a seleção do quadrado
    document.querySelectorAll('.selectedSquare').forEach((square) => {
        square.classList.remove('selectedSquare')
    })
    // remove o event listener pra que não fique cheio de eventlisteners e de um crash no browser e também pra não bugar o jogo
    window.removeEventListener('click',selectedPieceFunction)
}
webSocket.onclose = function(e){
    console.error('Chat socket closed unexpectedly')
}
webSocket.onmessage = receiveMessage

// envia a informação de que eu entrei

// enviar mensagem com o enter
chatButton.focus()
chatButton.onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        chatButton.click()
    }
}
chatButton.onclick = function(e){
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;
    webSocket.send(JSON.stringify({    
    'command':'chat_message',
    'message': message,
    }));
    messageInputDom.value = '';
};



function drawPiecesStart(allPieces){
    allPiecesArray = allPieces.split(' ')
    for (let i = 0; i<allPiecesArray.length;i++){
        const piece = allPiecesArray[i]
        // apenas para inverter as cores no front já que os números acabam invertidos
        pieceCoord = piece[2]+piece[3]
        squares = Array.from(squares)
        squares.map((square) => {
            if(square.dataset.id == pieceCoord){
                square.innerHTML = `<img class='square' src='../../main/static/imagens/piece/${piece[0]}${piece[1]}.png' data-piece="${piece}" ${piece[1]==yourColor? `onclick="selectPiece(this)"`:''}>`
                return;
            }
            return;
        })
    }
}
function selectPiece(e){
    if(e.dataset.piece[1] == yourColor)
    webSocket.send(JSON.stringify({
        'command':'select_piece',
        'piece':e.dataset.piece
    }))
}

// CHESS CLOCK 
let timerId;
let count1 = 10;
let count2 = 10;
let tempo1 = 600;
let tempo2 = 600;
let min1 = Math.floor(tempo1 / 60);
let min2 = Math.floor(tempo2 / 60);
let sec1 = tempo1 % 60;
let sec2 = tempo2 % 60;
let timer1 = document.querySelector('.timer1');
let timer2 = document.querySelector('.timer2');
function timer(player){
    if(timerId){
        clearInterval(timerId)
    }
    timerId = setInterval(() => {  
        if (player == 'b'){
            if(count1 == 10){
                if(sec1 == 0){
                    min1 = min1 - 1
                    sec1 = 60;
                }
                sec1 = sec1 - 1
                count1 = 0;
            }
            // Verifica se o tempo acabou
            if (sec1 == 0 && min1 == 0) {
                clearInterval(timerId);
            }
            strMin1 = min1.toString();
            strSec1 = sec1.toString();
            timer1.textContent = strMin1 + ':' + strSec1
            count1 = count1 + 1;
        }
        else{
            if(count2 == 10){
                if(sec2 == 0){
                    min2 = min2 - 1
                    sec2 = 60;
                }
                sec2 = sec2 - 1
                count2 = 0;
            }
            // Verifica se o tempo acabou
            if (sec2 == 0 && min2 == 0) {
                clearInterval(timerId);
            }
            strMin2 = min2.toString();
            strSec2 = sec2.toString();
            timer2.textContent = strMin2 + ':' + strSec2
            count2 = count2 + 1
        }
        if (min1 <= 0 && sec1 <= 0){
            webSocket.send(JSON.stringify({    
                'command':'timer_end'
                }));
        }
        if (min2 <= 0 && sec2 <= 0){
            webSocket.send(JSON.stringify({    
                'command':'timer_end'
                }));
        }

    }, 100); // Executa a cada (100 milliseconds = 1 second).
}
