n = int(input())
points = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

import sys

MIN_INT = -sys.maxsize
MAX_INT = sys.maxsize

min_area = MAX_INT

for i in range(n):
    min_x, max_x = MAX_INT, MIN_INT
    min_y, max_y = MAX_INT, MIN_INT
    for x, y in points[:i]+points[i+1:]:
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)
    area = (max_x-min_x)*(max_y-min_y)
    min_area = min(min_area, area)

print(min_area)