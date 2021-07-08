a = input().lower()
b = input().lower()


for i in range(len(a)):
    if a > b:
        print(1)
        exit()
    elif a < b:
        print(-1)
        exit()

print(0)