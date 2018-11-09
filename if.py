se_homem = False
se_alto = False

if se_homem or se_alto: 
    print('gênero masculino, ou alto, ou ambos.')
else:
    print('gênero indefinido nem alto.')

if se_homem and se_alto: 
    print('gênero masculino e alto.')
elif se_homem and not(se_alto):
    print('gênero masculino e baixo.')
else:
    print('gênero indefinido nem alto.')