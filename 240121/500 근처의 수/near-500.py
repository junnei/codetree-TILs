import sys

input = sys.stdin.readline

arr = list(map(int, input().split()))

maximin_val = 1
minimax_val = 1000

for num in arr:
    if num < 500 and num > minimax_val:
        minimax_val = num
    if num > 500 and num < maximin_val:
        maximin_val = num

print(minimax_val, maximin_val)