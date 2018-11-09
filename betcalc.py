num1 = float(input('Entre o primeiro número: '))
op = input('Entre com o operador: ')
num2 = float(input('Entre com o segundo número: '))

if op == '+':
    print(num1 + num2)
elif op == '-':
    print (num1 - num2)
elif op == '/':
    print (num1 / num2)
elif op == '*':
    print(num1 * num2)
else:
    print('Operador inválido.')