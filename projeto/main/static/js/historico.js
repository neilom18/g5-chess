

let allGames = document.querySelectorAll('.singleGame')

allGames = Array.from(allGames)

allGames = allGames.map((item) => {
    let singleGame = item.textContent.split(' ')
    let gameArray = 'error'
    singleGame.filter((item) => {
        if (item !== '' && item!== ' ' && item!== '\n'){
            gameArray = item.slice(0,item.length-1).split(',')
        }
    })
    return gameArray
})

console.log(allGames)
lista = document.querySelector('.lista');
let partida;
let testeMaior = allGames
let squares = document.querySelectorAll('.quadrado');
let rButton = document.querySelector('.pogresso');
let lButton = document.querySelector('.retrocesso');
const allPieces = 'rw00 cw01 bw02 qw03 kw04 bw05 cw06 rw07 pw10 pw11 pw12 pw13 pw14 pw15 pw16 pw17 pb60 pb61 pb62 pb63 pb64 pb65 pb66 pb67 rb70 cb71 bb72 qb73 kb74 bb75 cb76 rb77'

function drawPiecesStart(allPieces){
    allPiecesArray = allPieces.split(' ')
    for (let i = 0; i<allPiecesArray.length;i++){
        const piece = allPiecesArray[i]
        // apenas para inverter as cores no front já que os números acabam invertidos
        pieceCoord = piece[2]+piece[3]
        squares = Array.from(squares)
        squares.map((square) => {
            if(square.dataset.id == pieceCoord){
                square.innerHTML = `<img class='square' src='../../main/static/imagens/piece/${piece[0]}${piece[1]}.png' data-piece="${piece}">`
                return;
            }
            return;
        })
    }
}
// Cria a lista de partidas
let code;
listaPartidas =  testeMaior.map((item) => {
    code = item.length - 1
    return `<a class="partidas" href='#' data-id="${item[code]}">
    </a>`   
}).join('')
lista.innerHTML = listaPartidas;
for(let i = 0; i < testeMaior.length;i++){
    let partidaUnica = testeMaior[i]
    code = partidaUnica.length - 1;
    if(partidaUnica[2] === 'b'){
        partidaUnica[2] = 'Preto Ganhou'
    }else{
        partidaUnica[2] = 'Branco Ganhou'
    }
    for(let j = 0; j < 3;j++){
        if(j == 0){
            document.querySelector(`[data-id="${partidaUnica[code]}"]`).innerHTML += `<h4>${partidaUnica[j]}<span class='branco'> 0</span></h4>` 
        }else if(j == 1){
            document.querySelector(`[data-id="${partidaUnica[code]}"]`).innerHTML += `<h4>${partidaUnica[j]}<box class='preto'>   0</box></h4>`
        }else{
            document.querySelector(`[data-id="${partidaUnica[code]}"]`).innerHTML += `<h4>${partidaUnica[j]}</h4>`
        }
    }
}
partida = document.querySelectorAll('.partidas');
lista.onmouseover = function(e){
    let count = 4;
    for(let count99 = 0; count99 < testeMaior.length;count99++){
        partida[count99].onclick = function(e){
            drawPiecesStart(allPieces);
            let chat = document.querySelector('#chat-log');
            let allPositions = testeMaior[count99].slice(4,8)
            console.log(allPositions)
            //função para avançar as jogadas
            rButton.onclick = function(e){
                let tamanho = testeMaior[count99].length - 1;
                if(tamanho > count){
                    let positions = testeMaior[count99][count];
                    finalPos = positions.slice(4,8)
                    initialPos = positions.slice(0,4);
                    document.querySelector(`[data-piece="${initialPos}"]`).remove()
                    const squareToMove = document.querySelector(`[data-id="${finalPos[2]}${finalPos[3]}"]`)
                    squareToMove.innerHTML = `<img class='square' src='../../main/static/imagens/piece/${finalPos[0]}${finalPos[1]}.png' data-piece="${finalPos}">`
                    count = count + 1
                }
            }
            chat.textContent = allPositions
            console.log(chat.textContent)
            let initialPos = '';
            let finalPos = '';
            // Função para voltar as jogadas
            lButton.onclick = function(e){
                tamanho = 4;
                if(tamanho < count){
                    count = count - 1
                    let positions = testeMaior[count99][count]
                    finalPos = positions.slice(4,8);
                    initialPos = positions.slice(0,4);
                    document.querySelector(`[data-piece="${finalPos}"]`).remove()
                    const squareToMove = document.querySelector(`[data-id="${initialPos[2]}${initialPos[3]}"]`)
                    squareToMove.innerHTML = `<img class='square' src='../../main/static/imagens/piece/${initialPos[0]}${initialPos[1]}.png' data-piece="${initialPos}">`
                }
            }
        }
    }
}

