import math

# Solicita ao usuário que insira um número
numero = float(input("Digite um número: "))

# Verifica se o número é positivo
if numero > 0:
    # Calcula o quadrado do número
    quadrado = numero ** 2
    print(f"O quadrado de {numero} é: {quadrado}")

    # Calcula a raiz quadrada do número
    raiz_quadrada = math.sqrt(numero)
    print(f"A raiz quadrada de {numero} é: {raiz_quadrada}")
else:
    print("Número inválido. Por favor, insira um número positivo.")