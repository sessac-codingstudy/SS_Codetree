a_matrix = []
for i in range(3):
    a_matrix.append(list(map(int, input().split())))

new_metrix = []
for i in range(3):
    new_array = []
    for j in range(3):
        new_array.append(a_matrix[i][j] * 3)
    new_metrix.append(new_array)

for array in new_metrix:
    for value in array:
        print(value, end =' ')
    print()