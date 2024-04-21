# Recebe a hora de chegada e de partida do usuário
chegada_hora, chegada_minuto = map(int, input("Digite a hora de chegada (hh mm): ").split())
partida_hora, partida_minuto = map(int, input("Digite a hora de partida (hh mm): ").split())

# Calcula o tempo total de estacionamento em minutos
tempo_total = ((partida_hora - chegada_hora) * 60) + (partida_minuto - chegada_minuto)

# Calcula o número de horas arredondadas por excesso
num_horas = (tempo_total + 59) // 60

# Calcula o preço do estacionamento com base no número de horas
if num_horas <= 2:
    preco = num_horas * 1.00
elif num_horas <= 4:
    preco = 2 * 1.00 + (num_horas - 2) * 1.40
else:
    preco = 2 * 1.00 + 2 * 1.40 + (num_horas - 4) * 2.00

# Exibe o preço cobrado pelo estacionamento
print(f"O preço cobrado pelo estacionamento é: R$ {preco:.2f}")