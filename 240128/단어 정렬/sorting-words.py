n = int(input())
arr = [input() for _ in range(n)]

arr.sort()
for string in arr:
    print(string)