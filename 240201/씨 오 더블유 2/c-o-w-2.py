n = int(input())
arr = list(input())

cnt = 0

for i in range(n):
    if arr[i] == "C":
        for j in range(i+1, n):
            if arr[j] == "O":
                for k in range(j+1, n):
                    if arr[k] == "W":
                        cnt += 1
print(cnt)