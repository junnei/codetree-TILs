n = int(input())
arr = [
    input().split()
    for _ in range(n)
]

score = [0]*2
cnt = 0
last_state = 0
for c, s in arr:
    score[0 if c =='A' else 1] += int(s)
    state = 0
    if score[0] < score[1]:
        state = 1
    elif score[0] == score[1]:
        state = 2
    else:
        state = 3
    if state != last_state:
        last_state = state
        cnt += 1
print(cnt)