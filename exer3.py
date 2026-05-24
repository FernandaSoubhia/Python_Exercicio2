#Regras:
#- Custo base:
#- Até 20 kg:
#- R$ 1,80 por km
#- Acima de 20 kg:
#- R$ 2,75 por km
#- Se a entrega for prioritária:
#- Acrescentar 25%
#- Regiões:
#- Sul e Sudeste:
#- Sem taxa extra
#- Centro-Oeste:
#- Acrescentar 8%
#- Norte e Nordeste:
#- Acrescentar 15%
#- Se:
#- Peso > 50 kg E distância > 800 km
#- OU entrega prioritária em região Norte
#- Aplicar taxa de risco de 18%
#- Se o cliente tiver cupom de desconto E o valor ultrapassar R$ 2000:
#- Desconto de 10%
#- Se o valor final ficar acima de R$ 5000:
#- Acrescentar seguro obrigatório de R$ 350
#O programa deve:
#- Ler peso
#- Ler distância
#- Ler região
#- Ler se é prioritária
#- Ler se possui cupom
#- Calcular valor total do frete
peso = float(input("Digite o peso da carga (kg): "))
distancia = float(input("Digite a distância (km): "))
regiao = input("Digite a região (Sul, Sudeste, Centro-Oeste, Norte, Nordeste): ")
prioritaria = input("A entrega é prioritária? (sim/não): ")
cupom = input("Possui cupom de desconto? (sim/não): ")

#Regras:
if peso <= 20:
    valor = distancia * 1.80
else:
    valor = distancia * 2.75


if prioritaria == "sim":
    valor *= 1.25

if regiao == "Centro-Oeste":
    valor *= 1.08

elif regiao == "Norte" or regiao == "Nordeste":
    valor *= 1.15


if (peso > 50 and distancia > 800) or (prioritaria == "sim" and regiao == "Norte"):
    valor *= 1.18


if cupom == "sim" and valor > 2000:
    valor *= 0.90


if valor > 5000:
    valor += 350


print("Valor total do frete: R$", round(valor, 2))