# Recebe as notas das provas do usuário
nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))

# Calcula a média ponderada das notas
media = (nota1 + 2 * nota2) / 3

# Verifica se a média é maior ou igual a 70 para determinar se o aluno foi aprovado
if media >= 70:
    situacao = "aprovado"
else:
    situacao = "reprovado"

# Exibe a média do aluno e sua situação
print(f"A média do aluno é: {media}")
print(f"O aluno está {situacao}.")