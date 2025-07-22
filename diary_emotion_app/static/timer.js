// ページが読み込まれたらこの中の処理を始める
window.onload = function() {

    const timeLimit = 15;  // 制限時間は15秒
    let timeLeft = timeLimit;  // 残り時間を15秒で初期化

    // タイマー表示用（HTMLのid='timer'）取得
    const timerDisplay = document.getElementById('timer');
    // クイズのフォーム（HTMLのid='quiz-form'）取得
    const quizForm = document.getElementById('quiz-form');

    // 最初に画面に「残り時間: ？秒」と表示
    timerDisplay.textContent = `残り時間: ${timeLeft}秒`;

    // 1秒ごとにこの中の処理をくり返す
    const countdown = setInterval(() => {
        timeLeft--;  // 残り時間を1秒減らす
        // 新しい残り時間を画面に表示する
        timerDisplay.textContent = `残り時間: ${timeLeft}秒`;

        // もし残り時間が0秒以下になったら…
        if (timeLeft <= 0) {
            clearInterval(countdown);  // これ以上時間を減らさず
            quizForm.submit();  // 解答送信。（不正解表示）
        }
    }, 1000);  // 1秒ごとに繰り返し(setIntervalの間隔：1000ミリ秒)
};