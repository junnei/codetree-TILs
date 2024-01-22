import sys

input = sys.stdin.readline

string = input().rstrip()

def find_all(a_str, sub):
    result = []
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return result
        result.append(start)
        start += 1

print(len(find_all(string, 'ee')), len(find_all(string, 'eb')))