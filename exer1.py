#Regras:
#- Se o cliente for residencial:
#- Até 200 kWh: R$ 0,45 por kWh
#- Acima de 200 kWh: R$ 0,65 por kWh
#- Se o cliente for comercial:
#- Até 500 kWh: R$ 0,55 por kWh
#- Acima de 500 kWh: R$ 0,80 por kWh
#- Se o consumo ocorrer no horário de pico:
#- Acrescentar 15% ao valor final
#- Se o cliente tiver consumo acima de 1000 kWh OU estiver inadimplente:
#- Aplicar multa de 12%
#- Se o cliente for residencial E consumir menos de 80 kWh E não estiver inadimplente:
#- Aplicar desconto de 20%
#O programa deve:
#- Ler tipo de cliente
#- Ler consumo
#- Ler se está em horário de pico
#- Ler se está inadimplente= descumprimento
#- Calcular valor final da conta
tipo = input("Digite o tipo do cliente (residencial/comercial): ")
consumo = float(input("Digite o consumo em kWh: "))
pico = input("Está em horário de pico? (sim/não): ")
inadimplente = input("Está em descumprimento? (sim/não): ")

#Regras:
if tipo == "residencial":
    if consumo <= 200:
        valor = consumo * 0.45
    else:
        valor = consumo * 0.65

elif tipo == "comercial":
    if consumo <= 500:
        valor = consumo * 0.55
    else:
        valor = consumo * 0.80

if pico == "sim":
    valor *= 1.15\


if consumo > 1000 or inadimplente == "sim":
    valor *= 1.12


if tipo == "residencial" and consumo < 80 and inadimplente == "não":
    valor *= 0.80

print("Valor final da conta: R$ {valor:.2}")