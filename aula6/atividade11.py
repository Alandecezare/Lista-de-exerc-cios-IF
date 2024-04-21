import math

# Recebe o número inteiro do usuário
numero = int(input("Digite um número inteiro: "))

# Verifica se o número é negativo
if numero < 0:
    print("Número inválido")
else:
    # Calcula o logaritmo do número
    logaritmo = math.log(numero)
    print("O logaritmo do número é:", logaritmo)