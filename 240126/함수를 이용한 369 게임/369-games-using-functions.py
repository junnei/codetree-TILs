def solution(a, b):
    cnt = 0
    for i in range(a, b + 1):
        if i % 3 == 0 or is_include_369(i):
            cnt += 1
    return cnt

def is_include_369(n):
    for i in map(int, str(n)):
        if i == 3 or i == 6 or i == 9:
            return True
    return False
    
a, b = map(int, input().split())

print(solution(a, b))