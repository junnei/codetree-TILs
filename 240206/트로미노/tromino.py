n, m = map(int, input().split())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]


def get_max(arr):
    return max(
    arr[0][0] + arr[0][1] + arr[0][2],
    arr[0][0] + arr[0][1] + arr[1][0],
    arr[0][0] + arr[0][1] + arr[1][1],
    arr[0][0] + arr[1][0] + arr[1][1],
    arr[0][0] + arr[1][0] + arr[2][0],

    arr[0][1] + arr[0][2] + arr[1][1],
    arr[0][1] + arr[0][2] + arr[1][2],
    arr[0][1] + arr[1][1] + arr[1][0],
    arr[0][1] + arr[1][1] + arr[1][2],
    arr[0][1] + arr[1][1] + arr[2][1],

    arr[0][2] + arr[1][2] + arr[1][1],
    arr[0][2] + arr[1][2] + arr[2][2],

    arr[1][0] + arr[1][1] + arr[2][0],
    arr[1][0] + arr[1][1] + arr[2][1],
    arr[1][0] + arr[1][1] + arr[1][2],
    arr[1][0] + arr[2][0] + arr[2][1],

    arr[1][1] + arr[1][2] + arr[2][2],
    arr[1][1] + arr[1][2] + arr[2][1],
    arr[1][1] + arr[2][1] + arr[2][0],
    arr[1][1] + arr[2][1] + arr[2][2],

    arr[1][2] + arr[2][2] + arr[2][1],
    arr[2][0] + arr[2][1] + arr[2][2]
    )

max_val = 0
for i in range(n-2):
    for j in range(n-2):
        max_val = max(max_val, get_max([row[j:j+3] for row in arr[i:i+3]]))
print(max_val)