const board = document.querySelector(".board");
const boardletters=document.querySelector(".letters");
const boardnumbers= document.querySelector(".numbers");
let letters = ["a", "b", "c", "d", "e", "f", "g","h"];
let index = 0;
let black = false;
let num = 1;
const start = 'rw00 cw01 bw02 qw03 kw04 bw05 cw06 rw07 pw10 pw11 pw12 pw13 pw14 pw15 pw16 pw17 pb60 pb61 pb62 pb63 pb64 pb65 pb66 pb67 rb70 cb71 bb72 qb73 kb74 bb75 cb76 rb77'

// Transforma string em array
function Pecas(){
    let peca = []
    let listaPecas = []
    listaPecas = start.split(' ')
    for(let i=0; i<listaPecas.length;i++){
        peca.push(listaPecas[i][0])
    }
    return peca
}
let pecas = Pecas()
// Cria os numero da lateral do tabuleiro
for (let i = 0; i<8; i++) {
    let letter = document.createElement("li");
    letter.textContent = letters[i]
    boardletters.appendChild(letter);
    let numbers = document.createElement("li");
    numbers.textContent = num++;
    boardnumbers.appendChild(numbers);
}


let lista = []
// Cria um array com informações de cada quadrado do tabuleiro
for (let i = 0; i < 8; i++) {
    for (let j = 0; j < 8; j++){
        if (i > 1 && i < 6){
            lista.push(['-',i,j,black? 'black':'white'])
        }else{
            lista.push([pecas[index],i,j,black? 'black':'white'])
            index++
        }
        black = !black
        if (j === 7) {
            black = !black;
        }
    }
}
// Display do tabuleiro
tabuleiro = lista.map((item) => {
        return `<div class="quadrado square ${item[3]}"data-id="${item[1]}${item[2]}">
        </div>`
    
}).join('')
board.innerHTML = tabuleiro

