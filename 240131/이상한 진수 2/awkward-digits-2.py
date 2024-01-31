n = list(input())

for i in range(len(n)):
    if n[i] == '0':
        n[i] = '1'
        break

result = 0

for i in map(int, n):
    result = result*2 + i
print(result)