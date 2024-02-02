n, m, d, s = map(int, input().split())
eats = [
    []
    for _ in range(n)
]

for _ in range(d):
    p, m, t = tuple(map(int, input().split()))
    eats[p-1].append([m, t])

ills = [
    tuple(map(int, input().split()))
    for _ in range(s)
]

for i in range(n):
    eats[i].sort(lambda x: x[-1])
ills.sort(lambda x: x[-1])


answer = set(range(1, m+1))

for ill_p, ill_t in ills:
    cheeze = set()
    for eat_m, eat_t in eats[ill_p-1]:
        if eat_t >= ill_t:
            break
        cheeze.add(eat_m)
    answer = answer & cheeze
print(len(answer))