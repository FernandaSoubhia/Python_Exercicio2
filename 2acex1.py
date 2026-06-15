#Crie um programa que solicite ao usuário vários números inteiros.
#Após cada número digitado, pergunte:
#Deseja continuar? (S/N)
#Ao final, o programa deve exibir:
#- Quantidade total de números informados;
#- Soma de todos os números;
#- Média dos valores;
#- Maior número digitado;
#- Menor número digitado;
#- Quantidade de números pares.
numero=int(input('Digite vários números inteiros: '))
for i in range(numero+1):
    opcao='S'
while opcao.upper()=='S':
    opcao=input('Deseja continuar (S/N): ')

    