def get_matrix(n, m, value):
    matrix1 = []
    for i in range(n):
        matrix2 = []
        matrix1.append(matrix2)
        for j in range(m):
            matrix2.append(value)
    return matrix1
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)