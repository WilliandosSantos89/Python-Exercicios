
n = 1

sexo = str(input('Digite seu sexo [M / F]: ')).upper()[0].strip()
while sexo not in 'MF':
    sexo = str(input('Dados inválidos! Informe seu sexo novamente: ')).upper()[0].strip()

print('Sexo {} registrado.'.format(sexo))