def tipo_triangulo(a, b, c):
    """
    Verifica o tipo de triângulo com base nos comprimentos de seus lados.

    Argumentos:
    a, b, c: float - Comprimentos dos lados do triângulo.

    Retorna:
    str - O tipo de triângulo ("equilátero", "isósceles", "escaleno") ou uma mensagem de erro.
    """
    # Verificar se os valores fornecidos podem formar um triângulo
    if a + b > c and a + c > b and b + c > a:
        # Verificar o tipo de triângulo
        if a == b == c:
            return "equilátero"
        elif a == b or a == c or b == c:
            return "isósceles"
        else:
            return "escaleno"
    else:
        return "Os valores fornecidos não podem formar um triângulo."

# Ler os valores dos lados do triângulo
a = float(input("Digite o comprimento do lado A do triângulo: "))
b = float(input("Digite o comprimento do lado B do triângulo: "))
c = float(input("Digite o comprimento do lado C do triângulo: "))

# Verificar o tipo de triângulo e exibir o resultado
print(tipo_triangulo(a, b, c))