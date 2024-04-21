def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero."

def menu():
    print("Escolha a operação desejada:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

# Exibir o menu para o usuário
menu()

# Ler a opção escolhida pelo usuário
opcao = int(input("Digite o número da operação desejada: "))

# Verificar a opção escolhida e realizar a operação correspondente
if opcao in [1, 2, 3, 4]:
    # Ler os valores numéricos fornecidos pelo usuário
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))

    # Realizar a operação escolhida
    if opcao == 1:
        resultado = soma(valor1, valor2)
        print(f"Resultado da soma: {resultado}")
    elif opcao == 2:
        resultado = subtracao(valor1, valor2)
        print(f"Resultado da subtração: ")