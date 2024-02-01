n, k = map(int, input().split())
arr = [0 for _ in range(10001)]

for _ in range(n):
    pos, val = input().split()
    arr[int(pos)] = 1 if val == "G" else 2
    
import sys
INT_MIN = -sys.maxsize

max_val = INT_MIN

for i in range(1, 10000-k):
    sum_val = sum(arr[i:i+k+1])
    if sum_val > max_val:
        max_val = sum_val

print(max_val)