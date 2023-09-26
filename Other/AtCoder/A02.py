n, x = input().split()
x = int(x)
a = input().split()
for i in a:
    if int(i) == x:
        print("Yes")
        break
else:
    print("No")