#AtCoder Beginner Contest 339
#2024/2/3
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
#E 解いてる途中
count = 0
ans = 0

N, D = map(int, input().split())
A = input()
A_list = list(map(int, A.split()))
for i in range(1, len(A_list)):
    if abs(A_list[i]-A_list[i-1]) <= D:
        count += 1
    else:
        ans = max(ans, count)
        count = 0
ans = max(ans, count)
print(ans+1)
"""

H, W, N = map(int, input().split())
grid = [["." for _ in range(W)] for _ in range(H)]
x, y = 0, 0
direction = 0
    
movements = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
for _ in range(N):
    if grid[x][y] == ".":
        grid[x][y] = "#"
        direction = (direction + 1) % 4
    elif grid[x][y] == "#":
        grid[x][y] = "."
        direction = (direction - 1) % 4

    dx, dy = movements[direction]
    x = (x + dx) % H
    y = (y + dy) % W

for row in grid:
    print(''.join(row))
