import sys

input = sys.stdin.readline

arr = list(map(int, input().split()))
result = [0]*7

for num in arr:
    result[num] += 1
    
for i in range(1, len(result)):
    print(f"{i} - {result[i]}")