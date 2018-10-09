numeros = [42, 4, 8, 15, 16, 23]
nomes = ['Kevin','Karen','Jim','Oscar','Toby']
print (nomes)
nomes.extend(numeros)
# .extend pode ser útil para mesclar duas listas.
print (nomes)
nomes.append('Creed')
#. append pode ser útil para adicionar itens a uma lista.
print (nomes)
nomes.insert(1, 'Kelly')
# .insert usa dois parâmetros e serve para inserir um valor em um determinado
# número de indexação.
print (nomes)
nomes.remove('Kelly')
# .remove, naturalmente, remove a entrada.
print (nomes)
# .clear limpa a lista especificada.
nomes.pop()
print (nomes)
# .pop remove o último item da lista.
print(nomes.index('Kevin'))
# variável.index vai mostrar qual o número de index da entrada.
numeros.sort()
print(numeros)
# .sort vai organizar a lista em ordem.
numeros.reverse()
print(numeros)
# .reverse vai reverter a ordem.