class Data:
    def __init__(self, x, y, z):
        self.x = x
        self.y = int(y)
        self.z = int(z)

n = int(input())
datas = []
for i in range(n):
    x, y, z = input().split()
    datas.append(Data(x, y, z))

datas.sort(lambda x : (x.y, -x.z))

for data in datas:
    print(data.x, data.y, data.z)