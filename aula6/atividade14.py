# Dicionário que mapeia os números aos dias da semana
dias_da_semana = {
    1: "domingo",
    2: "segunda-feira",
    3: "terça-feira",
    4: "quarta-feira",
    5: "quinta-feira",
    6: "sexta-feira",
    7: "sábado"
}

# Recebe um número inteiro entre 1 e 7 do usuário
numero = int(input("Digite um número inteiro entre 1 e 7: "))

# Verifica se o número está dentro do intervalo esperado
if 1 <= numero <= 7:
    # Obtém o dia da semana correspondente ao número
    dia_da_semana = dias_da_semana[numero]
    print("O dia da semana correspondente é:", dia_da_semana)
else:
    print("Número inválido. Por favor, digite um número entre 1 e 7.")