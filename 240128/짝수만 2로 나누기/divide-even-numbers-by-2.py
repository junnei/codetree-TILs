def solution(arr):
    for i in range(len(arr)):
        if arr[i]%2 == 0:
            arr[i] //= 2
    print(*arr)

n = int(input())
arr = list(map(int, input().split()))

solution(arr[:])