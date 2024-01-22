import sys

input = sys.stdin.readline

string = input().rstrip()

len_str_is_even = len(string) % 2 +1

for char in string[-len_str_is_even::-2]:
    print(char, end="")