import mysql.connector
import random

# MySQL に接続
conn = mysql.connector.connect(
    host="localhost",
    user="root",        # MySQLユーザー名
    password="",        # 最初設定してなければ空欄
    database="python_app"  # 作成したデータベース名
)

if conn.is_connected():
    print("MySQL に接続できました")
    
cursor = conn.cursor()

#９、最後に「もう一回やる？」を追加してループ化
while True:

    #１、1〜100 の中からコンピューターがランダムに1つの数字を選んて出力する
    random_number = random.randint(1, 100) #選ばれた数字をrandom_number に保存

    #４、5回まで挑戦できるようにする
    cnt = 0
    for i in range(5):
        cnt = cnt + 1

        #２、ユーザーに数字を入力させて、それを answer という変数に入れる
        answer = int(input("1~100までの数字を当ててください: ")) 
        print(answer)

        #３、数字が合ってるか判断
        #８、正解したら「○回目で当たり！」を表示して終了
        if answer == random_number:
            print(f"{cnt}回目で当たり！")
            break

        #６、7、ヒントを表示（大きい・小さい）
        sa = abs(random_number - answer) #absは 例えば、30(random_number) - 80(answer)になったとしても、50にしてくれる関数
        if answer < random_number:
            if sa >= 50:
                print("すごく小さい！")
            else:
                print("ちょっと小さい！")
        elif answer > random_number:
            if sa >= 50:
                print("すごく大きい！")
            else:
                print("ちょっと大きい！")

    #５、5回すべて外れたら正解を教える
    else:
        print(f"残念！正解は {random_number} でした。また挑戦してね！")

    # MySQL に試行回数を保存
    cursor.execute(
        "INSERT INTO work1_record (try_count) VALUES (%s)",
        (cnt,)  # タプルで渡すのがポイント
    )
    conn.commit()

    # 保存した内容を確認したい場合
    cursor.execute("SELECT * FROM work1_record")
    print("==== これまでの試行回数 ====")
    for row in cursor.fetchall():
        print(row)
    print("=============================")

    #９、最後に「もう一回やる？」を追加してループ化
    mouikkai = input("もう一度挑戦しますか？（ する→ Y / しない→ N )")
    if mouikkai == "Y":
        print("もう一回やるよ！")
    else:
        print("バイバイ！")
        break 

cursor.close()
conn.close()

#----------------------------------------------------------------------------
#１、1〜100 の中からコンピューターがランダムに1つの数字を選んて出力する
#２、ユーザーに数字を入力させて、それを answer という変数に入れる
#３、数字が合ってるか判断
#４、5回まで入力受け付ける
#５、正解したら終了

#６、ヒントを表示（大きい・小さい）
#７、差が大きいとき「かなり小さい／大きい」ヒントにする
#８、正解したら「〇回目で当たり！」と表示
#９、最後に「もう一回やる？」を追加してループ化
