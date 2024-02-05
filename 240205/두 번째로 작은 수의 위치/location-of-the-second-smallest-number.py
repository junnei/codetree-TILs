n = int(input())
arr = list(map(int, input().split()))

num = sorted(arr)[1]
if arr.count(num) != 1:
    print(-1)
else:
    print(arr.index(num)+1)