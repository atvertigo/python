import math
from math import ceil
from math import sqrt

# desenhando formas no python com print.
print ('    /|')
print ('   / |')
print ('  /  |')
print (' /___|')
print ('_______________________________________________________________')


# variáveis e tipos diferentes de dados
cname = 'Pedro'
cage = '77' 
ismale = True
# nota: as variáveis devem ser colocadas sempre antes dos comandos.
print (' Existia um homem, chamado ' + cname + ',')
print (' que tinha ' + cage +' anos de idade. ')
print (' Ele gostava de se chamar ' + cname + ',')
print (' só não gostava de ter ' + cage + ' anos.')
# três tipos principais de dados: string (palavras), int (números) e true/false.
print ('_______________________________________________________________')


# Passo 6: Trabalhando com strings, ou texto simples.

print('Giraffe\'Academy') 
# comando usado pra "printar" uma aspa.
phrase = 'Giraffe academy'
print(phrase.lower())
# comando usado para deixar a frase minúscula. o oposto é .upper:
print ('.upper() para deixar em maiúsculo. ')
print(phrase.upper())
# também se pode utilizar tais comandos em conjunto com comandos do tipo "is":
print ('.isupper() para saber se True ou False.')
print(phrase.upper().isupper())
# isupper() retorna se a informação requerida é true ou false, no caso, se a frase é upper.
print ('len() para saber a extensão da frase em números.')
print(len(phrase))
# len() retorna o length de toda a frase entre aspas, ou seja, 
# a extensão da frase contando todos seus caracteres.
print('[] para retornar o caractere respectivo por um número.')
print(phrase[8])
# comando para retornar o caractere especificado pelo número digitado.
# exemplo: phrase = giraffe academy
# espaços contam.   123456789112345
print('.index para saber onde um caractere ou frase inteira começa.')
print(phrase.index('academy'))
# index serve para mostrar onde um caractere ou frase inteira começa. isso pode ser ajustado.
print('.replace para substituir o primeiro valor entrado pelo segundo.')
print(phrase.replace('academy', 'zoo'))
#.replace substitui o valor atual pelo segundo valor.
print('_____________________________________________________________')


# Passo 7: Trabalhando com números.
print('print(2.05+(7*8)):')
print(2.05+(7*8))
# parênteses sempre serão processados primeiro.
print('% para saber o resto de uma divisão: \'10 % 3\'. 10 por 3 é 3 e sobra 1.')
print(10 % 3)
# % = remainder, ou o resto.
print('round para arredondar o número entrado. exemplo, 3.2: print(round(3.2)) ')
print(round(3.2))
# usado para arredondar para o valor "fechado" mais próximo.

# para utilizar estas funções de matemática do python, "from math import *" deve ser usado.
print('ceil: arredonda para o número mais próximo, positivo ou negativo. ceil(4.9):')
mnum = 4.9
print(ceil(mnum))
# ceil arredonda o número para o número mais próximo positivamente, 
# se for positivo, e negativamente caso contrário.
print('sqrt: square root, ou raiz quadrada. sqrt(36):')
print(sqrt(36))
# sqrt. SQuare RooT

# Passo 8: Recebendo os dados do usuário
nome= input('Digite seu nome. ')
idade= input('E a sua idade? ')
print('Oi, ' + nome + '! Você tem ' + idade + ' anos')

# Passo 9: Construindo uma calculadora
# Ver calc.py

# Passo 10: Jogo madlibs
# Ver madlibs.py

# Passo 11: Listas
# Ver listas.py

# Passo 12: Funções de listas
# Ver listfunc.py