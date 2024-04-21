# Recebe o salário do trabalhador e o valor da prestação do empréstimo
salario = float(input("Digite o salário do trabalhador: "))
prestacao = float(input("Digite o valor da prestação do empréstimo: "))

# Calcula 20% do salário
limite_prestacao = salario * 0.2

# Verifica se a prestação é maior que 20% do salário
if prestacao > limite_prestacao:
    print("Empréstimo não concedido")
else:
    print("Empréstimo concedido")