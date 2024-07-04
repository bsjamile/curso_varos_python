import locale

# Configura o locale para o Brasil
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def calcular_juros_compostos(pv, n, taxa, aporte_mensal):
    taxa = taxa / 100  # Converte a taxa de percentual para decimal
    fv = pv*(1+taxa)
    for _ in range(1,n):
        fv = (fv + aporte_mensal) * (1 + taxa)
    return round(fv, 2)

def formatar_moeda(valor):
    return locale.currency(valor, grouping=True)

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
        print(f'Parabéns, {nome}! Daqui a {n} meses você terá o valor total de {formatar_moeda(fv)}')

        salario_mensal = fv * taxa

        if salario_mensal >= salario_desejado:
            print(f'Parabéns! Você conseguiu alcançar {formatar_moeda(salario_mensal)}! O salário desejado era {formatar_moeda(salario_desejado)}!')
        else:
            print(f'Com o salário mensal de {formatar_moeda(salario_mensal)} você ainda não alcança o salário desejado de {formatar_moeda(salario_desejado)}. Invista mais um pouco!')

    except ValueError:
        print("Por favor, insira valores válidos.")

if __name__ == "__main__":
    main()