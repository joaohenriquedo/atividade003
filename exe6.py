municipio = input("Informe o nome do município: ")
eleitores = float(input("Informe a quantidade de eleitores: "))
votos = float(input("Informe a quantidade de votos do candidato mais votado: "))
percentual_votos = (votos /eleitores) * 100
if percentual_votos >0.50:
        print("no município de {}, haverá segundo turno.".format(municipio))
else:
    print("o município de {}, não há necessidade de segundo turno.".format(municipio))
    print("joão Henrique")
