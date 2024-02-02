n, m, d, s = map(int, input().split())
eats = [
    tuple(map(int, input().split()))
    for _ in range(d)
]
ills = [
    tuple(map(int, input().split()))
    for _ in range(s)
]

eats.sort(lambda x: x[-1])
ills.sort(lambda x: x[-1])

cheeze = set()
for ill_p, ill_t in ills:
    for eat_p, eat_m, eat_t in eats:
        if eat_t > ill_t:
            break
        if ill_p == eat_p:
            cheeze.add(eat_m)

print(len(cheeze))