import sys

input = sys.stdin.readline

arr = list(map(int, input().split()))
result = [0]*11

for num in arr:
    if num == 0:
        break
    result[num//10] += 1
    
for i in range(len(result)-1, 0, -1):
    print(f"{i*10} - {result[i]}")