s = input()
for i in range(1,len(s)+1):
    if i%2 == 0:
        if s[i-1] != "0":
            print("No")
            break
else:
    print("Yes")