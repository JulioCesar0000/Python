for c in range(10,0, -1):
    print(c)
print('FIM')

# O programa sempre pula o último número. EX:  Se colocarmos de 0 a 3 ele vai até o 2. 

# A letra C não precisa ser exatamente ela, vai do seu gosto, pode ser qualquer letra do alfabeto brasileiro. 

# Se for contar números retire os '' do print, caso os '' ficar o programa vai contar a letra e não os números, para realizar a contagem apenas coloque a letra que você pós depois de FOR. 

# Para relizar uma contagem de trás para frente será nescessário o uso de -1 após o 0(ZERO) com a vírgula.

n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('FIM')