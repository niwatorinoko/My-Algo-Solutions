import random

print("1～10の中でランダムで整数を１つ選びました。３回以内にその数字を当ててください。")
ans = random.randrange(1,11)

flag = False

for i in range(3):
    n = int(input("予想する整数を入力してください : "))
    if n == ans:
        print("正解です！おめでとうございます！")
        flag = True
        break
    elif n > ans:
        print("入力した数は正解より大きいです。")
    elif n < ans:
        print("入力した数は正解より小さいです。")
    
if flag == False:
    print(f"残念！正解は {ans} でした。")