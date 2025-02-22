# taka, aoki = map(str, input().split())
# if taka == "sick" and aoki == "fine":
#   print(2)
# elif taka == "fine" and aoki == "fine":
#   print(4)
# elif taka == "sick" and aoki == "sick":
#   print(1)
# else:
#   print(3)



# S = input().strip()
# n = len(S)
# a_indices = [i for i in range(n) if S[i] == 'A']
# b_indices = [j for j in range(n) if S[j] == 'B']
# count = 0
    
# for i in a_indices:
#     for j in b_indices:
#         if j > i:
#             k = 2 * j - i 
#             if k < n and S[k] == 'C':
#                 count += 1

# print(count)

# N, M = map(int, input().split())
# edges = [tuple(map(int, input().split())) for _ in range(M)]

# self_loop_count = 0
# edge_set = set()
# multi_edge_count = 0
    
# for u, v in edges:
#     if u == v:
#         self_loop_count += 1
#     else:
#         edge_pair = (min(u, v), max(u, v))
#         if edge_pair in edge_set:
#             multi_edge_count += 1
#         else:
#             edge_set.add(edge_pair)
    
# print(self_loop_count + multi_edge_count)


N = int(input().strip())
S = input().strip()

ones_positions = [i for i, c in enumerate(S) if c == '1']
if not ones_positions:
    print(0)
    exit()
    
total_ones = len(ones_positions)
left_target = list(range(ones_positions[0], ones_positions[0] + total_ones))
right_target = list(range(ones_positions[-1] - total_ones + 1, ones_positions[-1] + 1))
middle_start = ones_positions[total_ones // 2] - total_ones // 2
middle_target = list(range(middle_start, middle_start + total_ones))
    
left_moves = sum(abs(ones_positions[i] - left_target[i]) for i in range(total_ones))
right_moves = sum(abs(ones_positions[i] - right_target[i]) for i in range(total_ones))
middle_moves = sum(abs(ones_positions[i] - middle_target[i]) for i in range(total_ones))
    
print(min(left_moves, right_moves, middle_moves))

