n, m = map(int, input().split())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]


def is_sub_list(sub, arr):
    num = len(arr) - len(sub) + 1
    for i in range(num):
        if sub == arr[i:i+len(sub)]:
            return True
    return False

cnt = 0
for i in range(n):
    for j in range(n-m+1):
        if is_sub_list([arr[i][j]] * m, arr[i]):
            cnt += 1
            break
    
    for j in range(n-m+1):
        if is_sub_list([arr[j][i]] * m, [j[i] for j in arr]):
            cnt += 1
            break
print(cnt)