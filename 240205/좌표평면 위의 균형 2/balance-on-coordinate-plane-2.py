n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

MAX_SIZE = 100

import sys

min_val = sys.maxsize

for i in range(1, MAX_SIZE+1, 2):
    for j in range(1, MAX_SIZE+1, 2):
        quadrant = [0] * 4
        for x, y in arr:
            if x < i:
                if y < j:
                    quadrant[0] += 1
                else:
                    quadrant[1] += 1
            else:
                if y < j:
                    quadrant[2] += 1
                else:
                    quadrant[3] += 1
        min_val = min(min_val, max(quadrant))

print(min_val)