# ポジティブ・ネガティブのキーワード例
positive_words = ['楽', '嬉', '最高', '幸せ', 'ワクワク']
negative_words = ['悲', '疲', '最悪', '嫌', '辛']

# 感情分析関数（引数：日記テキスト）
def analyze_sentiment(text):
    pos_count = sum(word in text for word in positive_words)
    neg_count = sum(word in text for word in negative_words)

    # ポジティブとネガティブの数で判定
    if pos_count > neg_count:
        return 'ポジティブ😊'
    elif neg_count > pos_count:
        return 'ネガティブ😢'
    else:
        return 'どちらとも言えない🤔'