N, K, P, T = map(int, input().split())

queries = [tuple(map(int, input().split())) for _ in range(T)]

queries.sort(lambda x: x[0])

infect = [0 for _ in range(N+1)]

infect[P] = K+1

for t, x, y in queries:
    if infect[x] >= 2:
        infect[x] -= 1
        
        if infect[y] >= 2:
            infect[y] -= 1
        elif infect[y] == 0:
            infect[y] = K+1
    else:
        if infect[y] >= 2:
            infect[y] -= 1
            
            if infect[x] == 0:
                infect[x] = K+1

for i in infect[1:]:
    print(0 if i == 0 else 1, end="")