class Data:
    def __init__(self, i, x, y):
        self.i = i
        self.x = int(x)
        self.y = int(y)

n = int(input())
datas = []
for i in range(1, n+1):
    x, y = input().split()
    datas.append(Data(i, x, y))

datas.sort(lambda x : (x.x*x.x + x.y*x.y, i))

for data in datas:
    print(data.i)