n, m = map(int, input().split())
MAX_TIME = 1000000

a_pos = [0 for _ in range(MAX_TIME + 1)]
b_pos = [0 for _ in range(MAX_TIME + 1)]

cur_t = 0
for _ in range(n):
    v, t = map(int, input().split())
    for i in range(t):
        a_pos[cur_t + i + 1] = a_pos[cur_t + i] + v
    cur_t += t
    
cur_t = 0
for _ in range(m):
    v, t = map(int, input().split())
    for i in range(t):
        b_pos[cur_t + i + 1] = b_pos[cur_t + i] + v
    cur_t += t


cur_sign = a_pos[1] > b_pos[1]
cnt = 0
for a, b in zip(a_pos[2:], b_pos[2:]):
    if a==0 and b==0:
        break
    if (a > b) != cur_sign:
        cnt += 1
        cur_sign = not cur_sign
print(cnt)