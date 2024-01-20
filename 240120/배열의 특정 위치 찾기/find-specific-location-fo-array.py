import sys

input = sys.stdin.readline

arr = list(map(int, input().split()))

sum_val = 0
sum_three = 0
cnt = 0
cnt_three = 0

for i in range(len(arr)):
    cnt += 1
    if cnt % 2 == 0:
        sum_val += arr[i]
    
    if cnt % 3 == 0:
        sum_three += arr[i]
        cnt_three += 1
        
print(sum_val, round(sum_three/cnt_three, 1))