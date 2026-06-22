aprovados = 0
recuperacao = 0
reprovados = 0
 
maior_media = 0
melhor_aluno = ""
 
for i in range(10):
    print(f"Aluno {i+1}")
 
    nome = input("Nome: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
 
    media = (nota1 + nota2) / 2
 
    print("Média:", media)
 
    if media >= 7:
        aprovados += 1
    elif media >= 5:
        recuperacao += 1
    else:
        reprovados += 1
 
    if media > maior_media:
        maior_media = media
        melhor_aluno = nome
 
print("RESULTADOS")
print("Quantidade de alunos cadastrados: 10")
print("Aprovados:", aprovados)
print("Recuperação:", recuperacao)
print("Reprovados:", reprovados)
print("Aluno com maior média:", melhor_aluno)
print("Maior média:", maior_media) 