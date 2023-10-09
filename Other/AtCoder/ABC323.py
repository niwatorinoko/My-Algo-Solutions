"""s = input()
for i in range(1,len(s)+1):
    if i%2 == 0:
        if s[i-1] != "0":
            print("No")
            break
else:
    print("Yes")"""

"""def get_keys_from_value(d, target_value):
    return [key for key, value in d.items() if value == target_value]

n = int(input())
result = dict()
for i in range(n):
  s = list(input())
  s_Count = s.count("o")
  result[i] = s_Count
scoreSet = sorted(list(set(result.values())))

ans = []
for i in sorted(scoreSet):
    ans = get_keys_from_value(result, i) + ans

for i in ans:
   print(i+1, end=" ")"""

N, M = map(int, input().split())

A = input()
A_list = list(map(int, A.split()))

s=dict()

for i in range(N):
  score = list(input())
  s_Count = score.count("o")
  s[i] = s_Count
print(s)