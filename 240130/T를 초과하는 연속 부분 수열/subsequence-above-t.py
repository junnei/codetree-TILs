n, t = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
cnt = 1

for i in range(n):
    if i>=1 and arr[i-1] > t and arr[i] > t:
        cnt += 1
    elif arr[i] > 3:
        cnt = 1
    else:
        cnt = 0
    
    if cnt > answer:
        answer = cnt
print(answer)