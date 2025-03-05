let scores = [0, 0];
let currentScore = 0;
let activePlayer = 0;
const diceFaces = ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"];
function rollDice() {
    let diceElement = document.getElementById("dice");
    
    diceElement.classList.add("rotate");
    
    setTimeout(() => {
        let roll = Math.floor(Math.random() * 6) + 1;
        diceElement.textContent = diceFaces[roll - 1];
        diceElement.classList.remove("rotate");

        if (roll === 1) {
            currentScore = 0;
            switchPlayer();
        } else {
            currentScore += roll;
        }
        document.getElementById("currentScore").textContent = currentScore;
    }, 500);
}

function saveScore() {
    scores[activePlayer] += currentScore;
    currentScore = 0;
    document.getElementById("score1").textContent = `${document.getElementById("player1").value}: ${scores[0]}`;
    document.getElementById("score2").textContent = `${document.getElementById("player2").value}: ${scores[1]}`;

    if (scores[activePlayer] >= 100) {
        document.getElementById("winner").textContent = `${document.getElementById(`player${activePlayer + 1}`).value} Wins!`;
        return;
    }
    switchPlayer();
}

function switchPlayer() {
    activePlayer = activePlayer === 0 ? 1 : 0;
    document.getElementById("currentPlayer").textContent = document.getElementById(`player${activePlayer + 1}`).value;
    document.getElementById("currentScore").textContent = 0;
}

function resetGame() {
    scores = [0, 0];
    currentScore = 0;
    activePlayer = 0;
    document.getElementById("score1").textContent = "Player 1: 0";
    document.getElementById("score2").textContent = "Player 2: 0";
    document.getElementById("currentScore").textContent = 0;
    document.getElementById("dice").textContent = "\u{1F3B2}"; 
    document.getElementById("winner").textContent = "";
    document.getElementById("currentPlayer").textContent = "Player 1";
}

