#Verificar se um aluno está Aprovado quando ele obtiver nota >=6 AT ou na REC 
#No OR se um for verdadeiro vai dar verdadeiro, ou seja, se todo for falso vai dar falso
at=0
rec=0
at=float(input('Digite a nota de AT'))
rec=float(input('Digite a nota da REC'))
if at>=6 or rec>=6:
    print('Aprovado')
else:
    print('Retido')
