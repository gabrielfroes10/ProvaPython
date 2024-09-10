def fibonacci_sequence(N):
    
    if N < 0:
        raise ValueError("O número N deve ser maior ou igual a 0.")
    
    fib_sequence = []
    
    a, b = 0, 1
    
    while a <= N:
        fib_sequence.append(a)
        a, b = b, a + b
    
    return fib_sequence

try:
    N = int(input("Digite um número inteiro N para gerar a sequência de Fibonacci até esse número: "))
    resultado = fibonacci_sequence(N)
    print(f"A sequência de Fibonacci até o número {N} é: {resultado}")
except ValueError as e:
    print(f"Entrada inválida: {e}")
