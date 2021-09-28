let squares = document.querySelectorAll('.quadrado')
const roomName = JSON.parse(document.getElementById('room-name').textContent);
const chatButton = document.querySelector('#chat-message-submit')
const startoooloo = 'rw00 cw01 bw02 qw03 kw04 bw05 cw06 rw07 pw10 pw11 pw12 pw13 pw14 pw15 pw16 pw17 pb60 pb61 pb62 pb63 pb64 pb65 pb66 pb67 rb70 cb71 bb72 qb73 kb74 bb75 cb76 rb77'

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
        document.querySelector("#chat-log").value += (data.message + '\n')
    }
    // verficia se tem alguma função startgame que vai ir ao nosso usuario
    if(data.startGame){
        drawPiecesStart(data.startGame)
    }
    // se não tiver movimentos apenas desenha a peça selecionada
    if(data.piece){
        const piece = data.piece
        const pieceCoord = piece[2]+piece[3]
        squares.map((square) =>{
            if(square.dataset.id == pieceCoord){
                square.classList.add('selected')
                window.addEventListener('click',selectedPieceRemoveColor)
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
        // pega a peça que sera movida
        document.querySelector(`[data-piece="${initialPos}"]`).remove()
        const squareToMove = document.querySelector(`[data-id="${finalPos[2]}${finalPos[3]}"]`)
        squareToMove.innerHTML = `<img class='square' src='../../main/static/imagens/piece/${finalPos[0]}${finalPos[1]}.png' data-piece="${finalPos}" onclick="selectPiece(this)">`

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
webSocket.onopen =  (e) => {
    webSocket.send(JSON.stringify({
        'command':'start_game'
    }))
}
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
    'message': message
    }));
    messageInputDom.value = '';
};



function drawPiecesStart(allPieces){
    yourColor = 'w'
    allPiecesArray = allPieces.split(' ')
    for (let i = 0; i<allPiecesArray.length;i++){
        const piece = allPiecesArray[i]
        var color
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
    webSocket.send(JSON.stringify({
        'command':'select_piece',
        'piece':e.dataset.piece
    }))
}