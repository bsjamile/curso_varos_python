def calcular_juros_compostos(pv, n, taxa, aporte_mensal):
    taxa = taxa / 100
    fv = pv
    for _ in range(n):
        fv = round((fv + aporte_mensal) * (1 + taxa), 2)
    return fv

def main():
    nome = input('Qual o seu nome? ')
    print(f'Olá, {nome}! Seja muito bem-vindo aos juros compostos! Aqui nós cuidamos da sua aposentadoria :)')

    try:
        pv = float(input('Digite a quantidade de dinheiro inicial do investimento: '))
        n = int(input('Por quantos meses você vai deixar o valor investido? '))
        taxa = float(input('Qual a taxa de retorno do seu investimento? (% por mês) '))
        salario_desejado = float(input('Digite o salário mensal que você quer receber ao se aposentar: '))
        aporte_mensal = float(input('Aporte mensal: '))

        if pv < 0 or n < 0 or taxa < 0 or salario_desejado < 0 or aporte_mensal < 0:
            print("Por favor, insira valores positivos.")
            return

        fv = calcular_juros_compostos(pv, n, taxa, aporte_mensal)

        print('---------------------------------')
        print(f'Parabéns, {nome}! Daqui a {n} meses você terá o valor total de R${fv:,.2f}')

        salario_mensal = fv * (taxa / 100)

        if salario_mensal >= salario_desejado:
            print(f'Parabéns! Você conseguiu alcançar R${salario_mensal:,.2f}! O salário desejado era R${salario_desejado:,.2f}!')
        else:
            print(f'Com o salário mensal de R${salario_mensal:..2f} você ainda não alcança o salário desejado de R${salario_desejado:,.2f}. Invista mais um pouco!')

    except ValueError:
        print("Por favor, insira valores válidos.")

if __name__ == "__main__":
    main()