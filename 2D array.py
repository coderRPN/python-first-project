
two_d_array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for row in two_d_array:
    print(row)


print("-----------------------------")
for row in two_d_array:
    for col in row:
        print(col)


print("-----------------------------")
x = range(len(two_d_array[0]))
for i in x:
    x = range(len(two_d_array[i]))
    for j in range(len(two_d_array)):
        print(two_d_array[i][j])

