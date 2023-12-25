def sort_oranges(N, weights):
    sorted_weights = []

    for w in weights:
        if w < N:
            # 重さが N 未満の場合は、最小の N の倍数（N 自体）に仕分ける
            sorted_weight = N
        else:
            # 最も近い N の倍数を見つける
            lower = (w // N) * N
            upper = lower + N
            # 重さがちょうど中間の場合は大きい方に仕分ける
            sorted_weight = lower if w - lower < upper - w else upper
        
        sorted_weights.append(sorted_weight)
    
    return sorted_weights

# 入力データを読み込む
N, M = map(int, input().split())  # N:区切り、M:みかんの個数
weights = [int(input()) for _ in range(M)]  # 各みかんの重さ

# みかんを仕分ける
sorted_weights = sort_oranges(N, weights)

# 仕分け結果を出力する
for sw in sorted_weights:
    print(sw)
