x, y = map(int, input().split())

def is_magic_number(n):
    numbers = [0] * 10
    for i in str(n):
        numbers[int(i)] += 1
    return (sum(numbers) - max(numbers) == 1)
cnt = 0
for i in range(x, y+1):
    if is_magic_number(i):
        cnt += 1
print(cnt)