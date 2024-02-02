n = int(input())
points = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

max_area = 0

def is_parallel(a, b, c):
    if (a[0] == b[0] != c[0] or a[0] != b[0] == c[0] or a[0] == c[0] != b[0]) and (a[1] == b[1] != c[1] or a[1] != b[1] == c[1] or a[1] == c[1] != b[1]):
        return True 


for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if is_parallel(points[i], points[j], points[k]):
                area = (max(points[i][0], points[j][0], points[k][0]) - min(points[i][0], points[j][0], points[k][0]))*(max(points[i][1], points[j][1], points[k][1]) - min(points[i][1], points[j][1], points[k][1]))
                max_area = max(max_area, area)

print(max_area)