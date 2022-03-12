N = int(input())
R = int(input())
strings = input().split(",")

# print(strings)
# print(N, R)

subsets = [0]

for i in range(N):
    subsets.append(2**i)

for i in range(1, 2**N):
    if not (i & (i - 1) == 0):
        subsets.append(i)

print(subsets)

num = subsets[R - 1]
i = 0
result = []
while num > 0:
    if (num & 1) == 1:
        result.append(strings[i])
    i += 1
    num = num >> 1

print(result)
print(",".join(result))

# n = 2
# [ 0, 1, 2,    3]
#   1  2  3     4

# n = 3
# [ 0, 1, 2, 4,     3,      5, 6, 7]
# r  1  2  3  4      5       6  7  8

# n = 4
# [ 0, 1, 2, 4, 8,      3,      5, 6, 7,     9, 10, 11, 12, 13, 14, 15]
# r  1  2  3  4  5       6       7  8  9      10 11  12  13  14  15  16

if r <= n + 1:
    num = 2 ** (r - 2)
