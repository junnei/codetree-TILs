import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

while True:
    max_val = -sys.maxsize
    max_idx = 0

    for idx, num in enumerate(arr):
        if num > max_val:
            max_val = num
            max_idx = idx
    print(max_idx + 1, end=" ")
    if max_idx == 0:
        break
    arr = arr[:max_idx]