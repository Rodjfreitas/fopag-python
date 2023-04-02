def moeda(valor):
    return f'R${valor:.2f}'


def fgtscalc(salario, formatar=True):
    """
    --> Função para calculo de FGTS
    :param salario: valor do salário bruto
    :return: retorna o valor de dedução do fgts pela empresa
    """
    if formatar:
        return moeda(salario * 0.08)
    return salario * 0.08


def insscalc(salario, formatar=True):
    """
    --> Função para calculo de INSS
    :param salario: valor do salário bruto
    :return: retorna o valor de dedução do inss na folha de pagamento
    """
    inssAmount = 0
    if salario <= 1302:
        inssAmount += salario * 0.075
    elif salario <= 2571.29:
        inssAmount += 1302 * 0.075
        inssAmount += (salario - 1302.01) * 0.09
    elif salario <= 3856.94:
        inssAmount += 1302 * 0.075
        inssAmount += (2571.29 - 1302.01) * 0.09
        inssAmount += (salario - 2571.30) * 0.12
    elif salario <= 7507.49:
        inssAmount += 1302 * 0.075
        inssAmount += (2571.29 - 1302.01) * 0.09
        inssAmount += (3856.94 - 2571.30) * 0.12
        inssAmount += (7507.49 - 3856.95) * 0.14
    else:
        inssAmount += 0
    if formatar:
        return moeda(inssAmount)
    return inssAmount


def irrfcalc(salario, formatar=True):
    baseirrf = salario - insscalc(salario, formatar=False)
    valorirrf = 0
    if baseirrf <= 1903.98:
        valorirrf += 0
    elif baseirrf <= 2826.65:
        valorirrf += baseirrf * 0.075 - 142.80
    elif baseirrf <= 3751.05:
        valorirrf += baseirrf * 0.15 - 354.80
    elif baseirrf <= 4664.68:
        valorirrf += baseirrf * 0.225 - 636.13
    else:
        valorirrf += baseirrf * 0.275 - 869.36
    if formatar:
        return moeda(valorirrf)
    return valorirrf


def vtcalc(salario, passagem, formatar=True):
    valorpassagem = (passagem * 2) * 22
    mensal = salario * 0.06
    aplicavel = 0
    if valorpassagem < mensal:
        aplicavel = valorpassagem
    else:
        aplicavel = mensal
    if formatar:
        return moeda(aplicavel)
    return aplicavel


def salliq(salario, passagem, formatar=True):
    valor = salario - insscalc(salario, formatar=False) - irrfcalc(salario, formatar=False) - vtcalc(salario, passagem, formatar=False)
    if formatar:
        return moeda(valor)
    return valor
