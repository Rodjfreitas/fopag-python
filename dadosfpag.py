def idade(nascimento):
    import datetime
    anoatual = datetime.datetime.now().year
    return anoatual - nascimento


def titulo(msg):
    print('=' * 50)
    print(f'{msg:^50}')
    print('=' * 50)


def linha():
    print('=' * 50)
    print('\n')


def questionyesno(msg):
    while True:
        question = input(f'{msg} [S/N]: ').strip().upper()[0]
        if question in 'SN':
            return question
        print('Inválido. digite S para sim, N para não.')


def cpformat(cpf):
    valor = []
    for letra in cpf:
        valor.append(letra)
    if len(cpf) == 10:
        valor.insert(2, '.')
        valor.insert(6, '.')
        valor.insert(10, '-')
    else:
        valor.insert(3, '.')
        valor.insert(7, '.')
        valor.insert(11, '-')
    return "".join(valor)
