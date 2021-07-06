n,k = [int(x) for x in input().split(" ")]
c = [int(x) for x in input().split(" ")]

t = 0
for v in c:
    if v >= c[k - 1] and v > 0:
        t+=1

print(t)