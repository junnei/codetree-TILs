n = int(input())
arr = [
    input().split()
    for _ in range(n)
]

score = [0] * 3
state = 0

def check_rank(score):
    max_val = max(score)
    num = score.count(max_val)
    if num == 1:
        return 1 + score.index(max_val)
    elif num == 2:
        i = 0
        for idx, val in enumerate(score):
            if val != max_val:
                i = idx
        return 4 + i
    else:
        return 0
cnt = 0
for c, s in arr:
    if c == "A":
        score[0] += int(s)
    elif c == "B":
        score[1] += int(s)
    else:
        score[2] += int(s)
    
    rank = check_rank(score)
    
    if state != rank:
        cnt += 1
        state = rank
print(cnt)