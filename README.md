⭐️ 公開中
Flaskで作成した日記感情分析Webアプリ（Render）
→ https://diary-emotion.onrender.com
 
[ファイル構成]
diary_emotion_app/
├── app.py                  ← Flaskメインファイル（感情分析＆クイズのルーティング）
├── requirements.txt        ← 使用ライブラリ（Flask、gunicornなど）
├── analysis/
│   └── sentiment.py        ← 感情分析ロジック
├── static/
│   ├── style_diary.css     ← 日記画面用CSS
│   ├── style_quiz.css      ← クイズ画面用CSS
│   └── timer.js            ← 制限時間付きクイズ用JavaScript
└── templates/
    ├── index.html          ← 日記入力フォームページ
    ├── result.html         ← 感情分析結果表示ページ
    ├── quiz.html           ← クイズ出題ページ（まとめページ）
    ├── quiz_question.html  ← クイズの1問ずつ表示ページ（番号入力フォーム付き）
    └── quiz_feedback.html  ← クイズ回答後フィードバックページ（正解・不正解と次へボタン）

    ⭐️公開中　Flaskで作成したWeb運勢占いアプリ。（Render）
→　https://fortune-app-gv8r.onrender.com

📁 ファイル構成（fortune_appフォルダ内）
⚫︎fortune_app/app.py ： メイン処理（Flask）
⚫︎fortune_app/templates/ ： HTMLファイル群
⚫︎fortune_app/static/style.css ： CSSファイル
⚫︎fortune_app/requirements.txt ： 必要パッケージ

CLI版について：
work_04.pyはターミナル用の占いプログラムで、Webアプリとは別です。
