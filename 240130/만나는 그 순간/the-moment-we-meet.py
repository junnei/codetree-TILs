n, m = map(int, input().split())

cur_a, cur_b = 0, 0
a_moves = []
b_moves = []
meet_at = -1

for _ in range(n):
    direction, value = input().split()
    a_moves.append([1 if direction=="R" else -1, int(value)])

for _ in range(m):
    direction, value = input().split()
    b_moves.append([1 if direction=="R" else -1, int(value)])

a = a_moves.pop(0)
b = b_moves.pop(0)

cnt = 0
while True:
    if a[1] <= 0:
        if len(a_moves) == 0:
            break
        a = a_moves.pop(0)
    if b[1] <= 0:
        if len(b_moves) == 0:
            break
        b = b_moves.pop(0)
    
    cur_a += a[0]
    a[1] -= 1
    
    cur_b += b[0]
    b[1] -= 1

    cnt += 1
    
    if cur_a == cur_b:
        meet_at = cnt
        break
print(meet_at)