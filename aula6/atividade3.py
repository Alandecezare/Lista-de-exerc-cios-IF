import math

# Solicita ao usuário que insira um número real
numero = float(input("Digite um número real: "))

# Verifica se o número é positivo ou negativo
if numero >= 0:
    # Se for positivo, calcula a raiz quadrada do número
    raiz_quadrada = math.sqrt(numero)
    print(f"A raiz quadrada de {numero} é: {raiz_quadrada}")
else:
    # Se for negativo, imprime o número ao quadrado
    quadrado = numero ** 2
    print(f"O quadrado de {numero} é: {quadrado}")