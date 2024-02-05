n = int(input())
arr = list(map(int, list(input())))

dist = []

first_index = 0
last_index = -1
for i in range(n):
    if arr[i] == 1:
        if last_index == -1:
            first_index = i
            last_index = i
        else:
            dist.append(i - last_index)
            last_index = i

last_index = n - 1 - last_index


if len(dist) > 0:
    max_val = max(dist)
    if max_val//2 >= first_index and max_val//2 >= last_index:
        val = dist.pop(dist.index(max_val))
        dist.extend([val-val//2, val//2])
        print(min(dist))
    else:
        new_dist = max(first_index, last_index)
        print(min(dist+[new_dist]))