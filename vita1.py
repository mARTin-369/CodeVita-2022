N = int(input())
adjList = {i + 1: [] for i in range(N)}


def solve(start, end):
    visited = set()
    que = [(start, 0)]

    while len(que) > 0:
        n = que.pop(0)
        if n[0] == end:
            return n[1]

        visited.add(n[0])
        for i in adjList[n[0]]:
            if i not in visited:
                que.append((i, n[1] + 1))
    return -1


for i in range(N):
    pages = list(map(int, input().split()))
    adjList[i + 1].extend(pages)

start, end = list(map(int, input().split()))

# print(adjList)
# print(s, e)

print(solve(start, end))
