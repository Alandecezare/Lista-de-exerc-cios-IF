# Recebe o número inteiro do usuário
numero = int(input("Digite um número inteiro maior que zero: "))

# Verifica se o número é válido
if numero <= 0:
    print("Número inválido")
else:
    # Calcula a soma dos algarismos convertendo o número para uma string e iterando sobre os caracteres
    soma = sum(int(digito) for digito in str(numero))
    print("A soma dos algarismos do número é:", soma)