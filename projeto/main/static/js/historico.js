teste = ['testinho','testinho2','520','510','pw14pw34','pb65pb45','pw13pw33','pb66pb46','qw03qw47','asdfwq']
let squares = document.querySelectorAll('.quadrado');
let rButton = document.querySelector('.pogresso');
let lButton = document.querySelector('.retrocesso')
let count = 4; 
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
drawPiecesStart(allPieces);
let initialPos;
let finalPos;
rButton.onclick = function(e){
    let tamanho = teste.length - 1;
    if(tamanho > count){
        let positions = teste[count]
        finalPos = positions.slice(4,8)
        initialPos = positions.slice(0,4);
        document.querySelector(`[data-piece="${initialPos}"]`).remove()
        const squareToMove = document.querySelector(`[data-id="${finalPos[2]}${finalPos[3]}"]`)
        squareToMove.innerHTML = `<img class='square' src='../../main/static/imagens/piece/${finalPos[0]}${finalPos[1]}.png' data-piece="${finalPos}">`
        count = count + 1
    }
}
lButton.onclick = function(e){
    tamanho = 4
    if(tamanho < count){
        count = count - 1
        let positions = teste[count]
        finalPos = positions.slice(4,8)
        initialPos = positions.slice(0,4);
        document.querySelector(`[data-piece="${finalPos}"]`).remove()
        const squareToMove = document.querySelector(`[data-id="${initialPos[2]}${initialPos[3]}"]`)
        squareToMove.innerHTML = `<img class='square' src='../../main/static/imagens/piece/${initialPos[0]}${initialPos[1]}.png' data-piece="${initialPos}">`
    }
}