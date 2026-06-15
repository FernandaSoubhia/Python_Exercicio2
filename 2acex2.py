#Desenvolva um programa para registrar produtos de uma loja.
#Para cada produto, o usuário deve informar:
#- Nome do produto;-
#- Preço.-
#Após cada cadastro, pergunte:
#Deseja cadastrar outro produto? (S/N)
#Ao encerrar, exiba:
#- Valor total gasto na compra;
#- Quantos produtos custam mais de R$ 1.000,00;
#- Nome e preço do produto mais barato;
#- Nome e preço do produto mais caro.
produto=input('Digite o nome do produto ')
preço=float(input('Digite o preço do produto: '))

while opcao.upper()=='S':
    opcao=input('Deseja continuar (S/N): ')

print('')

