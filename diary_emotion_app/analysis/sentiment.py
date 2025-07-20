# analysis/sentiment.py

def analyze_sentiment(text):
    """
    テキストの日記文に対して簡単な感情分析を行う関数。

    戻り値:
        sentiment: 感情のラベル（例："ポジティブ", "ネガティブ", "ニュートラル"）
        sentiment_comment: 感情に対するコメントやアドバイス
    """

    # 簡易的なキーワード判定による感情分析（例）
    positive_words = ["嬉しい", "楽しい", "幸せ", "良い", "感謝"]
    negative_words = ["悲しい", "辛い", "嫌い", "怒り", "疲れた"]

    # テキストを小文字化（必要に応じて日本語は別途処理も）
    text_lower = text.lower()

    pos_count = sum(word in text_lower for word in positive_words)
    neg_count = sum(word in text_lower for word in negative_words)

    if pos_count > neg_count:
        sentiment = "ポジティブ"
        sentiment_comment = "良い気持ちが伝わってきますね！"
    elif neg_count > pos_count:
        sentiment = "ネガティブ"
        sentiment_comment = "少し辛いことがあったかもしれませんね。"
    else:
        sentiment = "ニュートラル"
        sentiment_comment = "落ち着いた気持ちのようです。"

    return sentiment, sentiment_comment