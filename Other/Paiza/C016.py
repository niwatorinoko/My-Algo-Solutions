s = input()
leet =  {'A':4,'E':3,'G':6,'I':1,'O':0,'S':5,'Z':2}
ans = ""
for i in s:
    if i in leet:
        ans += str(leet[i])
    else:
        ans += i
print(ans)