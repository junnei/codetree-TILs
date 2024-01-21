import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort(reverse=True)
max_val = arr[0]
is_solo = True


for num in arr[1:]:
    if max_val == num:
        is_solo = False
    elif is_solo == True:
        print(max_val)
        break
    else:
        max_val = num
        is_solo = True

if is_solo == False:
    print(-1)