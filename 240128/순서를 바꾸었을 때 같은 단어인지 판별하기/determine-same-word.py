a, b = [list(input()) for _ in range(2)]

a.sort()
b.sort()

if a==b:
    print("Yes")
else:
    print("No")