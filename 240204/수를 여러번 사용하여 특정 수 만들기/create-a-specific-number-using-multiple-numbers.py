a, b, c = map(int, input().split())

max_val = 0
for i in range(c//a+1):
    for j in range(c//b+1):
        val = a*i+b*j
        if val <= c:
            max_val = max(max_val, val)
print(max_val)