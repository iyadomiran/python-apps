import random   # ランダムを扱うモジュールの利用
import time     # 時間を扱うモジュールの利用

best_time = None  # 最高記録（最速反応時間）を保存する変数。Noneは、まだ記録がないってこと。

print("反応速度を測定します。")
print("【!!!!!】が出たら、できるだけ早くEnterキーを押してください。")

while True:   #　ーーーーー while文でループ処理を始める ーーーーー

    start = input("準備ができたらEnterキーを押してください。終了するなら 'F'を入力してください。")
    if start == 'F':
        break   # 'F'が入力されたら終了

    wait_time = random.randint(5, 15)  # 5〜15秒のランダム待機時間を決定
    time.sleep(wait_time)   #time.sleepは、待機(プログラム停止)するって意味。
    print("!!!!!")   # 合図！！！！！を出す。
    now_time1 = time.time()   # 合図が出た時（今の）時刻が取る
    input("Enterキーを押してください")   # ユーザーに、Enterを押すように指示する
    now_time2 = time.time()   # Enterが押された時（今の）時間を取る
    hannou_time = now_time2 - now_time1  # 合図が出てからEnter押されるまでの時間(反応時間)

    if hannou_time < 0.01:   # 反応速度が0.01秒未満で押されてたら、不正とする
        print("不正です")
        continue  # ループの先頭に戻る（再チャレンジになるように）
    print(f"反応時間：{hannou_time:.4f} 秒です")   # 不正じゃなければ、反応時間を小数点以下4桁にして表示

    if best_time is None or hannou_time < best_time: #まだ最高記録がなかったり、今回の反応時間が最高記録より速ければ
        best_time = hannou_time #最高記録（best_time）を更新して
        print(f"あなたのこれまでの最高記録は {best_time:.4f} 秒です。")  # さようならの前に最高記録を表示する

               # 　ーーーーー while文（ループ処理）終了 ーーーーー
print("さようなら！また遊んでね！")