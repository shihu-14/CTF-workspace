s = input()

ans = ""
for c in s:
    if c.isalpha():
        if c.islower():
            ans += chr((ord(c) - ord('a') + 13) % 26 + ord('a'))
        else:
            ans += chr((ord(c) - ord('A') + 13) % 26 + ord('A'))
    else:
        ans += c

print(ans)