#comandos if, elif e else
# if: determina uma condição a ser atendida, true ou false.
# elif: segue para a próxima condição, se a primeira não for atendida.
# else: para qualquer coisa que não atenda as condições anteriores.

idade = int(input(' Quantos anos você tem? '))
if idade == 18:
    print(' Você tem 18 anos, portanto é maior de idade.')
elif idade > 18:
    print(' Você tem mais de 18 anos, portanto é maior de idade.')
else:
    print(' Você tem menos de 18 anos, então é menor de idade. ')