n, m, p = map(int, input().split())
arr = [
    input().split()
    for _ in range(m)
]

people = [0] * n

if arr[p-1][1] != '0':
    for i in range(p-1, m):
        people[ord(arr[i][0])-65] = 1


    for i in range(n):
        if people[i] == 0:
            print(chr(i+65), end=" ")