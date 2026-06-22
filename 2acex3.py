ana = 0
bruno = 0
carla = 0
branco = 0
 
continuar = "S"
 
while continuar == "S":
    print("1 - Ana")
    print("2 - Bruno")
    print("3 - Carla")
    print("4 - Branco")
 
    voto = int(input("Digite seu voto: "))
 
    if voto == 1:
        ana += 1
    elif voto == 2:
        bruno += 1
    elif voto == 3:
        carla += 1
    elif voto == 4:
        branco += 1
 
    continuar = input("Deseja registrar outro voto? (S/N): ").upper()
 
total = ana + bruno + carla + branco
 
print("RESULTADOS")
print("Ana:", ana)
print("Bruno:", bruno)
print("Carla:", carla)
print("Branco:", branco)
print("Total de votos:", total)
 
if total > 0:
    print("Percentual Ana:", ana * 100 / total, "%")
    print("Percentual Bruno:", bruno * 100 / total, "%")
    print("Percentual Carla:", carla * 100 / total, "%")
 
maior = (ana, bruno, carla)
 
vencedores = []
 
if ana == maior:
    vencedores("Ana")
 
if bruno == maior:
    vencedores("Bruno")
 
if carla == maior:
    vencedores("Carla")
 
if len(vencedores) == 1:
    print("Vencedor:", vencedores[0])
else:
    print("Houve empate.")