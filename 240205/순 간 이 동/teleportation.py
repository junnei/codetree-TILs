a, b, x, y = map(int, input().split())

d1 = abs(a-b)
d2 = abs(a-x) + abs(y-b)
d3 = abs(a-y) + abs(x-b)

print(min(d1, d2, d3))