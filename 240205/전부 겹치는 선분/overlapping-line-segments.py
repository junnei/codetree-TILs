n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def solution():
    for i in range(1, 101):
        found = True
        for a, b in arr:
            if a > i or i > b:
                found = False
        if found:
            return True
    return False

if solution():
    print("Yes")
else:
    print("No")