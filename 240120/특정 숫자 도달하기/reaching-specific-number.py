import sys

input = sys.stdin.readline

arr = list(map(int, input().split()))
found = False
for idx, i in enumerate(arr):
    if i >= 250:
        found = True
        print(sum(arr[:idx]),f"{sum(arr[:idx])/idx:.1f}")
        break
if found == False:
    print(sum(arr),f"{sum(arr)/10:.1f}")