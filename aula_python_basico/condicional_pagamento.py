def solicita_metodo_de_pagamento():
    metodo_de_pagamento = input('Qual seu método de pagamento? ')
    retorno = pagamento(metodo_de_pagamento)
    return retorno

def pagamento(metodo_de_pagamento):
    if metodo_de_pagamento == 'pix' or metodo_de_pagamento == 'cartão':
        return 'Podemos receber seu pagamento!'
    elif metodo_de_pagamento == 'dinheiro':
        return 'Infelimente não podemos aceitar pois não vivemos mais como os Incas!'
    else:
        return 'Não conheço esse tipo de dinheiro!'

print(solicita_metodo_de_pagamento())