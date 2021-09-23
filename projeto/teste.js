const board = document.querySelector(".board");
const boardletters=document.querySelector(".letters");
const boardnumbers= document.querySelector(".numbers");
let letters = ["a", "b", "c", "d", "e", "f", "g","h"];
let index = 0;
let black = false;
let num = 1;

for (let i = 0; i<8; i++) {
    let letter = document.createElement("li");
    letter.textContent = letters[i]
    boardletters.appendChild(letter);
    let numbers = document.createElement("li");
    numbers.textContent = num++;
    boardnumbers.appendChild(numbers);
}


let lista = []
for (let i = 0; i < 8; i++) {
    for (let j = 0; j < 8; j++){
        lista.push([i,j,black? 'black':'white'])
        black = !black
        if (j === 7) {
            black = !black;
        }
    }
}
teste = lista.map((item) => {
    return `<div class="square ${item[2]}"data-id="${item[0]}${item[1]}">
    </div>`
}).join('')
board.innerHTML = teste