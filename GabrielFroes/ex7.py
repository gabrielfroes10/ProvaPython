def soma_dos_quadrados(vetor):
    
    soma = sum(x**2 for x in vetor)
    return soma

vetor = []

print("Digite 10 números inteiros:")
for i in range(10):
    while True:
        try:
            numero = int(input(f"Digite o número {i+1}: "))
            vetor.append(numero)
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

resultado = soma_dos_quadrados(vetor)

print(f"A soma dos quadrados dos elementos do vetor é: {resultado}")
