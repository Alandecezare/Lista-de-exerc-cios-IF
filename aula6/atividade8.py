# Função para verificar se uma nota é válida
def nota_valida(nota):
    return 0.0 <= nota <= 10.0

# Função para calcular a média das notas
def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2

# Recebe as notas do usuário e verifica se são válidas
nota1 = float(input("Digite a primeira nota: "))
if not nota_valida(nota1):
    print("Nota inválida. Deve estar entre 0.0 e 10.0.")
    exit()

nota2 = float(input("Digite a segunda nota: "))
if not nota_valida(nota2):
    print("Nota inválida. Deve estar entre 0.0 e 10.0.")
    exit()

# Calcula e exibe a média das notas
media = calcular_media(nota1, nota2)
print(f"A média das notas é: {media}")