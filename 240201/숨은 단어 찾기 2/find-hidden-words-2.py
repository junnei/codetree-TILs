n, m = map(int, input().split())

arr = [
    list(input())
    for _ in range(n)
]

to_find = "LEE"

def in_range(x, y):
    return 0<=x<n and 0<=y<m

def check_string(x, y, string):
    dxs = [1, 1, 0, -1, -1, -1, 0, 1]
    dys = [0, -1, -1, -1, 0, 1, 1, 1]
    n = len(string)
    cnt = 0

    for dx, dy in zip(dxs, dys):
        all_in_range = True
        for i in range(n):
            if not in_range(x+dx*i, y+dy*i):
                all_in_range = False

        if all_in_range:
            found = True
            for i, c in enumerate(string):
                if arr[x+dx*i][y+dy*i] != c:
                    found = False
            if found:
                cnt += 1
    return cnt

sum_val = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == to_find[0]:
            sum_val += check_string(i, j, to_find)

print(sum_val)