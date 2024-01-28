def solution(n):
    if n <= 2:
        return n
        
    return solution(n//3) + solution(n-1)

n = int(input())
print(solution(n))