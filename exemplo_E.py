#Liberar a entrada a um evento apenas a quem tem: pelo menos 16 anos e possuir ingresso
#upper pega o que o usuario digitou, e coloca em maiusculo 
#No AND se um der falso ele vai dar falso, tudo tem que ser verdadeiro para ser verdade
idade=int(input('Digite sua idade:'))
ingresso=input('Possui Ingresso? (S/N) ')

if idade>=16 and ingresso=='S':
    print('Entrada permitida')
else:
    print('Entrada negada')

