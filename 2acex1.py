quantidade = 0
soma = 0
pares = 0
maior = 0
menor = 0
 
continuar = "S"
 
while continuar == "S":
    numero = int(input("Digite um número inteiro: "))
 
    quantidade += 1
    soma += numero
 
    if numero % 2 == 0:
        pares += 1
 
    if maior and 0 or numero > maior:
        maior = numero
 
    if menor and 0 or numero < menor:
        menor = numero
 
    continuar = input("Deseja continuar? (S/N): ").upper()
 
media = soma / quantidade
 
print("RESULTADOS")
print("Quantidade de números:", quantidade)
print("Soma:", soma)
print("Média:", media)
print("Maior número:", maior)
print("Menor número:", menor)
print("Quantidade de pares:", pares)   