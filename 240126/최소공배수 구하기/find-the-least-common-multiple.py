from functools import reduce

def get_minimax(n, m, data):
    found = False
    for i in range(2, min(n, m) + 1):
        if n % i == 0 and m % i == 0:
            found = True
            get_minimax(n//i, m//i, data+[i])
            break
    if found == False:
        print(n * m * reduce(lambda x, y: x * y, data))

n, m = map(int, input().split())
get_minimax(n, m, [])