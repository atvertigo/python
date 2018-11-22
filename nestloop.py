number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# Aqui, todos os elementos de uma lista são LISTAS.

print(number_grid[0][1])

# Para acessar um elemento específico de uma lista,
# primeiro deve-se especificar a posição da lista (0~)
# e em seguida a posição do número desejado da lista.

for row in number_grid:
    for col in row:
        print(col)