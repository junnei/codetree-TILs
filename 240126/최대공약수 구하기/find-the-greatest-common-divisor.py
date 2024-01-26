def get_maximin(n, m):
    result = 0
    for i in range(1, min(n, m) + 1):
        if n % i == 0 and m % i == 0:
            result = i
    print(result)

n, m = map(int, input().split())
get_maximin(n, m)