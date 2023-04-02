import fpag
import dadosfpag
from datetime import datetime
anoatual = datetime.now().year
cadastro = []
dados = {}
while True:
    # Nome do colaborador
    while True:
        nome = input('Nome Completo: ').strip().title()
        if nome.count(' ') >= 1 and nome.isnumeric() == False:
            dados['nome'] = nome
            break
        print('Inválido. Digite seu nome completo.')
    # Ano de nascimento e idade
    while True:
        nascimento = input('Ano de Nascimento: ')
        if len(nascimento) == 4 and int(nascimento) <= anoatual:
            dados['nascimento'] = nascimento
            dados['idade'] = dadosfpag.idade(int(nascimento))
            break
        print('Inválido. digite o ano completo, ex: 1990.')
    # Sexo
    while True:
        sexo = input('Sexo[M/F]: ').strip().upper()
        if sexo in 'MF':
            dados['sexo'] = sexo
            break
        print('Inválido. M para Masculino, F para Feminino.')
    # Salário
    while True:
        salario = input('Salário: ')
        if salario.isnumeric() == True:
            salario = int(salario)
            dados['salario'] = fpag.moeda(salario)
            break
        print('Inválido. Aceito apenas valores numéricos.')
    # Vale Transporte
    while True:
        passagem = input('Possui vt?[S/N]: ').strip().upper()[0]
        if passagem in 'SN':
            break
        print('Inválido')
    if passagem == 'S':
        valorvt = float(input('Digite o valor da passagem: '))
    else:
        valorvt = 0
    # Calculos
    dados['inss'] = fpag.insscalc(salario)
    dados['fgts'] = fpag.fgtscalc(salario)
    dados['irrf'] = fpag.irrfcalc(salario)
    dados['vt'] = fpag.vtcalc(salario, valorvt)
    dados['saliq'] = fpag.salliq(salario, valorvt)

    cadastro.append(dados.copy())
    dados.clear()
    # continuar novo cadastro
    while True:
        continuar = input('Cadastrar novo?[S/N]: ').strip().upper()[0]
        if continuar in 'SN':
            break
        print('Inválido. Aceito apenas S(sim)/ N(não).')
    if continuar == 'N':
        break
print(f'{"No.":<3}{"Nome":25}{"Sexo":8}{"Nasc.":<10}{"Idade":<10}{"Salário":12}{"INSS":10}{"FGTS":10}{"IRRF":10}{"VT":10}{"Líquido":12}')
for pos, valor in enumerate(cadastro):
    print(f'{pos:<3}{valor["nome"]:25}{valor["sexo"]:8}{valor["nascimento"]:<10}{valor["idade"]:<10}{valor["salario"]:12}{valor["inss"]:10}{valor["fgts"]:10}{valor["irrf"]:10}{valor["vt"]:10}{valor["saliq"]:12}')
