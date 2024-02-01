n = int(input())
MAX_POS = 100
arr = [0 for _ in range(MAX_POS+1)]

for _ in range(n):
    pos, val = input().split()
    arr[int(pos)] = 1 if val == "G" else 2

max_val = 0
for i in range(MAX_POS):
    for j in range(i+1, MAX_POS+1):
        cnt_g, cnt_h = 0, 0
        max_idx, min_idx = 0, 100
        for idx, item in enumerate(arr[i:j+1]):
            if item == 1:
                cnt_g += 1
                if idx > max_idx:
                    max_idx = idx
                if idx < min_idx:
                    min_idx = idx
            elif item == 2:
                cnt_h += 1
                if idx > max_idx:
                    max_idx = idx
                if idx < min_idx:
                    min_idx = idx
        if cnt_g + cnt_h == j-i or cnt_g == cnt_h:
            if max_idx - min_idx > max_val:
                max_val = max_idx - min_idx
print(max_val)