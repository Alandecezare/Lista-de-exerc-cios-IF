import math

# Solicita ao usuário que insira um número
numero = float(input("Digite um número: "))

# Verifica se o número é positivo ou negativo
if numero >= 0:
    # Calcula a raiz quadrada do número
    raiz_quadrada = math.sqrt(numero)
    print(f"A raiz quadrada de {numero} é: {raiz_quadrada}")
else:
    # Se o número for negativo, exibe uma mensagem de erro
    print("Número inválido. Por favor, insira um número positivo.")