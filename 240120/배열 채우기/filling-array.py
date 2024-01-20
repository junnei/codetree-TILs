import sys

input = sys.stdin.readline

arr = list(map(int, input().split()))

data = list()

for i in arr:
    if i == 0:
        break
    data.append(i)

for i in range(len(data)-1, -1, -1):
    print(data[i],end=" ")