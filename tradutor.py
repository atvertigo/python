def traduzir(frase):
    traducao = ''
    for letra in frase:
        if letra in 'AEIOUaeiou':
            traducao = traducao + "g"
        else:
            traducao = traducao + letra
    return traducao

print(traduzir(input('Digite uma frase: ')))