import sys

input = sys.stdin.readline

arr = list(map(int, input().split()))
result = [0]*10

for num in arr:
    if arr == 0:
        break
    result[((num%100)//10)] += 1
    
for i in range(1, len(result)):
    print(f"{i} - {result[i]}")