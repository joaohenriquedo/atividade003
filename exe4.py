sexo = input("informe seu sexo (homem ou mulher): ").lower()
idade = int(input("informe sua idade: "))

if sexo == "mulher":
    if 21 <= idade <= 34:
        print("você pode se alistar.")
    else:
        print("você não atende à faixa etária para o alistamento.")
elif sexo == "homem":
    if 18 <= idade <= 39:
        print("você pode se alistar.")
    else:
        print("você não atende à faixa etária para o alistamento.")
else:
    print("sexo inválido. Por favor, informe 'homem' ou 'mulher'.")
print("joão Henrique")