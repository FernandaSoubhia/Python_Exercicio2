#Para compra de um bem, verificar se o usuário tem um salário maior que R$5000,00
#O NO é para ter um fim, ou seja, em listas temos fim e este fim tem que ser definido 
salario=float(input('Digite seu salario'))
if not salario>5000:
    print ('Compra negada')
else: 
    print ('Compra aprovada')
