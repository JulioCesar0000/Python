nome = str(input('Qual é o seu nome? '))
# Nunca esquecer os : (dois pontos)
# Estrutura Aninhadas.
if nome == 'Júlio':
    print('Que nome bonito! ')
# Posso usar quantas vezes eu quiser o elif
elif nome == 'Pedro' or 'Nicole':
    print('Seu nome é bem estranho, mas é normal no Brasil.')
# Já o else vai de minha escolha
else:
    print('Seu nome é bem normal.')
# Vai até aqui.
# if, elif e else, são estruturas Condicional Aninhadas.
# É aninhada porque estão juntas em forma de ninho.
print('Tenha um bom dia, {}!'.format(nome))