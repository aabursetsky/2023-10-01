def get_matrix(n, m, value):
    matrix = []
    matrix_string = []
    for i in range(n):
        matrix.append(matrix_string)
        
    for j in range(m):
        matrix_string.append(value)
            
    return(matrix)

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
result4 = get_matrix(0, -1, 13)
print(result1)
print(result2)
print(result3)
print(result4)

#[[10, 10], [10, 10]]
#[[42, 42, 42, 42, 42], [42, 42, 42, 42, 42], [42, 42, 42, 42, 42]]
#[[13, 13], [13, 13], [13, 13], [13, 13]]
#[]
