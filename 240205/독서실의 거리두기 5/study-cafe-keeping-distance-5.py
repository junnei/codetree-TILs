n = int(input())
arr = list(map(int, list(input())))


def get_max_dist_idx(arr):
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
    
    return dist.index(max(dist))


arr[get_max_dist_idx(arr)] = 1
dist = []
last_index = -1
for i in range(n):
    if arr[i] == 1:
        if last_index != -1:
            dist.append(i - last_index)
        last_index = i
print(min(dist))