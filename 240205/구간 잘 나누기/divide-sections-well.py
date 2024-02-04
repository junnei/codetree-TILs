n, m = map(int, input().split())
arr = list(map(int, input().split()))

from itertools import combinations


min_val = 10000
for blocks in combinations(range(1,n),m-1):
    last_index = 0
    max_sum = 0
    for block in list(blocks)+[n]:
        sum_val = sum(arr[last_index:block])
        last_index = block
        max_sum = max(max_sum, sum_val)
    min_val = min(min_val, max_sum)
print(min_val)