#Peça ao usuário:
#- o valor total da compra-
#- a forma de pagamento (dinheiro, pix ou cartao)-
#Regras:
#- Se for dinheiro ou pix:
#- Até R$ 100 → 5% de desconto-
#- Acima de R$ 100 → 10% de desconto-
#- Se for cartao:
#- Até R$ 100 → sem desconto-
#- Acima de R$ 100 → 5% de desconto-
#Exiba:
#- Valor do desconto-
#- Valor final da compra-      




valortotal=int(input('Digite o valor total da compra: '))
formadepagamento=input('Digite a forma de pagamento(dinheiro, pix ou cartão): ')
 

if formadepagamento == "pix" or formadepagamento == "dinheiro":
    if valortotal <= 100:
        valorfinal = valortotal * 0.95
        print('Você tem um desconto de 5%')
    elif valortotal >100:
        valorfinal = valortotal * 0.9
        print('Você tem um desconto de 10%')
elif formadepagamento == "cartão":
    if valortotal <= 100:
            print('Você não tem desconto sobre este valor')
    elif  valortotal >100:
        valorfinal = valortotal * 0.95
        print('Você tem um desconto de 5%')

#exiba:
print(valorfinal)


 
