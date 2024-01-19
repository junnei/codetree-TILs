import sys

input = sys.stdin.readline

n = int(input())
prod = n
cnt = 0

for i in range(1,n+1):
    prod /= i
    cnt+=1
    if prod <= 1:
        break
print(cnt)