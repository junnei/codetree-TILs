class Data:
    def __init__(self, name, x, y, z):
        self.name = name
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)

n = int(input())
datas = [Data(*input().split()) for _ in range(n)]
datas.sort(lambda x : (x.x+x.y+x.z))
for data in datas:
    print(data.name, data.x, data.y, data.z)