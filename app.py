from flask import Flask, render_template, request
import random

app = Flask(__name__)

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


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    name = request.form["name"]
    kikan = request.form["kikan"]

    kekka_ichiran = []
    for unsei in unsei_data[kikan]:
        result = random.choice(unsei["message"])
        if unsei["type"] == "総合運":
            msg, item, music, color = result
            music_url = music_urls[music]
            kekka_ichiran.append({
                "type": unsei["type"],
                "message": msg,
                "item": item,
                "music": music,
                "music_url": music_url,
                "color": color,
            })
        else:
            kekka_ichiran.append({
                "type": unsei["type"],
                "message": result,
            })

    return render_template("result.html", name=name, kikan=kikan, kekka=kekka_ichiran)

if __name__ == "__main__":
    app.run(debug=True)