#Peça ao usuário:
#- valor do veículo-
#- valor de entrada-
#- quantidade de parcelas-
#- salário do comprador-
#Calcule:
#- valor financiado-
#- valor da parcela-
#Regras:
#1. Entrada mínima:
#- Se a entrada for menor que 20% do valor do veículo → financiamento negado
#2. Parcelamento:
#- Até 24 parcelas → juros de 5%
#- De 25 a 48 parcelas → juros de 10%
#- Acima de 48 parcelas → juros de 15%
#3. Aprovação:
#- A parcela não pode ultrapassar 30% do salário
#- Caso ultrapasse → financiamento negado
#Exiba:
#- Se o financiamento foi aprovado ou negado
#- Valor da parcela
#- Total pago com juros
 
 
valorveiculo=int(input('Digite o valor do veículo: '))
valorentrada=int(input('Digite o valor de entrada: '))
quantparcelas=int(input('Digite a quantidade de parcelas: '))
salarcomprador=int(input('Digite o salário do comprador: '))
 
valorfinanciado= valorveiculo-valorentrada
valorparcela=quantparcelas/valorentrada(valorveiculo-valorentrada)

if valorentrada<0.20:
    print('Financiamento negado')

