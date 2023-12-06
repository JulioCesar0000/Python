print('{:=^40}'.format(' LOJAS JÚLIO '))  
preço = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO 
[ 1 ] Á VISTA DINHEIRO/CHEQUE
[ 2 ] Á VISTA CARTÃO
[ 3 ] 2X NO CARTÃO
[ 4 ] 3X OU MAIS NO CARTÃO''')
opçao = int(input('Qual é a opção? '))
if opçao == 1:
    total = preço - (preço * 10 / 100)
elif opçao == 2:
    total = preço - (preço * 5 / 100)
elif opçao == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f} SEM JUROS'.format(parcela))
elif opçao == 4:
    total = preço + (preço * 20 / 100 )
    totparc = int(input('Quantas parcelas?? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS '.format(totparc, parcela))
else:
    total = 0 
    print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE!!')
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(preço, total))