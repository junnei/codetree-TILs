import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

result = [0]*1001

for num in arr:
    result[num] += 1

found = False
for i in range(1000, 0, -1):
    if result[i] == 1:
        found = True
        print(i)
        break
if not found:
    print(-1)