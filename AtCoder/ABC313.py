'''
n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])

count = 0
if n == 1:
    print(0)
else:
    while max(a)-min(a) != 1:
        maxNum = a.index(max(a))
        minNum = a.index(min(a))
        if max(a)-min(a) <= 10:
            a[maxNum] = max(a)-1
            a[minNum] = min(a)+1
            count += 1
        else:
            a[maxNum] = max(a)-1000
            a[minNum] = min(a)+1000
            count += 1000
        print(a)
    else:
        print(count)
'''
n, m= input().split()
n = int(n)
m = int(m)
strong = []
weak = []
for i in range(m):
    a = input().split()
    strong.append(int(a[0]))
    weak.append(int(a[1]))
ans = [i for i in range(1,n+1)]
for i in range(m):
   if weak[i] in ans:
       ans.remove(weak[i]) 

if len(ans) == 1:
    print(ans[0])
else:
    print(-1)
'''
#A
n = int(input())
p = input().split()
for i in range(n):
    p[i] = int(p[i])
saikyo = max(p)
if saikyo == p[0]:
    if p.count(saikyo)>=2:
        print(1)
    else:
        print(0)
else:
    print(saikyo+1-p[0])
'''