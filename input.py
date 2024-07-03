nome = input('Qual é o seu nome? ') #por padrao é uma string
idade = int(input('Qual é a sua idade? ')) #idade é uma string q precisa ser convertidada para inteira para que seja possível realizar uma operação

ano_nascimneto = 2024 - idade 

print(f'''Olá {nome}, seja bem vindo/a! Soube que você tem {idade} anos!
Dito isso, você nasceu no ano de {ano_nascimneto}''')

