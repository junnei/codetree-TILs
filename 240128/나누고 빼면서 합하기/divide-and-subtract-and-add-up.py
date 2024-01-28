def solution(n, m, arr):
    result = arr[0]
    while m != 1:
        result += arr[m - 1]
        if m % 2 == 1:
            m -= 1
        else:
            m //= 2

    return result

n, m = map(int, input().split())
arr = list(map(int, input().split()))

print(solution(n, m, arr))