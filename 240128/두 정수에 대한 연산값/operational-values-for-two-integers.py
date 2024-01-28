def solution(a, b):
    is_right_order = a < b
    low, high = (a, b) if is_right_order else (b, a)

    high += 25
    low *= 2
    return (low, high) if is_right_order else (high, low)

a, b = map(int, input().split())

print(*solution(a, b))