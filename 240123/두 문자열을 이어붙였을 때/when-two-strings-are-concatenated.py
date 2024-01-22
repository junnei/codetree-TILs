arr = [input().rstrip() for _ in range(2)]

print('true' if ''.join(arr) == ''.join(arr[::-1]) else 'false')