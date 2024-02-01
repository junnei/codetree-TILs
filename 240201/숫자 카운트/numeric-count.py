n = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def get_count(a, b):
    cnt1, cnt2 = 0, 0

    for i in range(3):
        for j in range(3):
            if a[i] == b[j]:
                if i == j:
                    cnt1 += 1
                else:
                    cnt2 += 1
    return cnt1, cnt2

MAX_NUM = 10
cnt = 0
for i in range(1, MAX_NUM):
    for j in range(1, MAX_NUM):
        for k in range(1, MAX_NUM):
            found = True
            for num, cnt1, cnt2 in arr:
                if get_count(str(num),str(i)+str(j)+str(k)) != (cnt1, cnt2):
                    found = False
                    break
            if found:
                cnt += 1
print(cnt)