def calcular_area_trapezio(base_maior, base_menor, altura):
    """
    Calcula a área de um trapézio.

    Argumentos:
    base_maior: float - Comprimento da base maior do trapézio.
    base_menor: float - Comprimento da base menor do trapézio.
    altura: float - Altura do trapézio.

    Retorna:
    float - A área do trapézio.
    """
    # Verificar se as bases são números maiores que zero
    if base_maior > 0 and base_menor > 0:
        # Calcular a área do trapézio
        area = ((base_maior + base_menor) * altura) / 2
        return area
    else:
        return "Erro: As bases devem ser números maiores que zero."

# Ler os valores das bases e da altura do trapézio fornecidos pelo usuário
base_maior = float(input("Digite o comprimento da base maior do trapézio: "))
base_menor = float(input("Digite o comprimento da base menor do trapézio: "))
altura = float(input("Digite a altura do trapézio: "))

# Calcular a área do trapézio
area_trapezio = calcular_area_trapezio(base_maior, base_menor, altura)

# Exibir a área do trapézio
print(f"A área do trapézio é: {area_trapezio}")