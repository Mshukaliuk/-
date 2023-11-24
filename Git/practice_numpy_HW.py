import numpy as np
import random
'''
print('\n TASK 4____________________________________________________________________________________________________\n')

# Task 4.  Generate chess dashboard

zero_2d = np.zeros((8, 8))  # arg - tuple, where first arg - row, second - column
zero_2d[:2, :] = 1
zero_2d[-2:, :] = 1

print(zero_2d)
'''

print('\n TASK 6____________________________________________________________________________________________________\n')

# # Task 6. Find sum of diagonal for matrix (5, 5).
# Step 1: generate matrix.
# Step 2: display diagonal,
# Step 3: Find sum of main dianogal,
# Step 3: Find alternative diagonal, find elements what more than sum of main diagonal

print('\n TASK 6 Option 1___________________________________________________________________________________________\n')

# OPTION 1 - рандомні номера, які ми збираємо в np, потім це reshape.
# тут ще мені колега підказав щоб зробити діагональ типу як справжня діагональ, розказав логіку і падказав використати enumerate
rows = 5
cols = 5
matrix = [[random.randint(1, 10) for j in range(cols)] for i in range(rows)]

numpy_matrix = np.array(matrix)
reshaped_matrix = numpy_matrix.reshape(5, -1)

print(reshaped_matrix)

diagonal_sum = 0
for index, row in enumerate(reshaped_matrix):
    d_number = row[index]
    diagonal_sum += d_number

print("Sum of Diagonal Elements:", diagonal_sum)

print('\n TASK 6 Option 2___________________________________________________________________________________________\n')

# OPTION 2 - всі числа по порядку йдуть, не рандомно
arr = np.arange(1, 26).reshape(5, -1)
print(arr)
for row in arr:
    print("dianogal: ",row)
    sum_result = np.sum(row)
    print(f'Sum of dianogal: {sum_result}')

print('\n TASK 6 Option 3___________________________________________________________________________________________\n')
# OPTION 3  примітивна. Обираємо колонку і її сумуємо

rows = 5
cols = 5
selected_column = 0

matrix2 = [[random.randint(1, 10) for j in range(cols)] for i in range(rows)]
numpy_matrix2 = np.array(matrix2)
reshaped_matrix = numpy_matrix2.reshape(5,5)

print("reshaped_matrix: \n", reshaped_matrix)
c = 0
for a in range(min(rows, cols)):
    # print("reshaped_matrix: ",reshaped_matrix[a,selected_column])
    b = (reshaped_matrix[a,selected_column])
    c = b + c
    # print("reshaped_matrix: ", reshaped_matrix[a, selected_column])

print(f"\nSum of all elements in column {selected_column} as diagonal = ", c)
