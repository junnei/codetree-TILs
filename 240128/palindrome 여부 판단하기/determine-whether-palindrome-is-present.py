def reverse(string):
    result = ""
    for char in string[::-1]:
        result += char
    return result

string = input()

if string == reverse(string):
    print("Yes")
else:
    print("No")