import random

meisanhin_jisho = {
    "もみじ饅頭": "広島県",
    "雷おこし": "東京都" ,
    "信玄餅": "山梨県",
    "明太子": "福岡県",
    "八ツ橋": "京都府",
    "味噌カツ": "愛知県",
    "きりたんぽ": "秋田県",
    "じゃがポックル": "北海道",
    "ういろう": "愛知県",
    "カステラ": "長崎県",
    "ずんだ餅": "宮城県"
}
#ランダムで問題１問を選ぶ
def sentaku(meisanhin_jisho):
    meisanhin_ichiran = list(meisanhin_jisho.items()) #辞書をリストの形に変換する
    list_sentaku = random.choice(meisanhin_ichiran) #リストからランダムに１つ選ぶ
    return list_sentaku[0], list_sentaku[1] #0が名産品、1が都道府県(listの要素番号)

#「都」「府」「県」以外の文字を出力する
def todofuken_nuki(text):
    result = ""
    for moji in text:  #文字列を、1文字ずつ見ていく
        if moji not in ["都", "府", "県"]: #もしその文字が「都」「府」「県」じゃなかったら
            result += moji #1文字ずつ、resultに追加していく
    return result

print("全国名産品 都道府県当てクイズ ")
print("名産品が表示されるので、それがどこの都道府県のものか当ててください。")
print("都・道・府・県は付けても付けなくてもOKです。")
print("クイズを終了したいときは、大文字で「Z」と入力してください。")

# --- 初期化 ---
seikai_suu = 0
kaitou_suu = 0
machigaeta_mondai_ichiran = []
shutsudai_zumi_meisanhin = []

# --- クイズをループする ---
while True:
    nokori_no_mondai = {} #出題していない名産品だけで辞書を作る
    for meisanhin, todofuken in meisanhin_jisho.items():
        if meisanhin not in shutsudai_zumi_meisanhin: #まだ出題してなければ
            nokori_no_mondai[meisanhin] = todofuken #辞書に追加する

    # 出題済みで問題がない場合は終了
    if not nokori_no_mondai:
        print("\n全問出題終わりました。")
        break

    mondai_meisanhin, seikai_todofuken = sentaku(nokori_no_mondai) #問題をランダムに１つ選ぶ
    shutsudai_zumi_meisanhin.append(mondai_meisanhin) #出題済みリストに追加

    print(f"\n 問題「{mondai_meisanhin}」はどこの都道府県の名産品？")
    nyuuryoku_kaitou = input("あなたの答えを入力してください: ")

    if nyuuryoku_kaitou == "Z": #「Z」と入力されたら終了する。
        print("\nクイズを終了します。")
        break
    kaitou_suu += 1

    if todofuken_nuki(nyuuryoku_kaitou) == todofuken_nuki(seikai_todofuken):#「都」「府」「県」を除いた文字で正解かどうか
        print("正解！")
        seikai_suu += 1
    else:
        print(f"不正解！正解は「{seikai_todofuken}」です。")
        machigaeta_mondai_ichiran.append((mondai_meisanhin, nyuuryoku_kaitou, seikai_todofuken))

# --- 結果表示 ---
print("\n 結果発表")
print(f"正解数: {seikai_suu} / {kaitou_suu}")


if kaitou_suu > 0: #回答数が0じゃなければ、正解率を計算して表示
    seikai_ritsu = round(seikai_suu / kaitou_suu * 100)
    print(f"正解率: {seikai_ritsu}%")

# 間違った問題の問題と回答を表示
if machigaeta_mondai_ichiran:
    print("\n間違えた問題一覧")
    for meisanhin, anata_no_kaitou, tadashii_kotae in machigaeta_mondai_ichiran:
        print(f"「{meisanhin}」 → あなたの答え: {anata_no_kaitou} / 正解: {tadashii_kotae}")
else:
    print("全問正解！")