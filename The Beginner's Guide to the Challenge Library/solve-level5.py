import hashlib
import subprocess

correct_pw_hash = open('level5.hash.bin', 'rb').read()

with open('dictionary.txt', 'r') as f:
    for line in f:
        pw = line.strip()
        if hashlib.md5(bytearray(pw.encode())).digest() == correct_pw_hash:
            result = subprocess.run(['python3', 'level5.py'], input=pw, capture_output=True, text=True)
            print(result.stdout)
        

# import hashlib
# import subprocess


# correct_pw_hash = open("level5.hash.bin", "rb").read()


# def hash_pw(pw):
#     pw_bytes = bytearray()
#     pw_bytes.extend(pw)
#     m = hashlib.md5()
#     m.update(pw_bytes)
#     return m.digest()


# correct_input = hash_pw(correct_pw_hash)
# # print(f"Correct input: {correct_input}")

# result = subprocess.run(['python3', 'level5.py'], input=correct_input, capture_output=True, text=True)
# if "Welcome back" in result.stdout:
#     print(f"Correct password: {correct_input}")
#     print(result.stdout)