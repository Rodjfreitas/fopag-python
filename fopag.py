import fpag
import dadosfpag
import pandas as pd
from datetime import datetime
anoatual = datetime.now().year
cadastro = []
dados = {}
id = 0
cpfexiste = 'nao'
while True:
    dados['id'] = id
    dadosfpag.titulo('Cadastro de Funcionário')
    # CPF do colaborador
    while True:
        cpfexiste = 'nao'
        cpf = input('Digite o CPF: ').strip()
        if cpf.isnumeric() == True and len(cpf) == 11:
            cpf = int(cpf)
            if id > 0:
                for pos, valor in enumerate(cadastro):
                    if cpf == valor['cpf']:
                        cpfexiste = 'sim'
            if cpfexiste == 'sim':
                print('\033[1;41mCPF já existente.\033[m')
                continue
            dados['cpf'] = int(cpf)
            break
        print('\033[1;41mCPF Inválido.\033[m')
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
            salario = float(salario)
            dados['salario'] = salario
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
            if continuar == 'S':
                id += 1
            break
        print('Inválido. Aceito apenas S(sim)/ N(não).')
    if continuar == 'N':
        dadosfpag.linha()
        break
# Impressão de informações
dadosfpag.titulo('Folha de Pagamento')
print(f'{"ID":<3}{"Nome":25}{"CPF":<13}{"Sexo":6}{"Nasc.":<7}{"Idade":<8}{"Salário":12}{"INSS":10}{"FGTS":10}{"IRRF":10}{"VT":10}{"Líquido":12}')
for pos, valor in enumerate(cadastro):
    print(f'{valor["id"]:<3}{valor["nome"]:25}{valor["cpf"]:<13}{valor["sexo"]:6}{valor["nascimento"]:<7}{valor["idade"]:<8}{fpag.moeda(valor["salario"]):12}{fpag.moeda(valor["inss"]):10}{fpag.moeda(valor["fgts"]):10}{fpag.moeda(valor["irrf"]):10}{fpag.moeda(valor["vt"]):10}{fpag.moeda(valor["saliq"]):12}')
dadosfpag.linha()

# Gravando informações no excel
while True:
    salvar = input(
        '\nDeseja salvar informações em um arquivo?[S/N]').strip().upper()[0]
    if salvar in 'SN':
        if salvar == 'S':
            df = pd.DataFrame(cadastro, columns=['id', 'nome', 'cpf', 'sexo', 'nascimento',
                                                 'idade', 'salario', 'inss', 'fgts', 'irrf', 'vt', 'saliq'])
            df.to_excel('Relatório Fopag.xlsx',
                        sheet_name='Folha de pagamento', index=False)
            print('\033[1;42mArquivo Salvo\033[m')
        else:
            print('\033[1;41mArquivo não Salvo\033[m')
        break
    print('Valor Inválido. Digite S ou N para Sim/Não.')
