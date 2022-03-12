N = int(input())
S = int(input())
snakes = []

for i in range(S):
    snakes.append(tuple(map(int, input().split())))

priest = list(input())

dir = {"E": (0, -1), "S": (-1, 0), "W": (0, 1), "N": (1, 0)}

x, y = 0, 0
if priest[0] == "E":
    x, y = int(priest[1]), N - 1
elif priest[0] == "S":
    x, y = N - 1, int(priest[1])
elif priest[0] == "W":
    x, y = int(priest[1]), 0
elif priest[0] == "N":
    x, y = 0, int(priest[1])
