
for i in range(5):
    j = 0
    for c in input().split(" "):
        if c == "1":
            print(abs(2 - i) + abs(2 - j))
        j+=1
