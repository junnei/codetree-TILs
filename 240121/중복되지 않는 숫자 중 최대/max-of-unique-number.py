import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

result = [0]*1001

for num in arr:
    result[num] += 1

answer = -1
for i in range(1000, 0, -1):
    if result[i] == 1:
        answer = i
        break

print(answer)