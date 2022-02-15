const playerOne = document.getElementById("playerOne")
const playerTwo = document.getElementById("playerTwo")
const reset = document.getElementById("reset")
const select = document.getElementById("playto")
const playerOneDisplay = document.getElementById("p1Display")
const playerTwoDisplay = document.getElementById("p2Display")

let maxScore = 3
let playerOneScore = 0
let playerTwoScore = 0
let isGameOver = false

playerOne.addEventListener("click", function () {
    if (!isGameOver) {
        playerOneScore++;
        if (playerOneScore === maxScore) {
            isGameOver = true
            playerOneDisplay.classList.add("has-text-success")
            playerTwoDisplay.classList.add("has-text-danger")
            playerOne.disabled = true
            playerTwo.disabled = true
        }
        playerOneDisplay.innerText = playerOneScore
    }
})
playerTwo.addEventListener("click", function () {
    if (!isGameOver) {
        playerTwoScore++;
        if (playerTwoScore === maxScore) {
            isGameOver = true
            playerOneDisplay.classList.add("has-text-danger")
            playerTwoDisplay.classList.add("has-text-success")
            playerOne.disabled = true
            playerTwo.disabled = true
        }
        playerTwoDisplay.innerText = playerTwoScore
    }
})
select.addEventListener("change", function () {
    resetfct()
    maxScore = parseInt(select.value)
})

reset.addEventListener("click", resetfct)

function resetfct() {
    isGameOver = false
    playerOneScore = 0
    playerTwoScore = 0
    playerOneDisplay.innerText = 0
    playerTwoDisplay.innerText = 0
    playerOneDisplay.classList.remove("has-text-success", "has-text-danger")
    playerTwoDisplay.classList.remove("has-text-success", "has-text-danger")
    playerOne.disabled = false
    playerTwo.disabled = false
}
