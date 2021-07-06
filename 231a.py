n = int(input())
t = 0
for i in range(n):
    p,v,s = [int(x) for x in input().split(" ")]
    if p+v+s > 1:
        t+=1
print(t)