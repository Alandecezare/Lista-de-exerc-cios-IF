# Recebe um número inteiro entre 1 e 12 do usuário
numero = int(input("Digite um número inteiro entre 1 e 12: "))

# Verifica o número e imprime o mês correspondente
if numero == 1:
    print("Janeiro")
elif numero == 2:
    print("Fevereiro")
elif numero == 3:
    print("Março")
elif numero == 4:
    print("Abril")
elif numero == 5:
    print("Maio")
elif numero == 6:
    print("Junho")
elif numero == 7:
    print("Julho")
elif numero == 8:
    print("Agosto")
elif numero == 9:
    print("Setembro")
elif numero == 10:
    print("Outubro")
elif numero == 11:
    print("Novembro")
elif numero == 12:
    print("Dezembro")
else:
    print("Número inválido. Por favor, digite um número entre 1 e 12.")