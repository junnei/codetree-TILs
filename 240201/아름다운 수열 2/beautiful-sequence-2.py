n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

from itertools import permutations
arr = list(map(list, permutations(b)))

cnt = 0

for i in range(n-m+1):
    if a[i:i+m] in arr:
        cnt += 1
print(cnt)