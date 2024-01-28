def solution(a, b):
    low, high = (a, b) if a < b else (b, a)

    high += 25
    low *= 2
    return low, high

a, b = map(int, input().split())

print(*solution(a, b))