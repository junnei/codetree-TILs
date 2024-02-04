n = int(input())
arr = list(map(int, input().split()))

from itertools import permutations

def solution():
    for nums in permutations(range(1,n+1)):
        found = True
        for i in range(1, n):
            if arr[i-1] != nums[i]+nums[i-1]:
                found = False
                break
        if found:
            return nums

print(*solution())