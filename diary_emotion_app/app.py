# Flaskから下記機能を使用可能にする
# Flask：アプリ本体、render_template：HTML表示、request：データを受け取る(日記など)、redirect＆url_for：ページ移動、session：データ一時保存
from flask import Flask, render_template, request, redirect, url_for, session
# 感情分析の関数をanalysis/sentiment.pyから読み込む
from analysis.sentiment import analyze_sentiment
# URLの中で使えない文字を、安全な文字に変換(quote)。エンコード
from urllib.parse import quote
import random

# Flaskアプリを作る宣言
app = Flask(__name__)
# ユーザーごとの情報を安全に保つためのキーを設定
app.secret_key = "your_secret_key"

music_urls = {
    "summer song - yui": "https://youtu.be/2vH0BXmgnlo?si=mnIwBbsuSETJ4xYA",
    "feel my soul - yui": "https://youtu.be/9MdbKAt06YQ?si=yuvqHeJjdycr7cYr",
    "tomorrow's way - yui": "https://youtu.be/yeGO-0p6ufg?si=Rolrtqk0Em0CJuCm",
    "the Beginning - one ok rock": "https://youtu.be/Hh9yZWeTmVM?si=yPiM8De4CqIY5JP4",
    "Stand Out Fit In - one ok rock": "https://youtu.be/IGInsosP0Ac?si=eSg69AIHKIfVvc-7",
}

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

# トップページにアクセス:表示・送信の両方対応
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":  # フォーム送信(post)の際は、下記４つ取得。
        username = request.form.get("username")  # ユーザー名
        habits = request.form.getlist("habits")  # チェックリスト
        self_score = request.form.get("self_score")  # 自己評価スコア
        diary_text = request.form.get("diary")  # 日記

        # チェックリスト合計４つ
        total_habits = 4
        # 達成率(%)の計算 (0より大きいなら計算、0なら0%  例: 2/4なら、2/4×100 = 50%)
        achievement_rate = len(habits) / total_habits * 100 if total_habits > 0 else 0

        # analyze_sentiment関数で、感情ポジネガとコメントを、日記から分析
        sentiment, sentiment_comment = analyze_sentiment(diary_text)

        # バッジ、お疲れコメントを表示
        if achievement_rate >= 90:
            badge = "🥇"
        elif achievement_rate >= 70:
            badge = "🥈"
        else:
            badge = "🥉"
        encourage_message = "今日もお疲れ様です！"

        # Xシェア用URLをエンコード(日本語でURL壊れないように)
        share_text = f"{username}さんの今日の感情は「{sentiment}」です。"
        share_text_encoded = quote(share_text)

        # music_urls からランダムに1つ選択(music_urls.values() → 曲のURL)
        selected_music_url = random.choice(list(music_urls.values()))

        # 各ユーザーごとの情報をサーバーに一時保存
        session["username"] = username  # ユーザー名
        session["habits"] = habits  # チェックリスト
        session["self_score"] = self_score  # 自己評価スコア
        session["diary_text"] = diary_text  # 日記
        session["achievement_rate"] = achievement_rate  # 習慣達成率（%）
        session["sentiment"] = sentiment  # 感情分析ポジネガ
        session["sentiment_comment"] = sentiment_comment  # 感情分析コメント
        session["badge"] = badge  # 習慣達成率バッジ
        session["encourage_message"] = encourage_message  # お疲れコメント
        session["share_text_encoded"] = share_text_encoded  # Xシェア時テキスト,URL
        session["selected_music_url"] = selected_music_url  # 音楽

        # 結果画面へ移動 (POST)
        return redirect(url_for("show_result"))
    else:
        # 入力フォーム画面を表示 (GET)
        return render_template("index.html")

# クイズにアクセスされた時
@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    # クイズの進行情報がセッションに一時保存されてなければ
    if "quiz_order" not in session:
        # 10問中ランダムに5問選んで出題順としてセット
        session["quiz_order"] = random.sample(range(len(quiz_questions)), 5)
        # 問題番号を 0 にリセット(1問目〜)
        session["current_q"] = 0
        # 正解・不正解を初期化
        session["last_result"] = ""

    # セッションに保存されたクイズをquiz_order に取り出して使う
    quiz_order = session["quiz_order"]
    # 現在のクイズ番号を変数 current_q に保存
    current_q = session["current_q"]

    # 解答送信されたら
    if request.method == "POST":
        # ユーザーの答えを取得
        user_answer = request.form.get("answer")
        # 問題のインデックス番号を取り出す
        question_index = quiz_order[current_q]
        # 正解の番号を取り出してcorrect_answerに入れる
        correct_answer = quiz_questions[question_index]["answer"]

        # user_answer は文字列、answerは整数なので整数(int)に変換して比較
        if user_answer.isdigit() and int(user_answer) == correct_answer:
            result = "正解！"
        else:
            result = f"不正解。正解は「{correct_answer}」でした。"

        session["last_result"] = result  # 正解不正解を保存
        session["current_q"] = current_q + 1  # 今何問目かカウント

        return redirect(url_for("quiz_result"))  # 結果ページへ
    
    # 問題ページを表示するとき
    else:
        # 現在の問題番号 current_q の出題数が、5以上になったら
        if current_q >= 5:
            # 結果ページへ
            return redirect(url_for("quiz_result"))
        
        # 出題問題のインデックス番号を取り出す
        question_index = quiz_order[current_q]
        # 問題文・選択肢・正解をquiz_questionsから取る
        question = quiz_questions[question_index]

        # 問題ページ表示(quiz.html)
        return render_template(
            "quiz.html",
            question=question,  # 1問分の問題
            question_number=current_q + 1,  # 今何問目か
            total_questions=5
        )

# クイズの結果ページ
@app.route("/quiz/result", methods=["GET"])
def quiz_result():
    result = session.get("last_result")  # 直前の問題の正解／不正解を取る
    current_q = session.get("current_q", 0)  # セッションから現在の問題番号を取る、見つからなければ 0（最初）
    total_questions = 5
    finished = current_q >= total_questions  # 全問終了したか判断

    return render_template(
        "quiz_last.html",  # クイズの結果ページを表示
        result=result,  # 正解 or 不正解
        current_q=current_q,  # 今何問目か
        total=total_questions,  # 全部で何問か(5)
        finished=finished  # 全問終了してればtrue
    )

# クイズを最初からやり直すときのルート
@app.route("/quiz/reset")
def quiz_reset():
    session.pop("quiz_order")  # session から "quiz_order"（クイズの出題順リスト）を削除
    session["current_q"] = 0  # 問題番号を 0番目にリセット
    session["last_result"] = ""   # セッションに保存された正解／不正解をリセット
    return redirect(url_for("quiz"))  # クイズ開始ページへ移動

# 日記結果画面にアクセスした時
@app.route("/result")
def show_result():
    # セッションから値を取得して渡す
    username = session.get("username")  # ユーザー名
    habits = session.get("habits")  # チェックリスト
    self_score = session.get("self_score")  # 自己評価スコア
    diary_text = session.get("diary_text")  # 日記
    achievement_rate = session.get("achievement_rate")  # 習慣達成率（%）
    sentiment = session.get("sentiment")  # 感情分析ポジネガ
    sentiment_comment = session.get("sentiment_comment")  # 感情分析コメント
    badge = session.get("badge")  # 習慣達成率バッジ
    encourage_message = session.get("encourage_message")  # お疲れコメント
    share_text_encoded = session.get("share_text_encoded")  # Xシェア時テキスト,URL
    selected_music_url = session.get("selected_music_url")  # 音楽URL

    return render_template(  # last.htmlで結果ページ表示
        "last.html",
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
    )

# Flaskアプリ起動（app.pyが直接実行されたときのみ起動する）
if __name__ == "__main__":
    app.run(debug=True)  # デバックモード有効(エラー発生時に詳細表示)