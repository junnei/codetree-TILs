def solution(arr):
    if len(arr) == 1:
        return arr[0]
    
    return max(solution(arr[:len(arr)//2]), solution(arr[len(arr)//2:]))

n = int(input())
arr = list(map(int, input().split()))
print(solution(arr))