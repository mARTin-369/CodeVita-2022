C, S = list(map(int, input().split()))
clg_seats = list(map(int, input().split()))

students = []

for i in range(S):
    std, per, clg1, clg2, clg3 = input().split(",")
    std_id = int(std.split("-")[1])
    per = float(per)
    clg1 = int(clg1.split("-")[1])
    clg2 = int(clg2.split("-")[1])
    clg3 = int(clg3.split("-")[1])

    students.append((per, std_id, clg1, clg2, clg3))

# print(students)
students.sort(key=lambda x: (-x[0], x[1]))
# print(students)

colleges = {i: [] for i in range(1, C + 1)}
admitted = [False for i in range(S)]

for i, std in enumerate(students):
    for c_id in std[2:]:
        if clg_seats[c_id - 1] > 0:
            colleges[c_id].append(std[0])
            clg_seats[c_id - 1] -= 1
            admitted[i] = True
            break

for i, std in enumerate(students):
    if not admitted[i]:
        c_id = clg_seats.index(max(clg_seats))
        colleges[c_id].append(std[0])
        clg_seats[c_id - 1] -= 1
        admitted[i] = True

# print(colleges)

for c_id, pers in colleges.items():
    if len(pers) > 0:
        print(f"C-{c_id} {min(pers)}")
    else:
        print(f"C-{c_id} n/a")
