
while True:
    try:
        w = int(input())
        if w % 2 == 0:
            if w > 2:
                print("YES")
                continue
        print("NO")
    except EOFError:
        exit()