n, m = map(int, input().split())
MAX_TIME = 1000000

a_pos = [0 for _ in range(MAX_TIME + 1)]
b_pos = [0 for _ in range(MAX_TIME + 1)]

a_time = 0
for _ in range(n):
    t, d = input().split()
    dx = 1 if d == "R" else -1
    for i in range(int(t)):
        a_pos[a_time + 1] = a_pos[a_time] + dx
        a_time += 1
    
b_time = 0
for _ in range(m):
    t, d = input().split()
    dx = 1 if d == "R" else -1
    for i in range(int(t)):
        b_pos[b_time + 1] = b_pos[b_time] + dx
        b_time += 1

min_time, max_time = min(a_time, b_time), max(a_time, b_time)
cnt = 0
for i in range(1, min_time + 1):
    if a_pos[i] == b_pos[i] and a_pos[i-1] != b_pos[i-1]:
        cnt += 1


if a_time < b_time:
    for i in range(min_time + 1, max_time + 1):
        if a_pos[min_time] == b_pos[i] and b_pos[i] != b_pos[i-1]:
            cnt += 1
else:
    for i in range(min_time + 1, max_time + 1):
        if b_pos[min_time] == a_pos[i] and a_pos[i] != a_pos[i-1]:
            cnt += 1
print(cnt)