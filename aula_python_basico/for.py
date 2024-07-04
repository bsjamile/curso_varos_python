bancos = ['Itau', 'Bradesco', 'Banco do Brasil']

for banco in bancos:
  print(banco)
  
cotacoes = [10,20,30]

for preco in cotacoes:
  print(preco)
  
for i in range(0, len(bancos)):
  print(f'{bancos[i]}:{cotacoes[i]}')  
  
for i in range(0, len(bancos)): 
  print(bancos[i],cotacoes[i])
  
for i in range(0, len(bancos)): 
  print(f'O preço da ação {bancos[i]} é {cotacoes[i]}')
  
#for = sabe quais são seus dados
#while = vc não sabe quantos dados existem e faz a condicao enquanto uma condicao for verdadeira