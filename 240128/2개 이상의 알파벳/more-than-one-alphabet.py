def solution(string):
    if len(set(string)) >= 2:
        return True
    return False

string = input()

if solution(string):
    print("Yes")
else:
    print("No")