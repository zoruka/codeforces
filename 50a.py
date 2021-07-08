m,n = [int(x) for x in input().split(" ")]

t = (m * n)

if t % 2 == 0:
    print(int(t / 2))
else:
    print(int((t - 1) / 2))