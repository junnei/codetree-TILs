x = 1
class Data:
    def __init__(self, y, z):
        global x
        self.x = x
        self.y = int(y)
        self.z = int(z)
        x+=1

n = int(input())
datas = [Data(*input().split()) for _ in range(n)]
datas.sort(lambda x : (-x.y, -x.z, x.x))
for data in datas:
    print(data.y, data.z, data.x)