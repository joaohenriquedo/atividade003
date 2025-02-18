risco = input("Informe o grau de aceitação de risco (BX para baixo ou AL para alto): ")
valor = int (input("Informe o valor a ser investido: "))
if risco not in ["BX", "AL"]:
        print("Dados inválidos para o grau de aceitação de risco.")
           
if risco == "BX":
                if valor < 1000:
                    print("Aplicação recomendada: Poupança")
                else:
                    print("Aplicação recomendada: Renda Fixa")
elif risco == "AL":
                if valor < 1000:
                    print("Aplicação recomendada: Bitcoins")
                else:
                    print("Aplicação recomendada: Ações")
else:
            print("Dados inválidos para o valor. Informe um número real.")