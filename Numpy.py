import numpy as np

print('matriz vazia 3/3')
empty_array = np.empty((3, 3))
print(empty_array)

print('matriz 2/2 com números 1')
ones_array = np.ones((2, 2))
print(ones_array)

print('matriz 4/4 com números 0')
zeros_array = np.zeros((4, 4))
print(zeros_array)

print('matriz 3/3 com números aleatórios (0-1)')
random_array = np.random.rand(3, 3)
print(random_array)

print('Seleciona o elemento na segunda linha e terceira coluna (6)')
my_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(my_array)
print(my_array[1, 2])

print('Valores máximos e mínimos da matriz')
max_value = np.max(my_array)
min_value = np.min(my_array)
print(f"Valor máximo: {max_value}, Valor mínimo: {min_value}")

print('Soma de valores de matrizes')
total_sum = np.sum(my_array)
print(f"Soma total: {total_sum}")

print('remover entradas unidimensionais')
squeezed_array = np.squeeze(my_array)
print(squeezed_array)

print('Adição de matrizes')
matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
resultado = matriz1 + matriz2
print("Resultado da adição de matrizes:")
print(resultado)

print('Subtração de matrizes')
matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
resultado = matriz1 - matriz2
print("Resultado da subtração de matrizes:")
print(resultado)

print('Multiplicação de matrizes')
matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
resultado = np.dot(matriz1, matriz2)
# Ou, alternativamente: resultado = matriz1 @ matriz2
print("Resultado da multiplicação de matrizes:")
print(resultado)

print('Soma das diagonais de uma matriz')
diagonal_sum = np.trace(my_array)
print(f"Soma diagonal: {diagonal_sum}")

print('N° de linhas e colunas da matriz')
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
num_linhas, num_colunas = np.shape(matriz)
print(f"Número de linhas: {num_linhas}")
print(f"Número de colunas: {num_colunas}")

