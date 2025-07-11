import random
import time

music_urls = {
    "summer song - yui": "https://youtu.be/2vH0BXmgnlo?si=mnIwBbsuSETJ4xYA",
    "feel my soul - yui": "https://youtu.be/9MdbKAt06YQ?si=yuvqHeJjdycr7cYr",
    "tomorrow's way - yui": "https://youtu.be/yeGO-0p6ufg?si=Rolrtqk0Em0CJuCm",
    "the Beginning - one ok rock": "https://youtu.be/Hh9yZWeTmVM?si=yPiM8De4CqIY5JP4",
    "Stand Out Fit In - one ok rock": "https://youtu.be/IGInsosP0Ac?si=eSg69AIHKIfVvc-7",
}

unsei_data = {
    "今日": [
        {
            "type": "総合運",
            "message": [
                ("大吉! 最高の1日になりそう!", "赤い靴", "summer song - yui", "赤色"),
                ("中吉! 運が味方してくれるかも。前向きに！", "四つ葉のクローバー", "feel my soul - yui", "緑"),
                ("小吉! 少しずつ良くなっていくよ。焦らずに！", "黄色いハンカチ", "tomorrow's way - yui", "黄"),
                ("吉! 悪くはないけど油断は禁物！", "星のネックレス", "the Beginning - one ok rock", "青"),
                ("凶! 今日は慎重に行動しよう。", "虹色の傘", "Stand Out Fit In - one ok rock", "紫"),
            ],
        },
        {
            "type": "仕事運",
            "message": [
                ("絶好調！仕事はかどるよ！"),
                ("普通だね、頑張れ！"),
                ("ミスに注意して！"),
                ("要注意！慎重に！"),
                ("最悪。。。大丈夫！焦らないで！"),
            ],
        },
        {
            "type": "学業運",
            "message": [
                ("絶好調！勉強はかどるよ！"),
                ("普通だね、頑張れ！"),
                ("ケアレスミスに注意して！"),
                ("要注意！復讐をしっかりしよう！"),
                ("最悪。。。でも失敗は成功のもと！"),
            ],
        },
        {
            "type": "健康運",
            "message": [
                ("絶好調！体調は最高！"),
                ("普通だね、今日も頑張れ！"),
                ("注意！周りをよく見て怪我に注意！"),
                ("要注意！！焦ると怪我するよ！"),
                ("最悪。。。今日は慎重に行動しよう！"),
            ],
        },
    ],
    "明日": [
        {
            "type": "総合運",
            "message": [
                ("明日は大吉！良いことがありそう！", "赤い帽子", "summer song - yui", "赤色"),
                ("明日は中吉！気をつけつつも楽しんで！", "四つ葉の種", "feel my soul - yui", "緑"),
                ("明日は小吉！無理しないでゆっくりね。", "青いリボン", "tomorrow's way - yui", "青"),
                ("明日は吉！変化の兆しあり。注意！", "銀のペンダント", "the Beginning - one ok rock", "銀"),
                ("明日は凶！無理しないで休もう。", "黒い傘", "Stand Out Fit In - one ok rock", "黒"),
            ],
        },
        {
            "type": "仕事運",
            "message": [
                ("絶好調！明日は仕事がはかどる！"),
                ("普通だね、明日も頑張れ！"),
                ("ミスに注意して！"),
                ("要注意！慎重に！"),
                ("最悪。。。焦らないで！"),
            ],
        },
        {
            "type": "学業運",
            "message": [
                ("絶好調！明日は勉強はかどるよ！"),
                ("普通だね、明日も頑張れ！"),
                ("ケアレスミスに注意して！"),
                ("要注意！復讐をしっかりしよう！"),
                ("最悪。。。でも失敗は成功のもと！"),
            ],
        },
        {
            "type": "健康運",
            "message": [
                ("絶好調！体調は最高！明日も頑張れ！"),
                ("普通だね、無理しないでね！"),
                ("注意！怪我に気をつけて！"),
                ("要注意！！焦らないで！"),
                ("最悪。。。ゆっくり休もう！"),
            ],
        },
    ],
    "今週": [
        {
            "type": "総合運",
            "message": [
                ("今週は大吉！目標に向かって一直線！", "金の指輪", "summer song - yui", "金"),
                ("今週は中吉！計画的に進めよう！", "四つ葉のクローバー", "feel my soul - yui", "緑"),
                ("今週は小吉！小さな幸運が舞い込む！", "黄色いバンダナ", "tomorrow's way - yui", "黄"),
                ("今週は吉！頑張りが評価されそう！", "星のチャーム", "the Beginning - one ok rock", "青"),
                ("今週は凶！休息を大事にしよう！", "赤いマフラー", "Stand Out Fit In - one ok rock", "赤"),
            ],
        },
        {
            "type": "仕事運",
            "message": [
                ("今週は絶好調！仕事がはかどる！"),
                ("今週は普通。地道に頑張ろう！"),
                ("今週はミス注意！慎重にね！"),
                ("今週は要注意！無理は禁物！"),
                ("今週は最悪。。。焦らずに！"),
            ],
        },
        {
            "type": "学業運",
            "message": [
                ("今週は絶好調！勉強がはかどる！"),
                ("今週は普通。コツコツ頑張ろう！"),
                ("今週はケアレスミス注意！"),
                ("今週は要注意！復習を忘れずに！"),
                ("今週は最悪。。。でも次につなげよう！"),
            ],
        },
        {
            "type": "健康運",
            "message": [
                ("今週は絶好調！元気いっぱい！"),
                ("今週は普通。体調に気をつけて！"),
                ("今週は注意！怪我に気をつけて！"),
                ("今週は要注意！焦らず過ごそう！"),
                ("今週は最悪。。。ゆっくり休もう！"),
            ],
        },
    ],
}

# ---------- 名前の入力 ----------
name = input("あなたの名前を入力してください: ")
print(f"\n{name}さん、運勢占いへようこそ！")

# ---------- 期間選択の入力処理 ----------
while True:
    print("\n占う期間を選んでください。")
    print("1: 今日")
    print("2: 明日")
    print("3: 今週")
    kikan_sentaku = input("番号を半角の数字で入力してください（例: 1）: ").strip()

    if kikan_sentaku == "1":
        kikan = "今日"
    elif kikan_sentaku == "2":
        kikan = "明日"
    elif kikan_sentaku == "3":
        kikan = "今週"
    else:
        print("1, 2, 3 のいずれかを入力してください。")
        continue

    input(f"\nエンターを押すと{kikan}の運勢を占います...")

    print("占っています...")
    time.sleep(2)  # 2秒待って演出する

    kekka_ichiran = []  # ← 結果まとめ用リストを空にしておく

    # ---------- 期間ごとの運勢をランダムに選ぶ ----------
    for unsei in unsei_data[kikan]:
        result = random.choice(unsei["message"])  # 運勢のmessageをランダムに1つ選ぶ
        kekka_ichiran.append((unsei["type"], result))  # ← 結果を保存

        print(f"\n【{unsei['type']}】")  # 運勢種類の見出し表示

        if unsei["type"] == "総合運":
            msg, item, music, color = result
            print(f"運勢: {msg}")
            print(f"ラッキーアイテム: {item}")
            print(f"ラッキーミュージック: {music}")
            print(f"ラッキーカラー: {color}")
        else:
            msg = result
            print(f"運勢: {msg}")

        input("エンターを押して次の運勢へ！")

    # ---------- 結果まとめ表示 ----------
    print("\n--- 運勢まとめ ---")
    for unsei_type, result in kekka_ichiran:
        if unsei_type == "総合運":
            music = result[2]
            url = music_urls[music]

            print(f"{unsei_type} : {result[0]}（カラー：{result[3]}）")
            print(f"ラッキーミュージック: {music}")
            print(f"上の音楽を聴いてみる → {url}")
        else:
            print(f"{unsei_type} : {result}")

    print(f"\n{name}さんの運勢はこれで終わりです！")

    # ---------- リトライするか確認 ----------
    while True:
        retry = input("もう一度占いたいですか？（Y/N）: ").strip().upper()

        if retry == "Y":
            break  # → 占いループの先頭に戻る
        elif retry == "N":
            print(f"\n{name}さん、良い一日を！また来てね〜！")
            exit()  # → プログラムを完全終了
        else:
            print("Y または N を入力してください。")
