var socket = new WebSocket('ws://localhost:8000/ws/room/')

socket.onmessage = function(e){
    var djangoData = JSON.parse(e.data)
    console.log(djangoData)
    showValue = document.querySelector("#teste")
    showValue.innerText = djangoData.value
}