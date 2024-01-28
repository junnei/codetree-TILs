def solution(n):
    if n<=2:
        return n

    return solution(n - 2) + n

n = int(input())
print(solution(n))