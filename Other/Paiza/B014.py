def print_front_view(X, Y, Z, data):
    front_view = [['.' for _ in range(Y)] for _ in range(Z)]

    for z in range(Z):
        for y in range(Y):
            for x in range(X):
                if data[z][x][y] == '#':
                    front_view[z][y] = '#'
                    break

    for row in reversed(front_view):
        print(''.join(row))

X, Y, Z = map(int, input().split())
data = []

for _ in range(Z):
    layer = []
    for _ in range(X):
        layer.append(input())
    data.append(layer)
    input()

print_front_view(X, Y, Z, data)
