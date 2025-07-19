# ポジティブ・ネガティブのキーワード例
positive_words = ['楽', '嬉', '最高', '幸せ', 'ワクワク']
negative_words = ['悲', '疲', '最悪', '嫌', '辛']

def analyze_sentiment(text):
    pos_count = sum(text.count(word) for word in positive_words)  # 出現回数をカウント
    neg_count = sum(text.count(word) for word in negative_words)

    if pos_count > neg_count:
        return 'ポジティブ😊'
    elif neg_count > pos_count:
        return 'ネガティブ😢'
    else:
        return 'どちらとも言えない🤔'