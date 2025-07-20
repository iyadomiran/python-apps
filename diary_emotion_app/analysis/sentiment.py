def analyze_sentiment(text):
    # 簡易的なキーワード判定による感情分析（例）
    positive_words = ["嬉しい", "楽しい", "幸せ", "良い", "感謝"]
    negative_words = ["悲しい", "辛い", "嫌い", "怒り", "疲れた"]

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