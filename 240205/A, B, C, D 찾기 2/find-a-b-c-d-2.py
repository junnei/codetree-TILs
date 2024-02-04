arr = list(map(int, input().split()))

MAX_NUM = 40

def get_answer():
    for a in range(1, MAX_NUM+1):
        for b in range(a, MAX_NUM+1):
            for c in range(b, MAX_NUM+1):
                for d in range(c, MAX_NUM+1):
                    if sorted([a, b, c, d, a+b, b+c, c+d, d+a, a+c, b+d, a+b+c, a+b+d, a+c+d, b+c+d, a+b+c+d]) == sorted(arr):
                        return a, b, c, d
print(*get_answer())