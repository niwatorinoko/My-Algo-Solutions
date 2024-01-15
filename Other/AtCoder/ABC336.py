"""
#A
n = int(input())
print("L" + "o"*n + "ng")
"""
"""
#B
n = int(input())
binNum = bin(n)[2:]

ans = 0
for i in range(len(binNum)-1,-1,-1):
    if binNum[i] == "0":
        ans += 1
    else:
        break

print(ans)
"""

"""
#C
def find_nth_good_number(N):
    count = 0
    i = 0
    while True:
        if all(digit in ["0", "2", "4", "6", "8"] for digit in str(i)):
            count += 1
            if count == N:
                return i
        i += 1

n = int(input())
ans = find_nth_good_number(n)
print(ans)
"""