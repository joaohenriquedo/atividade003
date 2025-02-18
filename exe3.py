salario = int(input("insira seu salario:"))
parcela = int(input("insira sua parcela"))
emprestimo = int(input("insira o valor do emprestimo"))
taxa = salario * 0.8
if taxa > salario:
    print("trasição negada")
else:
    print("transição aprovada")