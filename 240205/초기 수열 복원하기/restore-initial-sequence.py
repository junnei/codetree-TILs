n = int(input())
arr = list(map(int, input().split()))

from itertools import permutations

def solution():
    for nums in permutations(range(1,n+1)):
        temp = []
        for i in range(1, n):
            temp.append(nums[i]+nums[i-1])
        if temp == arr:
            return nums

print(*solution())