n = int(input())
arr = list(map(int, input().split()))

board = [0] * 101
 
for i in range(n):
    if board[arr[i]] == 0:
        board[arr[i]] = i + 1
    elif board[arr[i]] != -1:
        board[arr[i]] = -1

answer = -1
found = False
for count in board:
    if count == 0:
        continue
    else:
        if found:
            answer = count
            break
        found = True
print(answer)