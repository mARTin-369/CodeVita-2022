t1 = int(input())
t2 = int(input())
N = int(input())
villages = list(map(int, input().split()))

# print(villages)


def solve(i, res):
    if i >= len(villages):
        return res
    return min(
        solve(i + 1, res + villages[i] * t1), solve(i + 1, res + villages[i] * t2)
    )


print(solve(0, 0))
