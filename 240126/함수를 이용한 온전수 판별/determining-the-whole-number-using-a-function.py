def solution(a, b):
    cnt = 0
    for i in range(a, b+1):
        if is_magic_number(i):
            cnt += 1
    return cnt

def is_magic_number(n):
    if n % 2 == 0 or n % 10 == 5:
        return False
    if n % 3 == 0 and n % 9 != 0:
        return False
    return True

a, b = map(int, input().split())

print(solution(a, b))