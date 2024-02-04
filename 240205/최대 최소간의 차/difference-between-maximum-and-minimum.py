n, k = map(int, input().split())
arr = list(map(int, input().split()))

MAX_LIMIT = 10000

def calculate(number, limit):
    if number < limit:
        return limit - number
    elif number > limit + k:
        return number - limit - k
    else:
        return 0

min_cost = 1000000
for limit in range(1, MAX_LIMIT + 1):
    sum_cost = 0
    for num in arr:
        sum_cost += calculate(num, limit)
    min_cost = min(min_cost, sum_cost)
print(min_cost)