# Flaskから必要な3つの機能を読み込む
# Flask：アプリ本体、render_template：HTML表示、request：送信データを受け取る
from flask import Flask, render_template, request
import random  # ランダム選択用
from urllib.parse import quote  # URLエンコード用

# 感情分析関数を別ファイルから読み込む（analysis/sentiment.py）
from analysis.sentiment import analyze_sentiment

# Flaskアプリの初期設定（__name__は今動かしているファイル名が自動セットされる）
app = Flask(__name__)

# 励ましメッセージのリスト
encouragements = [
    "継続は力なり！",
    "一歩ずつ進もう！",
    "今日もよく頑張りました！",
    "明日はもっと良くなる！",
    "自分を信じて！"
]

# 音楽URLの辞書（曲名とURLのペア）
music_urls = {
    "summer song - yui": "https://youtu.be/2vH0BXmgnlo?si=mnIwBbsuSETJ4xYA",
    "feel my soul - yui": "https://youtu.be/9MdbKAt06YQ?si=yuvqHeJjdycr7cYr",
    "tomorrow's way - yui": "https://youtu.be/yeGO-0p6ufg?si=Rolrtqk0Em0CJuCm",
    "the Beginning - one ok rock": "https://youtu.be/Hh9yZWeTmVM?si=yPiM8De4CqIY5JP4",
    "Stand Out Fit In - one ok rock": "https://youtu.be/IGInsosP0Ac?si=eSg69AIHKIfVvc-7",
}

# 「/」＝URLのトップページを作る。GETとPOSTの両方に対応。
@app.route('/', methods=['GET', 'POST'])
def index():
    # 【フォームからのデータ取得】
    if request.method == 'POST':
        # フォームから名前を取得
        username = request.form.get('username')

        # フォームから「habits（習慣チェックリスト）」のデータをリストで取得
        check_list = request.form.getlist('habits')

        # フォームから「self_score（自己評価点数）」を取得
        self_score = request.form.get('self_score')

        # フォームから「diary（日記テキスト）」を取得
        diary_text = request.form.get('diary')

        # 【感情分析の実行】
        sentiment = analyze_sentiment(diary_text)

        if sentiment == 'ポジティブ😊':
            sentiment_comment = "素敵な気持ちが伝わってきますね！この調子でがんばりましょう。"
        elif sentiment == 'ネガティブ😢':
            sentiment_comment = "辛い時もありますが、少しずつ元気になっていきましょう。応援しています！"
        else:
            sentiment_comment = "日々の気持ちを大切に、ゆっくり進んでいきましょう。"

        # 【習慣達成率の計算】
        total_habits = 4  # index.htmlのチェックボックス数に合わせてください
        check_kazu = len(check_list)
        seika = int((check_kazu / total_habits) * 100)

        # 【バッジ判定】
        if seika >= 90:
            badge = "🏅 ゴールドバッジ獲得 🏅"
        elif seika >= 70:
            badge = "🥈 シルバーバッジ獲得 🥈"
        elif seika >= 50:
            badge = "🥉 ブロンズバッジ獲得 🥉"
        else:
            badge = "がんばろう！"

        # 【自己評価点数コメント】
        score = int(self_score)
        if score >= 4:
            score_comment = "素晴らしい！よく頑張りました！"
        elif score == 3:
            score_comment = "まずまずの一日でしたね。"
        else:
            score_comment = "明日はもっと良くなるように応援しています！"

        # 【ランダム励ましメッセージ】
        message = random.choice(encouragements)

        # 【音楽URL選択】
        selected_music_url = random.choice(list(music_urls.values()))

        # 【Xシェア用テキストとURLエンコード】
        share_text = f"{username}さんの今日の自己評価は{self_score}点。習慣達成率は{seika}%。{message}"
        share_text_encoded = quote(share_text) #文章をURLに使える形に変換（エンコード）

        # 【結果ページにデータを渡す】
        return render_template('result.html',
                               username=username,
                               check_list=check_list,
                               self_score=self_score,
                               diary_text=diary_text,
                               comment=score_comment,
                               achievement_rate=seika,
                               encourage_message=message,
                               sentiment=sentiment,
                               sentiment_comment=sentiment_comment,
                               share_text_encoded=share_text_encoded,
                               badge=badge,
                               selected_music_url=selected_music_url)

    # 【最初にアクセスされたときの表示（フォーム）】
    return render_template('index.html')

# app.py を直接実行したときだけ、Flaskアプリを起動する。
if __name__ == '__main__':
    # Flaskアプリ起動時、デバッグモードON。（エラー時に詳細表示）
    app.run(debug=True)