n = int(input())

c = 0
for i in range(n):
    l = input()
    if "+" in l:
        c+=1
    else:
        c-=1
print(c)