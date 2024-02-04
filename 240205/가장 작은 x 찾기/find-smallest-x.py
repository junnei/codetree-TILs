n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

for i in range(1,10001):
    cnt = 1
    found = True
    for a, b in arr:
        num = i*(2**cnt)
        if a > num or num > b:
            found = False
            break
        cnt += 1
    if found:
        print(i)
        break