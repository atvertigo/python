def elevar_a_potencia(num1, potnum):
    result = 1
    for index in range(potnum):
        result = result * num1
    return result

print(elevar_a_potencia(2, 3))

# Função simples de calcular potência.
# Abre-se uma função def e o código é escrito para
# ser executado (loop) sempre que o index estiver dentro do
# alcance de potnum, que é o potenciador (potnum).