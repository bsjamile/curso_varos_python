
def solicita_dim_reais():
    try:
        dinheiro = float(input('Quanto dinheiro você tem para investir? '))
        retorno = investir_ou_nao(dinheiro)
        return retorno
    except:
        return 'Digite um valor válido!'

def investir_ou_nao(dim_reais):
    if dim_reais < 20:
        return 'Invista em você mesmo!'
    elif dim_reais >= 20 and dim_reais <1000:
        return 'Comece a montar uma carteira de investimentos!'
    else:
        return 'Invista pesado e se aposente cedo!'

print(solicita_dim_reais())
