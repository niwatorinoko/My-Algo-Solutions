#AtCoder Beginner Contest 340
#2024/2/10
"""
#メモ！！
N, M = map(int, input().split())

A = input()
A_list = list(map(int, A.split()))
"""
"""
#A
s = input().split(".")
print(s[-1])
"""
"""
#B
N = int(input())
A = input()
A_list = list(map(int, A.split()))
if A_list[0] < 0:
    ans = 0
else:
    ans = A_list[0]
for i in range(1, len(A_list)):
    if A_list[i] < 0 and ans < abs(A_list[i]):
        ans += abs(A_list[i])-ans
    ans += A_list[i]
print(ans)
"""

"""
#A
A, B, D = map(int, input().split())
for i in range(A, B+1, D):
    print(i, end = " ")
"""
"""
#B
Q = int(input())
li = []
for i in range(Q):
    q = input()
    query = list(map(int, q.split()))
    if query[0] == 1:
        li.append(query[1])
    else:
        print(li[-query[1]])
"""

#C
def divide_and_round(n):
    floor_value = n // 2
    ceil_value = (n + 1) // 2

    return [floor_value, ceil_value]

N = int(input())
ans = N
li = divide_and_round(N)

while max(li) >= 2:
    num = max(li)
    if li[0] >= 2:
        ans += li[0]
    if li[1] >= 2:
        ans += li[1]
    #ans += num
    li = divide_and_round(num)
    print(ans, li)

print(ans)

