#Peça ao usuário:
#- nome do funcionário-
#- quantidade de tarefas concluídas no mês-
#- quantidade de erros cometidos-
#Regras:
#- Se concluiu menos de 20 tarefas:-
#- desempenho baixo-
#- Se concluiu 20 ou mais tarefas:-
#- Se cometeu mais de 10 erros → desempenho regular-
#- Se cometeu entre 5 e 10 erros → desempenho bom
#- Se cometeu menos de 5 erros → desempenho excelente
#Exiba:
#- Nome do funcionário
#- Nível de desempenho
 
 
nomefuncionario=input('Digite o nome do funcionário: ')
quanttarefas=int(input('Digite a quantidade de tarefas concluídas no mês: '))
quanterros=int(input('Digite a quantidade de erros cometidos: '))
 
 
print('Nome do funcionário:')
print(nomefuncionario)
print('Nível de desempenho de tarefas:')

if quanttarefas<=20: 
    print('Desempenho baixo')

print('Nível de desempenho por erros em tarefas: ')

if quanterros < 5:
    print('Desempenho excelente')
elif quanterros < 10:
    print('Desempenho bom')
else:
    print('Desempenho regular')



