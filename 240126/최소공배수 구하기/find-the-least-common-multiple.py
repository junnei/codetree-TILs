def get_minimax(n, m):
    for i in range(max(n, m), n*m):
        if i % n == 0 and i % m == 0:
            print(i)
            return i

n, m = map(int, input().split())
get_minimax(n, m)