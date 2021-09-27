let squares = document.querySelectorAll('.quadrado')
const roomName = JSON.parse(document.getElementById('room-name').textContent);
const startoooloo = 'rw00 cw01 bw02 qw03 kw04 bw05 cw06 rw07 pw10 pw11 pw12 pw13 pw14 pw15 pw16 pw17 pb60 pb61 pb62 pb63 pb64 pb65 pb66 pb67 rb70 cb71 bb72 qb73 kb74 bb75 cb76 rb77'
// cria o webscoket
const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/room/'
    + roomName
    + '/'
);
// recebe a mensagem do websocket
chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    if(data.message){
        document.querySelector('#chat-log').value += (data.message + '\n');

    }
    if(data.piece){
        drawPieces(startoooloo)
    }
    else{
        console.log(data)
    }
};
// informa quando é desconectado do websocket

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};



// função para o enter do teclado
document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#chat-message-submit').click();
    }
};
// função para enviar informação do websocket
document.querySelector('#chat-message-submit').onclick = function(e) {
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;
    chatSocket.send(JSON.stringify({    
        'command':'select_piece',
        'message': message
    }));
    messageInputDom.value = '';
};

function drawPieces(allPieces){
    allPiecesArray = allPieces.split(' ')
    for (let i = 0; i<allPiecesArray.length;i++){
        const piece = allPiecesArray[i]
        pieceCoord = piece[2]+piece[3]
        squares = Array.from(squares)
        squares.map((square) => {
            if(square.dataset.id == pieceCoord){
                square.innerHTML = `<img class='square' src='./pecas/${piece[0]}${piece[1]}'>`
                return;
            }
            return;
        })
    }
}