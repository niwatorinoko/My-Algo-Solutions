# s = input()
# ans = ""
# for i in s:
#     if i == "2":
#         ans += "2"
# print(ans)

# n = int(input())
# words = dict()
# for _ in range(n):
#     word = input()
#     words[len(word)] = word
# words = [v for k, v in sorted(words.items())]
# print("".join(words))

# s = input()
# # s = "W" * (300000 - 1) + "A"
# s = list(s)
# i = 0
# while i < len(s) - 1:
#     if s[i] == 'W' and s[i + 1] == 'A':
#         s[i] = 'A'  # W → A に変更
#         s[i + 1] = 'C'  # A → C に変更
#         i = max(0, i - 1)  # 直前に戻って再確認
#     else:
#         i += 1
# print(''.join(s))

s = input()
# s = ")" * 100000 + "(" * 100000
kakko = {"(":")", "[":"]", "<":">"}
stack = []
for c in s:
    if not stack and c not in kakko:
        print("No")
        exit()
    elif c in kakko or not stack:
        stack.append(c)
    else:
        if kakko[stack[-1]] == c:
            stack.pop()

if stack:
    print("No")
else:
    print("Yes")