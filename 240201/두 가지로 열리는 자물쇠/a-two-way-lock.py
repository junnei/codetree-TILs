n = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

cnt = 0

def get_distance(a, b):
    return min(abs(a - b), n - abs(a - b))
        
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if (get_distance(i, a1)<=2 and get_distance(j, b1)<=2 and get_distance(k, c1)<=2) \
            or (get_distance(i, a2)<=2 and get_distance(j, b2)<=2 and get_distance(k, c2)<=2):
                cnt += 1
print(cnt)