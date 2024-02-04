n = int(input())
arr = input()


for len_str in range(1, n+1):
    found = False
    for i in range(n-len_str+1):
        cnt = 0
        for j in range(n-len_str+1):
            if arr[i:i+len_str] == arr[j:j+len_str]:
                cnt += 1
                if cnt >= 2:
                    break
        if cnt >= 2:
            found = True
            break
    if not found:
        print(len_str)
        break