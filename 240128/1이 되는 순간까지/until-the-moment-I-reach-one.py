def solution(n, i):
    if n == 1:
        return i
    if n % 2 == 0:
        return solution(n//2, i+1)
    else:
        return solution(n//3, i+1)

n = int(input())
print(solution(n, 0))