def solution(n):
    if n==1:
        return arr[1]
        
    return get_lcm(solution(n-1), arr[n])

def get_gcd(a, b):
    result = 0
    for i in range(1, min(a, b)+1):
        if a % i == 0 and b % i == 0:
            result = i
    return result

def get_lcm(a, b):
    gcd = get_gcd(a, b)
    return (a * b) // gcd

n = int(input())
arr = [0] + list(map(int, input().split()))
print(solution(n))