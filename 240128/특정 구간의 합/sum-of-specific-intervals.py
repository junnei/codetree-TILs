def solution(pairs):
    global arr
    for a1, a2 in pairs:
        print(sum(arr[a1:a2+1]))

n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))
pairs = [map(int, input().split()) for _ in range(m)]

solution(pairs)