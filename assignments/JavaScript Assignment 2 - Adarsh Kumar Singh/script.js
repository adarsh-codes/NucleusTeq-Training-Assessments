/*
CODE FOR LOADING ALL THE CATEGORIES FROM THE OPEN TRIVIA DB TO CREATE A DROPDOWN OF CATEGORIES
 */
document.addEventListener("DOMContentLoaded", function () {
  const categoryDropdown = document.getElementById("categorybox");

  fetch("https://opentdb.com/api_category.php")
    .then((response) => response.json())
    .then((data) => {
      const allOption = document.createElement("option");
      allOption.value = "All";
      allOption.textContent = "All";
      categoryDropdown.appendChild(allOption);

      data.trivia_categories.forEach((category) => {
        const option = document.createElement("option");
        option.value = category.id;
        option.textContent = category.name;
        categoryDropdown.appendChild(option);
      });
    })
    .catch((error) => console.error("Error fetching categories:", error));
});

// CODE FOR STARTING THE QUIZ

let currentQuestionIndex = 0;
let questions = [];
let score = 0;
let timer;
let timeLeft = 15;

const optionLabels = ["A", "B", "C", "D"];

async function fun() {
  let category = document.getElementById("categorybox").value;
  let difficulty = document.getElementById("difficultybox").value;

  document.getElementsByClassName("container")[0].style.display = "none";
  document.getElementsByClassName("question-container")[0].style.display =
    "block";

  let apiurl = `https://opentdb.com/api.php?amount=20&category=${category}&difficulty=${difficulty}&type=multiple`;

  if (category == "All" && difficulty == "All") {
    apiurl = `https://opentdb.com/api.php?amount=20&type=multiple`;
  } else if (difficulty == "All") {
    apiurl = `https://opentdb.com/api.php?amount=20&category=${category}&type=multiple`;
  } else if (category == "All") {
    apiurl = `https://opentdb.com/api.php?amount=20&difficulty=${difficulty}&type=multiple`;
  }

  try {
    const res = await fetch(apiurl);
    const data = await res.json();
    questions = data.results;
    showQuestion();
  } catch (error) {
    console.log(error);
    alert("An error occurred while fetching the questions. Please try again.");
  }
}

function showQuestion() {
  resetState();
  let currentQuestion = questions[currentQuestionIndex];
  let questionElement = document.getElementById("question-text");
  let answerButtons = document.getElementById("answer-buttons");
  let scoreDisplay = document.getElementById("score-display");

  questionElement.innerHTML = currentQuestion.question;
  scoreDisplay.innerHTML = `Score: ${score}`;

  let answers = [
    ...currentQuestion.incorrect_answers,
    currentQuestion.correct_answer,
  ];
  answers.sort(() => Math.random() - 0.5);

  answers.forEach((answer, index) => {
    let button = document.createElement("button");
    button.innerHTML = answer;
    button.classList.add("answer-btn");
    button.setAttribute("data-label", optionLabels[index]);
    button.onclick = () => selectAnswer(button, currentQuestion.correct_answer);
    answerButtons.appendChild(button);
  });

  startTimer();
}

function startTimer() {
  clearInterval(timer);
  timeLeft = 15;
  updateTimerUI();

  timer = setInterval(() => {
    timeLeft--;
    updateTimerUI();

    if (timeLeft === 0) {
      clearInterval(timer);
      autoSelectCorrectAnswer();
    }
  }, 1000);
}

function updateTimerUI() {
  document.getElementById("timer").innerText = timeLeft;
  document.getElementById(
    "timer-circle"
  ).style.background = `conic-gradient(#ff0000 ${
    (timeLeft / 15) * 360
  }deg, #ffffff 0deg)`;
}

function autoSelectCorrectAnswer() {
  let correctAnswer = questions[currentQuestionIndex].correct_answer;
  let buttons = document.getElementsByClassName("answer-btn");

  for (let btn of buttons) {
    btn.disabled = true;
    if (btn.innerHTML === correctAnswer) {
      btn.classList.add("correct");
    } else {
      btn.classList.add("wrong");
    }
  }

  document.getElementById("next-btn").style.display = "block";
}

function selectAnswer(button, correctAnswer) {
  clearInterval(timer);

  let feedbackElement = document.getElementById("feedback");
  let isCorrect = button.innerHTML === correctAnswer;

  if (isCorrect) {
    button.classList.add("correct");
    feedbackElement.innerText = "✅ Correct! 🎉";
    feedbackElement.className = "correct";
    score++;
  } else {
    button.classList.add("wrong");
    feedbackElement.innerText = `❌ Wrong! The correct answer was: ${correctAnswer}`;
    feedbackElement.className = "wrong";
  }

  Array.from(document.getElementsByClassName("answer-btn")).forEach((btn) => {
    btn.disabled = true;
    if (btn.innerHTML === correctAnswer) {
      btn.classList.add("correct");
    }
  });

  document.getElementById("next-btn").style.display = "block";
}

function resetState() {
  clearInterval(timer);
  document.getElementById("answer-buttons").innerHTML = "";
  document.getElementById("next-btn").style.display = "none";

  let feedbackElement = document.getElementById("feedback");
  feedbackElement.innerText = "🟡 Select an answer";
  feedbackElement.className = "";
}

function nextQuestion() {
  currentQuestionIndex++;
  if (currentQuestionIndex < questions.length) {
    showQuestion();
  } else {
    showFinalScore();
  }
}

function showFinalScore() {
  document.getElementsByClassName("question-container")[0].innerHTML = `
        <h2>Quiz Completed!</h2>
        <p>Your Final Score: ${score} / ${questions.length}</p>
        <button onclick="location.reload()">Play Again</button>
    `;
}
