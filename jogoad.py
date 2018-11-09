palavra_secreta = 'girafa'
ad = ''
tentativas = 0
limite = 3
fim = False

while ad != palavra_secreta and not(fim):
    if tentativas < limite:
        ad = input('Tente adivinhar: ')
        tentativas += 1
    else: 
        fim = True

if fim:
    print('As tentativas acabaram, você perdeu!')
else:
    print('Você acertou.')

# Primeiro, cria-se um número de variáveis que vão
# setar os parâmetros do jogo. Depois, cada vez que uma tentativa
# falha, o contador de tentativas aumenta, até 3. Em 3, o jogador
# perde. Enquanto tais condições forem atendidas, o código vai 
# continuar em um loop até um limite especificado.