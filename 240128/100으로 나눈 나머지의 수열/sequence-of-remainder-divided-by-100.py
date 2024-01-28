def solution(n):
    if n <= 2:
        return 2**n
        
    return (solution(n-1) * solution(n-2)) % 100

n = int(input())
print(solution(n))