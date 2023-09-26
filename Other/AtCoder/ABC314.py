'''
s = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"

n = int(input())
print(s[:n+2])
'''
'''
n = int(input())
ans = []
for i in range(n):
    c = int(input())
    a = input().split()
    for j in range(c):
        a[j] = int(a[j])
    ans.append(a)
x = int(input())

res = [[],[]]


for i in range(len(ans)):
    if x in ans[i]:
        res[0].append(len(ans[i]))
        res[1].append(i+1)
if len(res[0]) == 0:
    print(0)
    print()
else:
    minLen = min(res[0])
    jieguo = []

    #print(res)
    #print(len(res[0]))
    for i in range(len(res[0])):
        if res[0][i] == minLen:
            jieguo.append(res[1][i])
    print(len(jieguo))
    for i in jieguo:
        print(i, end=" ")
'''
n = int(input())
s = list(input())
q = int(input())
for i in range(q):
    a = input().split()
    if int(a[0]) == 1:
        s[int(a[1])-1] = a[2]
    elif int(a[0]) == 2:
        for j in range(len(s)):
            if s[j].isupper():
                s[j] = s[j].lower()
            
    elif int(a[0]) == 3:
        for j in range(len(s)):
            if s[j].islower():
                s[j] = s[j].upper()
for i in s:
    print(i,end="")