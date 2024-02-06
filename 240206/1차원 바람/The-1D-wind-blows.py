n, m, q = map(int, input().split())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
commands = [
    input().split()
    for _ in range(q)
]

def next_available(i, d, arr, v):
    found = False
    for a, b in zip(arr[i], arr[i+v]):
        if a==b:
            found = True
            break
    if found:
        move(i+v, "L" if d == "R" else "R", arr, v)
    return

def move(i, d, arr, v):
    if d == "L":
        arr[i] = [arr[i][-1]] + arr[i][:-1]
    else:
        arr[i] = arr[i][1:] + [arr[i][0]]

    if v == 0:
        for v in [-1, 1]:
            next_available(i, d, arr, v)
    else:
        if 0<=i+v<n:
            next_available(i, d, arr, v)
        
for r, d in commands:
    move(int(r)-1, d, arr, 0)

for row in arr:
    print(*row)