import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
new_arr = [num**2 for num in arr]
print(*new_arr)