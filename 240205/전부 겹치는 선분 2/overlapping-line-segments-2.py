n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def solution(arr):
    min_end = 100
    max_start = 0
    for a, b in arr:
        min_end = min(min_end, b)
        max_start = max(max_start, a)
        
    if max_start <= min_end:
        return True
    return False

found = False
for i in range(n):
    if solution(arr[:i] + arr[i+1:]):
        found = True
if found:
    print("Yes")
else:
    print("No")