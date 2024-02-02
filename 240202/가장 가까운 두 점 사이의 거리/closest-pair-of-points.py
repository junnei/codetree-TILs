n = int(input())
points = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

import sys

MAX_INT = sys.maxsize

min_dist = MAX_INT

for i in range(n):
    for j in range(i+1, n):
        dist = (points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2
        min_dist = min(min_dist, dist)

print(min_dist)