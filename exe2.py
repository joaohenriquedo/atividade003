nome = input("digite seu nome")
peso = int(input("digite seu peso"))
if peso >= 52 and peso <65:
    print("{} sua categoria é pena".format(nome))
elif peso >=65 and peso <72:
    print("{} sua categoria é leve".format(nome))
elif peso >= 72 and peso <79:
    print("{} sua categoria é ligeiro".format(nome))
elif peso >=79 and peso <86:
    print("{} sua categoria é medio".format(nome))
elif peso >=86 and peso <90:
    print("{} sua categoria é medio")
elif peso >=86 and peso <100:
    print("{} sua categoria é meio pesado")
elif peso >=100:
    print("{} sua categoria é pesado")
else:
    print("catogoria invalida")
    print("joão Henrique")
    