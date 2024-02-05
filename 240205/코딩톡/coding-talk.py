n, m, p = map(int, input().split())
arr = [
    input().split()
    for _ in range(m)
]

people = [0] * n
to_find = 0
if arr[p-1][1] != '0':
    for i in range(m):
        people[ord(arr[i][0])-65] = int(arr[i][1]) + 1
        if i == p-1:
            to_find = int(arr[i][1]) + 1

for i in range(n):
    if people[i] < to_find:
        print(chr(i+65), end=" ")