listas_de_nomes = ['Brenno','Leandro','Lucas']

print(listas_de_nomes[0])
print(listas_de_nomes[-1])
print(listas_de_nomes[0:2])

listas_de_nomes.append('Jamile')

print(listas_de_nomes)

listas_de_nomes.remove('Jamile')

print(listas_de_nomes)

bancos = ['Itau','Bradesco','Banco do Brasil']
precos_acoes = [20,15,10]

bancos.append('Santander') #adiciona ao final da lista
precos_acoes.append(30)

#Adicionar um novo dado em uma posição específica
bancos.insert(0,'Nubank')
precos_acoes.insert(0,9)
bancos.insert(1,'Inter')
precos_acoes.insert(1,13)
print(bancos)

#Remover um item da lista
bancos.append('Sulamérica')
print(bancos)
bancos.remove('Sulamérica')
print(bancos)

for i in range(0,6):
    print(f'{bancos[i]}:{precos_acoes[i]}')

#order uma lista
precos_acoes.sort() #ordena a lista do menos para o maior
print(precos_acoes) 

