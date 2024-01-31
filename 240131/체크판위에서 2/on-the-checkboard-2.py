import sys

INT_MIN = -sys.maxsize

r, c = map(int, input().split())
arr = [
    list(input().split())
    for _ in range(r)
]

cnt = 0
def start(x, y, color, n):
    global cnt
    if n == 3:
        cnt += 1
    for i in range(x+1, r):
        for j in range(y+1, c):
            if arr[i][j] != color:
                start(i, j, arr[i][j], n+1)

x, y, color, n = 0, 0, arr[0][0], 0
start(x, y, color, n)
print(cnt)