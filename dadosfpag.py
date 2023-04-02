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