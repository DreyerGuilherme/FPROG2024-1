# Inicializar o vetor com 5 valores inseridos pelo usuário
v = []
for i in range(5):
    valor = int(input(f"Informe o valor para a posição {i}: "))
    v.append(valor)

# Multiplicar cada valor pela sua posição e imprimir o resultado
resultado = []
for i in range(len(v)):
    resultado.append(v[i] * i)

print("Os valores multiplicados pela sua posição no vetor são:", resultado)