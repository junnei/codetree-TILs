import sys

input = sys.stdin.readline

n = int(input())
answer = 0

for i in range(n):
    if i%2==0 or i%3 ==0 or i%5 == 0:
        continue
    else:
        answer += 1
print(answer)