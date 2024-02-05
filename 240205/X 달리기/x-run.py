x = int(input())
import sys
sys.setrecursionlimit(10000)
def move(d, v, t):
    if d == x and v == 1:
        return t
    if v <= 0:
        return sys.maxsize
    if d >= x:
        return sys.maxsize

    min_time = min(move(d+v, v-1, t+1), move(d+v, v, t+1), move(d+v, v+1, t+1))
    return min_time
print(move(1, 1, 1))