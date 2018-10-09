num1 = input('Digite o primeiro número:')
num2 = input('Digite o segundo número:')
result = num1 + num2
print(result)
print('Não é esse resultado que procuramos. ')

# Por padrão, o Python trata tudo como str (string), 
# então, ele só junta os dois números, em vez de somar.
# Adicionar int(integer, inteiro) ou float(flutuante) 
# antes dos números converte o dado, e resolve o problema.
# Usar float é mais seguro, pois cobre uma variedade maior de dados.

num1 = input('Digite o primeiro número:')
num2 = input('Digite o segundo número:')
result = float(num1) + float(num2)
print(result)