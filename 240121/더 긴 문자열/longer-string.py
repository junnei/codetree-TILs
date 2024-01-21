import sys

input = sys.stdin.readline

arr = input().rstrip().split()

long_val = ""
if len(arr[1]) > len(arr[0]):
    long_val = arr[1]
elif len(arr[0]) > len(arr[1]):
    long_val = arr[0]
else:
    long_val = "same"

print(long_val, end=" ")
if long_val != "same":
    print(len(long_val))