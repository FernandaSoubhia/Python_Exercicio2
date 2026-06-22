total = 0
acima_1000 = 0
 
mais_barato_nome = ""
mais_barato_preco = 0
 
mais_caro_nome = ""
mais_caro_preco = 0
 
continuar = "S"
 
while continuar == "S":
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: R$ "))
 
    total += preco
 
    if preco > 1000:
        acima_1000 += 1
 
    if mais_barato_nome == "" or preco < mais_barato_preco:
        mais_barato_nome = nome
        mais_barato_preco = preco
 
    if mais_caro_nome == "" or preco > mais_caro_preco:
        mais_caro_nome = nome
        mais_caro_preco = preco
 
    continuar = input("Deseja cadastrar outro produto? (S/N): ").upper()
 
print("RESULTADOS")
print("Valor total gasto: R$", total)
print("Produtos acima de R$1000:", acima_1000)
print("Produto mais barato:", mais_barato_nome, "- R$", mais_barato_preco)
print("Produto mais caro:", mais_caro_nome, "- R$", mais_caro_preco)   
