salario = float(input("digite o valor do salário: "))
parcela = float(input("digite o valor da parcela: "))
if parcela <= 0.08 * salario:
    print("empréstimo concedido!")
else:
    print("empréstimo não concedido.")
    print("joão Henrique")