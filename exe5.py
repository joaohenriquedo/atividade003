
preco_custo = float(input("informe o preço de custo do produto: R$ "))
if preco_custo <= 100:
    margem_bruta = 0.45 
else:
    margem_bruta = 0.35  
preco_venda = preco_custo * (1 + margem_bruta)
print("o preço de venda do produto é: R$ {}".format(preco_venda))
print("joão Henrique")