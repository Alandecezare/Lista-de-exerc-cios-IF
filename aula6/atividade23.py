# Recebe a idade do atleta do usuário
idade = int(input("Digite a idade do atleta: "))

# Classifica o atleta em uma das categorias
if 5 <= idade <= 7:
    categoria = "Infantil A"
elif 8 <= idade <= 10:
    categoria = "Infantil B"
elif 11 <= idade <= 13:
    categoria = "Juvenil A"
elif 14 <= idade <= 17:
    categoria = "Juvenil B"
else:
    categoria = "Sênior"

# Exibe a categoria do atleta
print(f"O atleta está na categoria {categoria}.")