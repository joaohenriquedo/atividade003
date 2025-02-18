municipio = input("Informe o nome do município: ")
eleitores = int(input("Informe a quantidade de eleitores: "))
votos = int(input("Informe a quantidade de votos do candidato mais votado: "))
if eleitores >= 200000:
    percentual_votos = (votos /eleitores) * 100
    if percentual_votos > 50:
        print("no município de {}, não haverá segundo turno.".format(municipio))
    else:
        print("no município de {}, haverá segundo turno.".format(municipio))
else:
    print("o município de {}, não há necessidade de segundo turno.".format(municipio))