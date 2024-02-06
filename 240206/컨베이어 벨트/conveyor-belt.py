n, t = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

t %= n*2
for i in range(t):
    a, b = [b[-1]] + a[:-1], [a[-1]] + b[:-1]
print(*a)
print(*b)