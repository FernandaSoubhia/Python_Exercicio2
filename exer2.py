#Regras:
#- O cliente só pode solicitar empréstimo se:
#- Tiver idade maior ou igual a 21 anos
#- E salário maior ou igual a R$ 2500
#- Se o score for:
#- Maior ou igual a 800:
#- Juros de 1,2% ao mês
#- Entre 600 e 799:
#- Juros de 2,5% ao mês
#- Menor que 600:
#- Juros de 4% ao mês
#- Se o valor solicitado for maior que 10 vezes o salário:
#- Empréstimo negado
#- Se o cliente tiver score abaixo de 500 E solicitar acima de R$ 50.000:
#- Empréstimo negado imediatamente
#- Caso aprovado:
#- Calcular o valor total a pagar em 24 meses usando juros compostos
#Fórmula:
#M = C(1+i)^t
#Onde:
#- M = montante final
#- C = valor do empréstimo
#- i = taxa de juros mensal
#- t = quantidade de meses
#O programa deve exibir:
#- Se foi aprovado
#- Taxa aplicada
#- Valor total a pagar
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário: "))
score = int(input("Digite seu score de crédito: "))
valor = float(input("Digite o valor do empréstimo: "))

#Regras:
if idade >= 21 and salario >= 2500:

    
    if valor > salario * 10:
        print("Empréstimo negado")

    elif score < 500 and valor > 50000:
        print("Empréstimo negado imediatamente")

    else:
       
        if score >= 800:
            taxa = 0.012

        elif score >= 600:
            taxa = 0.025

        else:
            taxa = 0.04

        #conta do juros compostos
        montante = valor * (1 + taxa) ** 24

        print("Empréstimo aprovado")
        print("Taxa aplicada:", taxa * 100, "%")
        print("Valor total a pagar:", round(montante, 2))

else:
    print("Cliente não pode solicitar empréstimo")