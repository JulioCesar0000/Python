casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de empréstimo? '))
prestaçao = casa / (anos * 12)
mínimo = salario * 30 / 100
print('Para pagar uma casa de R$ {:.2f} em {} anos'.format(casa, anos))
print('a prestação será de R$ {:.2f}'.format(prestaçao))
if prestaçao <= mínimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Seu empréstimo foi NEGADO, boa sorte na próxima. ')