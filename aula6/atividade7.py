# Recebe dois números do usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Verifica se os números são iguais
if numero1 == numero2:
    print("Números iguais")
else:
    # Caso contrário, verifica qual número é maior
    maior = max(numero1, numero2)
    print(f"O maior número é: {maior}")