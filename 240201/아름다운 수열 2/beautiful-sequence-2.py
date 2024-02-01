import sys 

MAX_SIZE = 100
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = [0] * (MAX_SIZE + 1)

for i in list(map(int, input().split())):
    b[i] += 1

if n<m:
    print(0)
    sys.exit()

cnt = 0

for i in range(n-m+1):
    temp = [0] * (MAX_SIZE + 1)
    for item in a[i:i+m]:
        temp[item] += 1
    if temp == b:
        cnt += 1
print(cnt)