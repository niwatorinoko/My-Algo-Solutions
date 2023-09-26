"""
#A
n, h, x = input().split()
n = int(n)
h = int(h)
x = int(x)
p = input().split()
for i in range(n):
    if int(p[i])+h >= x:
        print(i+1)
        break
"""
"""
#B
n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
a = sorted(a)
for i in range(1,n):
    if a[i] - a[i-1] == 2:
        print(a[i]-1)
        break
"""
n = int(input())
all = 0
li = []
takahashi = 0
aoki = 0
for i in range(n):
    x, y, z = input().split()
    all += int(z)
    x = int(x)
    y = int(y)
    takahashi += x
    aoki += y
    if x < y:
        #引数１はその時の鞭変え数、２は獲得できる座席数
        print(x,y,((y-x+1)//2)+1-x)
        li.append([((y-x+1)//2)+1-x,int(z)])
if takahashi>aoki:
    print(0)
else:
    ans = 0
    for i in range(len(li),0,-1):
        for j in range(len(li)-i+1):
            print(li[j:j+i])