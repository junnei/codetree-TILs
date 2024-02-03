x, y = map(int, input().split())

def is_magic_number(n):
    return len(set(str(n))) == 2
cnt = 0
for i in range(x, y+1):
    if is_magic_number(i):
        cnt += 1
print(cnt)