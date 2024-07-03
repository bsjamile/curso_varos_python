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

taxa = taxa/100

fv = round(pv * (1+taxa)**n,2)
print('---------------------------------')

print(f'Parabéns, {nome}! Daqui a {n} meses você terá o valor total de R${fv}')

