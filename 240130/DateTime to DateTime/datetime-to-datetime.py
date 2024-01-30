a, b, c = map(int, input().split())
time = (a-11)*60*24+(b-11)*60+(c-11)
if time<0:
    print(-1)
else:
    print(time)