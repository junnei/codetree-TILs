n = 19
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def check_win(x, y):
    dxs = [1, 1, 0, -1, -1, -1, 0, 1]
    dys = [0, -1, -1, -1, 0, 1, 1, 1]

    for dx, dy in zip(dxs, dys):
        found = True
        for i in range(1, 5):
            if in_range(x+dx*i, y+dy*i) and found:
                if arr[x][y] != arr[x+dx*i][y+dy*i]:
                    found = False
            else:
                found = False
        if found:
            return x+dx*2 + 1, y+dy*2 + 1
    return False

no_win = True
for i in range(n):
    for j in range(n):
        if no_win and arr[i][j] != 0:
            result = check_win(i, j)
            if result != False:
                no_win = False
                print(1 if arr[i][j]==1 else 2)
                print(*result)
if no_win:
    print(0)