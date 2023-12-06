from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))


print('O que você quer fazer com os números ')
sleep(1)
opçao = 0
while opçao != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar 
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair do Programa''') 
    sleep(0.5)
    opçao = int(input('>>>>>> Qual é a sua opção? '))

    if opçao == 1: 
        soma = n1 + n2
        print('A soma de {} + {} é igual a {}'.format(n1, n2, soma))
        sleep(1)
    elif opçao == 2:
        produto = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, produto))
        sleep(1)
    elif opçao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior entre {} e {} é {}'.format(n1, n2, maior))
        sleep(1)
    elif opçao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        sleep(1)
    elif opçao == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('Opção Inválida. Tente Novamente: ')
    print('=-=' *10)
print('Fim do programa. Volte sempre')