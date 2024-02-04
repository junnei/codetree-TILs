n = int(input())
arr = list(map(int, input().split()))



def solution():
    for start_num in range(1, arr[0]):
        found = True
        result = [start_num]
        for i in range(n-1):
            num = arr[i] - result[i]
            if num <= 0 or num in result:
                found = False
                break
            result.append(num)
        if found:
            return result
print(*solution())