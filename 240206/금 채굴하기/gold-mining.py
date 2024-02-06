n, m = map(int, input().split())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]


def is_range(a, b):
    return 0<=a<n and 0<=b<n

def get_score(a, b, k):
    limit = k*k+(k+1)*(k+1)

    cnt = 0
    for i in range(a-k, a+k+1):
        for j in range(b-k, b+k+1):
            if abs(i-a)+abs(j-b) <= k and is_range(i, j):
                if arr[i][j] == 1:
                    cnt += 1

    if cnt*m >= limit:
        return cnt
    else:
        return 0

max_val = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            max_val = max(max_val, get_score(i, j, k))
print(max_val)