n = int(input())
arr = list(map(int, input().split()))

board = [
    []
    for _ in range(n)
]
for idx, num in enumerate(arr):
    board[num].append(idx)


found = False
for count in board:
    if len(count) == 0:
        continue
    else:
        if found:
            if len(count)==1:
                print(count[0]+1)
            else:
                print(-1)
        else:
            found = True