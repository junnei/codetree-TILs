x, y = map(int, input().split())


max_val = 0
for i in range(x, y+1):
    val = sum(list(map(int, str(i))))
    max_val = max(max_val, val)
print(max_val)