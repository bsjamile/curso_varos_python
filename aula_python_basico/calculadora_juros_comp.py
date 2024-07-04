#Projeto criando uma calculadora de juros compostos
'''
Fórmula de juros compostos: FV = PV * (1+i)**n
'''
nome = input('Qual o seu nome? ')

print(f'Olá, {nome}! Seja muito bem vindo aos juros compostos! Aqui nós cuidamos da sua aposentadoria :)')

pv = float(input('Digite a quantidade de dinheiro inicial do investimentos: '))
n = int(input('Por quantos meses você vai deixar o valor investido? '))
taxa = float(input('Qual a taxa de retorno do seu investimento? (% por mês) '))
salario_desejado = float(input('Digite o salário mensal que você quer receber ao se aposentar: '))
aporte_mensal = float(input('Aporte mensal: '))

taxa = taxa/100

tempo_final= 0

while tempo_final < n:

  if tempo_final == 0:
    fv = round(pv * (1+taxa),2)
    tempo_final += 1
  else:
    fv = round((fv+aporte_mensal) * (1+taxa),2)
    tempo_final += 1
  
fv = fv + aporte_mensal


print('---------------------------------')

print(f'Parabéns, {nome}! Daqui a {n} meses você terá o valor total de R${fv}')

salario_mensal = fv * taxa

if salario_mensal >= salario_desejado:
  print(f'Parabéns! Você conseguiu alcançar R${round(salario_mensal,2)}! O salário desejado era R${salario_desejado}!')
else:
  print(f'Com o salário mensal lde R${round(salario_mensal,2)} você ainda não alcança o salário desejado de R${salario_desejado}. Invista mais um pouco!!')