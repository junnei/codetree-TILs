import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(float, input().split()))

avg = round(sum(arr)/len(arr), 1)
print(avg)

if avg>=4.0:
    print("Perfect")
elif avg>=3.0:
    print("Good")
else:
    print("Poor")