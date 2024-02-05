x = int(input())

d = 1
v = 1
t = 1

while d < x:
    t += 1
    
    if d + v + v*(v+1)//2 <= x: 
        v += 1
    elif d + v + v*(v-1)//2 > x:
        v -= 1
    d += v

print(t)