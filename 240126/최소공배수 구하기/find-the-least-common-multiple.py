from functools import reduce

def get_gcd(n, m):
    gcd = 0
    for i in range(1, min(n, m) + 1):
        if n % i == 0 and m % i == 0:
            gcd = i
    return gcd

def get_lcm(n, m):
    return n * m // get_gcd(n, m)

n, m = map(int, input().split())

print(get_lcm(n, m))