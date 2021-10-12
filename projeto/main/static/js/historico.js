teste = document.querySelectorAll('.singleGame')

teste2 = Array.from(teste)


teste2.map((item) => {
    teste3 = item.textContent.split(' ')
    console.log(teste3)
    teste3 = teste3.filter((item) => {
        if (item !== ''  && item!== ' ' && item !== ',' && item !== '\n'){
            return item
        }
    })
    console.log(teste3)
})