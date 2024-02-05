n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def solution():
    for i in range(1, 101):
        for a, b in arr:
            if a > i or i > b:
                return False
    return True

if solution():
    print("Yes")
else:
    print("No")