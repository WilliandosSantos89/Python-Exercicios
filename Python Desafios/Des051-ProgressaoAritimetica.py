print("="*20)

print('10 Termos de uma PA')

print('='*20)



primeiro_termo = int(input("Primeiro Termo: "))
razão = int(input("Razão: "))

termo = primeiro_termo + (10 - 1) * razão
for c in range (primeiro_termo,termo + razão, razão):
    print('{}'.format(c), end=' -> ')

print("Acabou")