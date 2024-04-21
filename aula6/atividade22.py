# Dicionário com as taxas de imposto de cada estado
taxas_imposto = {'MG': 0.07, 'SP': 0.12, 'RJ': 0.15, 'MS': 0.08}

# Recebe o valor e o estado destino do usuário
valor_produto = float(input("Digite o valor do produto: "))
estado_destino = input("Digite o estado destino do produto (MG, SP, RJ, MS): ")

# Verifica se o estado destino é válido
if estado_destino in taxas_imposto:
    # Calcula o preço final do produto com base na taxa de imposto do estado
    taxa_imposto = taxas_imposto[estado_destino]
    preco_final = valor_produto * (1 + taxa_imposto)
    print(f"O preço final do produto para o estado {estado_destino} é: R${preco_final:.2f}")
else:
    print("Estado destino inválido. Por favor, digite um estado válido.")