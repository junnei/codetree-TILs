def solution(a, b):
    cnt = 0
    for i in range(a, b+1):
        if is_prime(i) and is_sum_demical(i):
                cnt += 1
    return cnt

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_sum_demical(n):
    if sum([int(i) for i in str(n)]) % 2 == 0:
        return True
    else:
        return False


a, b = map(int, input().split())

print(solution(a, b))