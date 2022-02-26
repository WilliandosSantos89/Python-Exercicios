print('>>>> Desafio 027 <<<<')
print('>>> Custo da Viagem <<<')

distância = int(input('Qual é a distância da sua viagem? '))
print("Você está prestes a fazer uma viagem de {}KM!".format(distância))

if distância <= 200:
    preço = distância * 0.50

else:
    preço = distância * 0.45

print('O custo da sua viagme é de R$ {:.2f}'.format(preço))

