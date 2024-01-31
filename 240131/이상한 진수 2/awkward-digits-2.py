n = list(input())

found = False

for i in range(len(n)):
    if n[i] == '0':
        n[i] = '1'
        found = True
        break

if not found:
    n[-1] = '0'

result = 0

for i in map(int, n):
    result = result*2 + i
print(result)