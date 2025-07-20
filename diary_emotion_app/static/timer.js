// timer.js

window.onload = function() {
    const timeLimit = 15;  // 制限時間（秒）
    let timeLeft = timeLimit;
    const timerDisplay = document.getElementById('timer'); // タイマー表示要素
    const quizForm = document.getElementById('quiz-form'); // クイズフォーム

    // 初期表示
    timerDisplay.textContent = `残り時間: ${timeLeft}秒`;

    // 1秒ごとにカウントダウン
    const countdown = setInterval(() => {
        timeLeft--;
        timerDisplay.textContent = `残り時間: ${timeLeft}秒`;

        if (timeLeft <= 0) {
            clearInterval(countdown);
            // タイマー終了で自動送信
            quizForm.submit();
        }
    }, 1000);
};