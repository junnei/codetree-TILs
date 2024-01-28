def solution(arr):
    for i in range(n):
        if arr[i] < 0:
            arr[i] = -arr[i]

n = int(input())
arr = list(map(int, input().split()))

solution(arr)
print(*arr)