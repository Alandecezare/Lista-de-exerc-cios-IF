# Recebe as notas do usuário
lab = float(input("Digite a nota do trabalho de laboratório: "))
avaliacao = float(input("Digite a nota da avaliação semestral: "))
exame_final = float(input("Digite a nota do exame final: "))

# Calcula a média ponderada das notas
media = (2 * lab + 3 * avaliacao + 5 * exame_final) / 10

# Verifica a situação do aluno com base na média
if media < 3:
    situacao = "reprovado"
elif media < 5:
    situacao = "em recuperação"
else:
    situacao = "aprovado"

# Exibe a situação do aluno
print(f"O aluno está {situacao}.")