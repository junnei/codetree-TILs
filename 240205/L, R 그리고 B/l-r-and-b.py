arr = [
    list(input())
    for _ in range(10)
]
n = 10
l, b, r = [0, 0], [0, 0], [0, 0]
for i in range(n):
    for j in range(n):
        if arr[i][j] == "B":
            b = [i, j]
        if arr[i][j] == "L":
            l = [i, j]
        if arr[i][j] == "R":
            r = [i, j]
count = 0
if (l[0] == b[0] == r[0] and (l[1]-r[1])*(b[1]-r[1]) < 0) \
or (l[1] == b[1] == r[1] and (l[0]-r[0])*(b[0]-r[0]) < 0):
    count += 2

print(abs(l[0]-b[0]) + abs(l[1]-b[1]) - 1 + count)