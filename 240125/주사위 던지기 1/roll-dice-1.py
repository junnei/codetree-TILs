from itertools import combinations, permutations, product

n, m = map(int, input().split())

all_cases = product(*[range(1, 7) for _ in range(n)])

if m == 1:
    for i in all_cases:
        print(*i)
elif m == 2:
    for i in set(map(lambda x : tuple(sorted(x)), all_cases)):
        print(*i)

elif m == 3:
    for i in all_cases:
        if len(set(i)) != 1:
            print(*i)