n = int(input())
arr = list(map(int, list(input())))


def get_max_dist(arr):
    dist = [0] * n

    cnt = 0
    for i in range(n):
        if arr[i] == 1:
            dist[i] = 0
            j = 1
            while i >= j:
                if dist[i-j] <= j:
                    break
                dist[i - j] = j
                j += 1
            cnt = 0
        else:
            cnt += 1
            dist[i] = cnt
    return max(dist)


max_val = 0
for i in range(n):
    if arr[i] == 0:
        val = get_max_dist(arr[:i] + [1] + arr[i+1:])
        max_val = max(max_val, val)
print(max_val)