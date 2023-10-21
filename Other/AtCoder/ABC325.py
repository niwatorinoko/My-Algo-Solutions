"""
name = input().split()
print(name[0] + " " + "san")
"""
time = [0]*24
n = int(input())
for i in range(n):
    w, x = map(int, input("").split())
    flag9 = False
    flag18 = False
    for j in range(24):
        if x>=9 and x<18:
            if x==18 and flag18:
                x += 1
                continue
            if x == 18:
                flag18 = True
            time[j] += w
        x += 1
        if x==24:
            x = 0
print(max(time))