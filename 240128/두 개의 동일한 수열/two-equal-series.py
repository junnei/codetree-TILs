n = int(input())
a, b = [list(map(int, input().split())) for _ in range(2)]

if set(a) == set(b):
    print("Yes")
else:
    print("No")