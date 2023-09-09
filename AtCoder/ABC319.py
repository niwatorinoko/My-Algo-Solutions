"""
#A
name = input()
name_li = ["tourist","ksun48","Benq" ,"Um_nik","apiad","Stonefeang" ,"ecnerwala","mnbvmar" ,"newbiedmy","semiexp"]
score_li = [3858,3679,3658,3648,3638,3630,3613,3555,3516,3481]

print(score_li[name_li.index(name)])
"""

"""
#B
n = int(input())
for i in range(n+1):
    for j in range(1,10):
        if i % (n/j) == 0:
            print(str(j), end="")
            break
    else:
        print("-",end="")
"""

#D
def widthcheck(li,w,m):
    c = 0
    ans = 0
    for i in li:
        c += i+1
        if c == w:
            c = 0
            ans += 1
        elif c > w:
            c = 0
            c += i+1
            ans += 1

    if ans == 0:
        ans = 1
    if ans == m:
        #print("True",ans)
        return True
    #print("False",ans)
    return False

n, m=input().split()
n = int(n)
m = int(m)
l = input().split()
li = []
for i in range(n):
    li.append(int(l[i]))
'''
print(widthcheck(li,1,m))
print(widthcheck(li,10000000009,m))
print(widthcheck(li,213,m))
print(widthcheck(li,sum(li)+1*(n-1),m))
'''

l, r = m, sum(li)+1*(n-1)
while r-l > 1:
    #print(l,r)
    if widthcheck(li,(l+r)//2,m):
        l = (l+r)//2
    else:
        r = (l+r)//2
if widthcheck(li,l,m) == False:
    if widthcheck(li,sum(li)+1*(n-1),m):
        print(sum(li)+1*(n-1))
else:
    print(l)