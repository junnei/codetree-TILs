n = int(input())
datas = [(i, int(x)) for i, x in enumerate(input().split())]

datas.sort(lambda x : (x[1]))

datas = [(i, x[0], x[1]) for i, x in enumerate(datas)]
datas.sort(lambda x : x[1])

for data in datas:
    print(data[0]+1, end=" ")