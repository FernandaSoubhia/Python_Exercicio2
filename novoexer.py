#1. Receba as seguintes informações do usuário:
#○ idade (inteiro)-
#○ senha (string)-
#○ tem_convite (booleano: True ou False)-
#○ assinatura (string: 'gratuita', 'premium', 'vip')-
#○ horario (inteiro de 0 a 23, representando a hora do dia)
#2. Determine se o usuário pode acessar a plataforma seguindo estas regras
#complexas:
#○ Acesso permitido se:
#1. O usuário tem mais de 18 anos e a senha é '1234'.
#2. Ou se o usuário tem convite e a idade é entre 16 e 18 anos, inclusive.
#3. Ou se a assinatura for 'premium' ou 'vip', mas só entre 8h e
#20h.
#○ Usuários com assinatura 'vip' podem acessar a qualquer hora, mesmo sem senha ou convite.
#○ Usuários com menos de 16 anos nunca podem acessar.
#3. Exiba mensagens específicas:
#○ "Acesso permitido" se puder entrar.
#○ "Acesso negado: idade insuficiente" se tiver menos de 16 anos.
#○ "Acesso negado: fora do horário de acesso" se estiver fora do horário
#permitido para premium.
#○ "Acesso negado: senha ou convite incorretos" para todos os outros casos.


idade=int(input('Digite sua idade: '))
senha=int(input('Digite sua senha: '))
temconv=input('Digite se você tem convite: ')
assinatura=input('Digite o tipo de assinatura: ')

