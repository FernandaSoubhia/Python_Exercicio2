#Peça ao usuário:
#- sua idade-
#Regras:
#- Se a idade for menor que 12 → criança
#- Se for entre 12 e 17 → adolescente
#- Se for entre 18 e 59 → adulto
#- Se for 60 ou mais → idoso
#Exiba:
#- A classificação correspondente
 
idade=int(input('Digite sua idade: '))
if idade<12:
     print('Criança')
elif idade<=17:
     print('Adolescente')
elif idade<=59:
     print('Adulto')
elif idade>=60:
     print('Idoso')
     