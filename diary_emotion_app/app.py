# Flaskから必要な3つの機能を読み込む
# Flask：アプリ本体、render_template：HTML表示、request：送信データを受け取る
# redirect、url_for はページ遷移に使う、sessionはセッション管理用
from flask import Flask, render_template, request, redirect, url_for, session
from analysis.sentiment import analyze_sentiment
from urllib.parse import quote  # URLエンコード用
import random  # ランダム抽出用

# Flaskアプリの初期設定（__name__は今動かしているファイル名が自動セットされる）
app = Flask(__name__)
app.secret_key = "your_secret_key"  # セッション使用に必要（適当な文字列にすること）

music_urls = {
    "summer song - yui": "https://youtu.be/2vH0BXmgnlo?si=mnIwBbsuSETJ4xYA",
    "feel my soul - yui": "https://youtu.be/9MdbKAt06YQ?si=yuvqHeJjdycr7cYr",
    "tomorrow's way - yui": "https://youtu.be/yeGO-0p6ufg?si=Rolrtqk0Em0CJuCm",
    "the Beginning - one ok rock": "https://youtu.be/Hh9yZWeTmVM?si=yPiM8De4CqIY5JP4",
    "Stand Out Fit In - one ok rock": "https://youtu.be/IGInsosP0Ac?si=eSg69AIHKIfVvc-7",
}

# クイズの問題一覧
quiz_questions = [
    {
        "question": "Pythonの拡張子は？",
        "options": ["1. .py", "2. .java", "3. .txt"],
        "answer": 1
    },
    {
        "question": "HTMLの略は？",
        "options": ["1. Hyper Trainer Marking Language", "2. HyperText Markup Language", "3. HighText Machine Language"],
        "answer": 2
    },
    {
        "question": "CSSの役割は？",
        "options": ["1. ページ構造", "2. スタイルの指定", "3. データベース"],
        "answer": 2
    },
    {
        "question": "Flaskは何のフレームワーク？",
        "options": ["1. Java", "2. Python", "3. PHP"],
        "answer": 2
    },
    {
        "question": "辞書型のデータ構造は？",
        "options": ["1. list", "2. set", "3. dict"],
        "answer": 3
    },
    {
        "question": "for文は何をする？",
        "options": ["1. 条件分岐", "2. 繰り返し", "3. 関数定義"],
        "answer": 2
    },
    {
        "question": "if文の役割は？",
        "options": ["1. 繰り返し", "2. 条件分岐", "3. 変数定義"],
        "answer": 2
    },
    {
        "question": "Pythonでコメントを書くには？",
        "options": ["1. //", "2. <!-- -->", "3. #"],
        "answer": 3
    },
    {
        "question": "int型は何を表す？",
        "options": ["1. 文字列", "2. 整数", "3. 小数"],
        "answer": 2
    },
    {
        "question": "len関数の役割は？",
        "options": ["1. 長さを求める", "2. 足し算する", "3. 型を変える"],
        "answer": 1
    }
]

# 日記入力画面と感情分析の処理
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # フォームから値を受け取る
        username = request.form.get("username", "")
        habits = request.form.getlist("habits")  # チェックボックスは getlist を使う
        self_score = request.form.get("self_score", "")
        diary_text = request.form.get("diary", "")

        # 習慣達成率を計算（選択肢4個中の達成割合）
        total_habits = 4
        achievement_rate = len(habits) / total_habits * 100 if total_habits > 0 else 0

        # 感情分析を実行
        sentiment, sentiment_comment = analyze_sentiment(diary_text)

        # バッジや励ましメッセージは適宜設定（例として固定値）
        badge = "努力賞"
        encourage_message = "今日もよく頑張りましたね！"

        # シェア用テキストをURLエンコード
        share_text = f"{username}さんの今日の感情は「{sentiment}」です。"
        share_text_encoded = quote(share_text)

        # 疲れを癒す音楽のURL（例）
        # music_urls からランダムに1つ選択
        selected_music_url = random.choice(list(music_urls.values()))

        # セッションに保存して別ルートでも使えるようにする
        session["username"] = username
        session["habits"] = habits
        session["self_score"] = self_score
        session["diary_text"] = diary_text
        session["achievement_rate"] = achievement_rate
        session["sentiment"] = sentiment
        session["sentiment_comment"] = sentiment_comment
        session["badge"] = badge
        session["encourage_message"] = encourage_message
        session["share_text_encoded"] = share_text_encoded
        session["selected_music_url"] = selected_music_url

        # 結果画面へリダイレクト
        return redirect(url_for("show_result"))
    else:
        # GETは入力フォーム画面表示
        return render_template("index.html")

# クイズの最初の問題を表示するルート
@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if "quiz_order" not in session:
        # 10問中ランダムに5問選んで出題順としてセット
        session["quiz_order"] = random.sample(range(len(quiz_questions)), 5)
        session["current_q"] = 0
        session["last_result"] = ""
        session["score"] = 0

    quiz_order = session["quiz_order"]
    current_q = session["current_q"]

    if request.method == "POST":
        user_answer = request.form.get("answer", "")
        question_index = quiz_order[current_q]
        correct_answer = quiz_questions[question_index]["answer"]

        # 正誤判定（番号の文字列として比較）
        # user_answer は文字列、answerはintなので変換して比較
        if user_answer.isdigit() and int(user_answer) == correct_answer:
            result = "正解！"
            session["score"] += 1
        else:
            result = f"不正解。正解は「{correct_answer}」でした。"

        session["last_result"] = result
        session["current_q"] = current_q + 1  # 次の問題へ進める

        return redirect(url_for("quiz_result"))

    else:
        # GETは問題表示
        if current_q >= len(quiz_order):
            # 全問終了したら結果画面へ
            return redirect(url_for("quiz_result"))

        question_index = quiz_order[current_q]
        question = quiz_questions[question_index]

        return render_template(
            "quiz.html",
            question=question,
            question_number=current_q + 1,
            total_questions=len(quiz_order)
        )

# クイズの結果表示ページ
@app.route("/quiz/result", methods=["GET"])
def quiz_result():
    result = session.get("last_result", "")
    current_q = session.get("current_q", 0)
    total_questions = len(session.get("quiz_order", []))
    score = session.get("score", 0)
    finished = current_q >= total_questions
    return render_template(
        "quiz_result.html",
        result=result,
        current_q=current_q,
        total=total_questions,
        score=score,
        finished=finished
    )

# クイズを最初からやり直すときのルート
@app.route("/quiz/reset")
def quiz_reset():
    session.pop("quiz_order", None)
    session["current_q"] = 0
    session["last_result"] = ""
    session["score"] = 0
    return redirect(url_for("quiz"))

# 日記結果画面を別ルートで表示したい場合に追加する例
@app.route("/result")
def show_result():
    # セッションから値を取得して渡す
    username = session.get("username")
    habits = session.get("habits")
    self_score = session.get("self_score")
    diary_text = session.get("diary_text")
    achievement_rate = session.get("achievement_rate")
    sentiment = session.get("sentiment")
    sentiment_comment = session.get("sentiment_comment")
    badge = session.get("badge")
    encourage_message = session.get("encourage_message")
    share_text_encoded = session.get("share_text_encoded")
    selected_music_url = session.get("selected_music_url")

    if username is None:
        return redirect(url_for("index"))

    return render_template(
        "result.html",
        username=username,
        habits=habits,
        self_score=self_score,
        diary_text=diary_text,
        achievement_rate=achievement_rate,
        sentiment=sentiment,
        sentiment_comment=sentiment_comment,
        badge=badge,
        encourage_message=encourage_message,
        share_text_encoded=share_text_encoded,
        selected_music_url=selected_music_url,
        comment=sentiment_comment
    )

# Flaskアプリ起動（このファイルが直接実行されたときのみ起動する）
if __name__ == "__main__":
    app.run(debug=True)