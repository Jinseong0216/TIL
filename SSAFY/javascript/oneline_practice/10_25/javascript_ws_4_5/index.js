class Player {
    constructor() {
        this.choice = ''
        this.winning = 0
        this.draw = 0
    }
}

let player1ImgTag =document.querySelector('#player1-img')
let player2ImgTag =document.querySelector('#player2-img')
let btnTags = document.querySelectorAll('.button-box button')
let imgTags = document.querySelectorAll('.button-box button img')
let rscSrcs = ["./img/scissors.png", "./img/rock.png", "./img/paper.png"]
const player1 = new Player()
const player2 = new Player()


for (const btnTag of btnTags) {
    btnTag.addEventListener('click', function (e) {

        if (this.id === 'scissors-button') {player1.choice = 0}
        if (this.id === 'rock-button') {player1.choice = 1}
        if (this.id === 'paper-button') {player1.choice = 2}
        player1ImgTag.src = rscSrcs[player1.choice]
        onoffButton('off')
        setTimeout(choosePlayer2(), 1000);
    })
}


const onoffButton = function (command) {
    if (command === 'off') {
        for (const btnTag of btnTags) {
            btnTag.disabled = true
        }
    }
    if (command === 'on') {
        for (const btnTag of btnTags) {
            btnTag.disabled = false

        }
    }
}


const choosePlayer2 = function () {
    const changePlayer2Img = setInterval(() => {
        const randomChoice = Math.floor(Math.random() * 10) % 3
        player2ImgTag.src = rscSrcs[randomChoice]}
        , 50)
    
    setTimeout(() => {
        clearInterval(changePlayer2Img)

        if (player2ImgTag.src === rscSrcs[0]) {player2.choice = 0}
        else if (player2ImgTag.src === rscSrcs[1]) {player2.choice = 1}
        else {player2.choice = 2}
        
        const result = [[0, 2, 1], [1, 0, 2], [2, 1, 0]][player1.choice][player2.choice]
        updateResult(result)
    }, 3000)
}		 


const updateResult = function (result) {
    if (result === 0) { player1.winning += 1}
    else if (result === 1 ) { player2.winning += 1}
    else {player1.draw += 1; player2.draw += 1}
    
    const countA = document.querySelector('.countA')
    const countB = document.querySelector('.countB')
    countA.textContent = player1.winning
    countB.textContent = player2.winning

    // 결과 출력
    const resultComment = `Player ${result} wins!`
    const resultNotice = document.querySelector('#result-notice')
    const resultNoticeContent = resultNotice.querySelector('div')
    if (result === 0) {resultNoticeContent.textContent = "It's a tie!"}
    else {resultNoticeContent.textContent = resultComment}
    resultNotice.style.display = 'flex'

    setTimeout(() => {
        resultNotice.style.display = 'none'
        onoffButton('on')
    }, 4000);
} 
