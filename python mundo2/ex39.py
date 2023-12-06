from datetime import date 
atual = date.today().year
nasc = int(input('Ano de NASCIMENTO: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))

if idade == 18:
    print('Você deve se alistar IMEDIATAMENTE!!')

elif idade < 18:
    saldo =  18 - idade

    print('Você ainda não tem 18 anos. Faltam {} anos para o ALISTAMENTO MILITAR!'.format(saldo))

    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))

elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se ALISTADO há {} ANOS!!'.format(saldo))

    ano = saldo - atual
    print('Seu alistamento foi em {}'.format(ano))
