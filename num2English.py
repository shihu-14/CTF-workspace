with open("numlist.txt", "r") as f:
    for line in f:
        num = line.strip()
        print(chr(int(num)), end="")

    print()
