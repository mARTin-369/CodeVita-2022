import math

N = int(input())
vccord = []
vc = {i: [] for i in range(N)}

for i in range(N):
    lat, lon = list(map(int, input().split()))
    vccord.append((lat, lon))

P = int(input())

for i in range(P):
    name, age, cat, lat, lon = input().split()
    age, lat, lon = int(age), int(lat), int(lon)

    dist = [math.sqrt((x - lat) ** 2 + (y - lon) ** 2) for x, y in vccord]
    vc[dist.index(min(dist))].append((age, cat, name))

# print(vc)

for v, p in vc.items():
    l = sorted(p, key=lambda x: (-x[0], x[1], x[2]))
    l = list(map(lambda x: x[2], l))

    if len(l) > 0:
        print(" ".join(l))
    else:
        print("Empty Centre")
