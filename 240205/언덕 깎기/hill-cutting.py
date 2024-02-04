n = int(input())
arr = [
    int(input())
    for _ in range(n)
]
MAX_HEIGHT = 100

def calculate(height, limit):
    if height < limit:
        return (limit - height)**2
    elif height > limit + 17:
        return (limit + 17 - height)**2
    else:
        return 0

answer = 10000000
for limit in range(min(arr), MAX_HEIGHT + 1 - 17):
    result = 0
    for height in arr:
        result += calculate(height, limit)
    answer = min(result, answer)
print(answer)