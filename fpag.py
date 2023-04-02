def moeda(valor):
    return f'R$ {valor:.2f}'


def fgtscalc(salario):
    """
    --> Função para calculo de FGTS
    :param salario: valor do salário bruto
    :return: retorna o valor de dedução do fgts pela empresa
    """
    return salario * 0.08


def insscalc(salario):
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
    return inssAmount


def irrfcalc(salario):
    baseirrf = salario - insscalc(salario)
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
    return valorirrf


def vtcalc(salario, passagem):
    valorpassagem = (passagem * 2) * 22
    mensal = salario * 0.06
    aplicavel = 0
    if valorpassagem < mensal:
        aplicavel = valorpassagem
    else:
        aplicavel = mensal
    return aplicavel


def vacalc(valorva):
    return (valorva * 22) * 0.20


def salliq(salario, passagem, valorva):
    valor = salario - insscalc(salario) - irrfcalc(salario) - vtcalc(salario, passagem) - vacalc(valorva)
    return valor
