# Recebe um número inteiro do usuário
numero = int(input("Digite um número inteiro: "))

# Verifica se o número é divisível por 3 ou por 5, mas não simultaneamente pelos dois
if numero % 3 == 0 and numero % 5 != 0:
    print("O número é divisível por 3, mas não por 5.")
elif numero % 5 == 0 and numero % 3 != 0:
    print("O número é divisível por 5, mas não por 3.")
else:
    print("O número não é divisível por 3 ou por 5, ou é divisível por ambos.")