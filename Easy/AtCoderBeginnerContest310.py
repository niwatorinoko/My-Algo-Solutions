'''
n, p, q = input().split()
d = input().split()
for i in range(len(d)):
    d[i] = int(d[i])

if int(p) > min(d)+int(q):
    print(min(d)+int(q))
else:
    print(p)
'''
'''
n, m= input().split()
n = int(n)
m = int(m)
li = []
for i in range(n):
    temp = input().split()
    li.append(temp)

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if int(li[i][0]) >= int(li[j][0]):
            elif li[j][2:int(len(li[j]))]>li[i][2:int(len(li[i]))]:
'''         
n = int(input())
li = []
for i in range(n):
    temp = input()
    if sorted(temp) not in li:
        li.append(sorted(temp))
print(len(li))

'''
print(set(li))
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        #print(i,j,sorted(li[i]),sorted(li[j]))
        if sorted(li[i]) == sorted(li[j]):
            li[j] = ""
count = 0
for i in li:
    if len(i) != 0:
        count+=1
print(count)
'''