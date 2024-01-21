import sys

input = sys.stdin.readline

n1, n2 = tuple(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if n1<n2:
    print("No")
found = False
for i in range(n1-n2+1):
    if a[i:i+n2] == b:
        found = True
        break
if found:
    print("Yes")
else:
    print("No")