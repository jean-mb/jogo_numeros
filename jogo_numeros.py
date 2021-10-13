import random

# ======================= APRESENTAÇÃO =================================
print('===========')
print('Adivinhação')
print('===========')
# ======================= INSTRUÇÃO ====================================
print('===================================================================')
print('O seu objetivo é adivinhar o número que EU pensar, entre 1 e 100:')
print('\nEu vou responder apenas se: ')
print(' Seu chute está CERTO\n Seu chute está ALTO \n Seu chute está BAIXO')
print('===================================================================')

#-------- CONDIÇÕES --------
chances = int(input(' - Digite quantas chances você quer ter para adivinhar o número -> '))
tentativa = 1
numero_secreto = random.randrange(1,101)

# ================================== LÓGICA ==========================================
while tentativa <= chances:

    print('===================================================================')
  
    chute = int(input(' - Digite seu chute -> '))
    print(f'\n TENTATIVA {tentativa}')
    
    if chute == numero_secreto:
        print(f'Eba! Você acertou em {tentativa} tentativas')
        break
    else:
        if chute < numero_secreto:
            print('Palpite baixo!')
        elif chute > numero_secreto:
            print('Palpite alto!')

        tentativa += 1
    