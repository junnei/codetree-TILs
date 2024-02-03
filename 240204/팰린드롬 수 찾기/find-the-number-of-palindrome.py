x, y = map(int, input().split())

def is_palindrome(n):
    return str(n) == str(n)[::-1]

cnt = 0
for i in range(x, y+1):
    if is_palindrome(i):
        cnt += 1
print(cnt)