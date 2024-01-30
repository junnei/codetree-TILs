n, m = map(int, input().split())
MAX_TIME = 1000000

a_pos = [0 for _ in range(MAX_TIME + 1)]
b_pos = [0 for _ in range(MAX_TIME + 1)]

a_time = 1
for _ in range(n):
    v, t = map(int, input().split())
    for i in range(t):
        a_pos[a_time] = a_pos[a_time - 1] + v
        a_time += 1
    
b_time = 1
for _ in range(m):
    v, t = map(int, input().split())
    for i in range(t):
        b_pos[b_time] = b_pos[b_time - 1] + v
        b_time += 1

cnt = 0
last_result = set()

for i in range(1, b_time):
    result = set()
    max_pos = max(a_pos[i], b_pos[i])
    if a_pos[i] == max_pos:
        result.add(0)
    if b_pos[i] == max_pos:
        result.add(1)

    if result != last_result:
        last_result = result
        cnt += 1
print(cnt)