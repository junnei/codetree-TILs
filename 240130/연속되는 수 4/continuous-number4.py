n = int(input())
arr = [int(input()) for _ in range(n)]

answer = 0
cnt = 1
cur_sign = 0

for i in range(n):
    if i>=1 and arr[i]>arr[i-1]:
        cnt += 1
    else:
        cnt = 1
    
    if cnt > answer:
        answer = cnt
print(answer)