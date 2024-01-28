def solution(arr):
    if len(arr) == 1:
        return arr[0]

    return arr[0] * solution(arr[1:])

def sum_all(num):
    if num < 10:
        return num

    return sum_all(num//10) + num%10

arr = list(map(int, input().split()))
print(sum_all(solution(arr)))