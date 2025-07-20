def analyze_sentiment(text):
    positive_words = ["嬉", "楽", "幸", "良", "感謝"]
    negative_words = ["悲", "辛", "嫌", "怒", "疲"]

    pos_count = sum(word in text for word in positive_words)
    neg_count = sum(word in text for word in negative_words)

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