num = int(input('Digite um número de sua escolha: '))
print('''Escolha uma das bases para a CONVERSÃO 
[ 1 ] converter para BINÁRIO 
[ 2 ] converter para OCTAL 
[ 3 ] converter para HEXADECIMAL ''') 
opção = int(input('Escolha uma das TRÊS opções: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, (num)[2:]))
else:
    print('Número inválido. Tente novamente. ')