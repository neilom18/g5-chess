
const roomName = JSON.parse(document.getElementById('room-name').textContent);
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
    document.querySelector('#chat-log').value += (data.message + '\n');
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
        'message': message
    }));
    messageInputDom.value = '';
};