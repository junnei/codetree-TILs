import sys

input = sys.stdin.readline

arr = [
    input().rstrip() for _ in range(3)
]

chars = list(set([j for i in arr for j in i]))

solo_win = set()
for i in range(3):
    if arr[i][0] == arr[i][1] == arr[i][2]:
        solo_win.add(arr[i][0])

for i in range(3):
    if arr[0][i] == arr[1][i] == arr[2][i]:
        solo_win.add(arr[0][i])

print(len(solo_win))

duo_win = set()
for a in range(len(chars)):
    for b in range(a + 1, len(chars)):
        is_win = False
        for i in range(3):
            found = True
            for j in range(3):
                if not (arr[i][j] == chars[a] or arr[i][j] == chars[b]):
                    found = False
                    break
            if found:
                if not arr[i][0] == arr[i][1] == arr[i][2]:
                    is_win = True

        for i in range(3):
            found = True
            for j in range(3):
                if not (arr[j][i] == chars[a] or arr[j][i] == chars[b]):
                    found = False
                    break
            if found:
                if not arr[0][i] == arr[1][i] == arr[2][i]:
                    is_win = True
        
        for i in [True, False]:
            found = True
            for j in range(3):
                if not (arr[j if i else 2 - j][j] == chars[a] or arr[j if i else 2 - j][j] == chars[b]):
                    found = False
                    break
            if found:
                if not arr[0][0] == arr[1][1] == arr[2][2]:
                    is_win = True
        if is_win:
            duo_win.add(tuple(sorted([chars[a], chars[b]])))
print(len(duo_win))