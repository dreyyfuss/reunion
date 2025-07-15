// static/js/quiz.js
document.addEventListener('DOMContentLoaded', function() {
    const quiz = [
        {
          question: "__________ Plus Plus. Which trainee did this comment refer to?",
          options: ["Aliyu S", "Martins A", "John U", "John E"],
          answer: "Aliyu S"
        },
        {
          question: "Which of these SITP trainee was always around the REC centre?",
          options: ["Ifeanyi N", "Femi A", "Uche O", "Suka B"],
          answer: "Ifeanyi N"
        },
        {
          question: "Who is popularly know as the 'Governor'?",
          options: ["Gideon G", "Jolomi E", "Chidi O", "Amaka K"],
          answer: "Chidi O"
        },
        {
          question: "__________ is a monster. Which trainee did this comment refer to?",
          options: ["Aliyu S", "Martins A", "Niyi O", "Omoh O"],
          answer: "Martins A"
        },
        {
          question: "Which trainee was the Batch chairman?",
          options: ["Awusa K", "Chinedu I", "John U", "Niyi O"],
          answer: "John U"
        },
        {
          question: "Which trainee was populay referred to as 'Well Fed'?",
          options: ["Ijeoma O", "Tobin D", "Chinedu I", "Felix A"],
          answer: "Chinedu I"
        },
        {
          question: "When did SITP 4 start?",
          options: ["Jun 2020", "May 2020", "Dec 2020", "Jan 2021"],
          answer: "Jun 2020"
        },   
        {
          question: "How many babies were in batch 4?",
          options: ["1", "2", "0", "10"],
          answer: "1"
        },
        {
          question: "Who was the Batch 4 Engineering Stream student representative?",
          options: ["Awusa K", "Chidi O", "Didi C", "Niyi O"],
          answer: "Chidi O"
        },
        {
          question: "Who was the Batch 4 IT Stream student representative?",
          options: ["Steve O", "Awusa K", "Anuli N", "Felix A"],
          answer: "Awusa K"
        },   
        {
          question: "Which prof used to say '...some people just like to hear the sound of their own voice'?",
          options: ["Prof. Basil Onyekpe", "Prof Salami", "Prof. Etu Efeoto", "Prof. Omuigui"],
          answer: "Prof. Basil Onyekpe"
        },
        {
          question: "Which prof used to say '...some people spend the better part of their lives sleeping'?",
          options: ["Prof Salami", "Prof Ohanomah", "Prof. Etu Efeoto", "Prof. Basil Onyekpe"],
          answer: "Prof Ohanomah"
        },      
        {
          question: "Who was SITP administrator during our session??",
          options: ["Dr Peter Kragha", "Tony Akpokene", "Kirsty Moore", "Niyi O"],
          answer: "Dr Peter Kragha"
        }, 
        {
          question: "Which of these people lived in 10 Kaduna St?",
          options: ["Tunde L", "Martins A", "Niyi O", "Aliyu S"],
          answer: "Martins A"
        },     
        {
          question: "Which of these people did not live in 5 Kaduna St?",
          options: ["Deji A", "Yemi B", "Ehi A", "Awusa K"],
          answer: "Ehi A"
        },                     
        {
          question: "Who was the Batch 4 Geoscience Stream student representative?",
          options: ["Gideon G", "Uche O", "Deji A", "Nnamdi O"],
          answer: "Gideon G"
        }      
    ];

    // Shuffle questions
    const shuffledQuiz = quiz.sort(() => Math.random() - 0.5);

    let currentQuestion = 0;
    let score = 0;
    let timer;
    let timeLeft = 10; // seconds per question

    const questionEl = document.getElementById("question");
    const optionsEl = document.getElementById("options");
    const nextBtn = document.getElementById("next-btn");
    const resultEl = document.getElementById("result");
    const timerEl = document.getElementById("timer");
    const progressEl = document.getElementById("progress");

    function loadQuestion() {
    resetTimer();
    const q = shuffledQuiz[currentQuestion];
    questionEl.textContent = q.question;
    optionsEl.innerHTML = "";
    q.options.forEach(option => {
        const label = document.createElement("label");
        label.classList.add("option");
        const input = document.createElement("input");
        input.type = "radio";
        input.name = "option";
        input.value = option;
        label.appendChild(input);
        label.appendChild(document.createTextNode(option));
        optionsEl.appendChild(label);
    });
    updateProgress();
    startTimer();
    }

    function startTimer() {
    timeLeft = 10;
    timerEl.textContent = timeLeft;
    timer = setInterval(() => {
        timeLeft--;
        timerEl.textContent = timeLeft;
        if (timeLeft <= 0) {
        clearInterval(timer);
        autoNext();
        }
    }, 1000);
    }

    function resetTimer() {
    clearInterval(timer);
    timerEl.textContent = timeLeft;
    }

    function autoNext() {
    checkAnswer();
    currentQuestion++;
    if (currentQuestion < shuffledQuiz.length) {
        loadQuestion();
    } else {
        showResult();
    }
    }

    nextBtn.addEventListener("click", () => {
    if (!document.querySelector('input[name="option"]:checked')) {
        alert("Please select an option.");
        return;
    }
    checkAnswer();
    currentQuestion++;
    if (currentQuestion < shuffledQuiz.length) {
        loadQuestion();
    } else {
        showResult();
    }
    });

    function checkAnswer() {
    const selected = document.querySelector('input[name="option"]:checked');
    if (selected && selected.value === shuffledQuiz[currentQuestion].answer) {
        score++;
    }
    }

    function generateComment(score, total) {
    const percent = (score / total) * 100;
    if (percent === 100) {
        return "You too much! You missed your calling, you should be a Professor. Go for it! 🎉";
    } else if (percent >= 80) {
        return "Well done o! One SJ Abed rice on the way. 👏";
    } else if (percent >= 60) {
        return "Let my people go. No worry, make we finish the matter for Kosini 👍";
    } else if (percent >= 40) {
        return "Please return the allowee! We no gree. You can do better.  💪";        
    } else if (percent >= 20) {
        return "Just take the test again. No long story. Make we no report you to Shell management. 📚";
    } else {
        return "AChai diaris God o! Please return the certificate. No stories, just return am. 🌱";
    }
    }

    function showResult() {
    questionEl.style.display = "none";
    optionsEl.style.display = "none";
    nextBtn.style.display = "none";
    timerEl.style.display = "none";
    progressEl.style.width = "100%";
    const comment = generateComment(score, shuffledQuiz.length);
    resultEl.innerHTML = `You scored ${score} out of ${shuffledQuiz.length}.<br>${comment}`;
    }

    function updateProgress() {
    const progressPercent = ((currentQuestion) / shuffledQuiz.length) * 100;
    progressEl.style.width = `${progressPercent}%`;
    }

    // Load first question
    loadQuestion();
});