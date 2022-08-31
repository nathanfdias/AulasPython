n = input('Digite um valor: ')
f = n.isnumeric()

if f:
    print('Tipo numérico: {}'.format(n))
else:
    print('Tipo Não numérico')
