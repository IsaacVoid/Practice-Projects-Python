# Coin flip streaks
import random
number_streaks = 0
number_tryies = 20
total_toss = []
for experimentNumber in range(1):
    round_toss = []
    # Tiradas y creación del arreglo de una ronda de 100 intentos
    for toss in range(number_tryies):
        a = random.randint(0, 1)
        if a == 0:
            round_toss.append('H')
        else: 
            round_toss.append('T')
    # Buscar racha de 6 
    strek_H, strek_T = 0
    for b in range(len(round_toss)):
        try:
            if round_toss[b] == 'H': 
                strek_H =+ 1
            else: 
                strek_H = 0

            if round_toss[b] == 'T': 
                strek_T =+ 1
            else: 
                strek_T = 0
                    
        except:
            False
            
    print(round_toss)    

         
print(number_streaks)


'''
print(f'indice {a} = {flips[a]}')
print(f'{round_toss[b]}, {round_toss[b+1]}, {round_toss[b+2]}, {round_toss[b+3]}, {round_toss[b+4]}, {round_toss[b+5]}')


Esto no funciono: 
    try:
        if round_toss[b] and round_toss[b+1] and round_toss[b+2] and round_toss[b+3] and round_toss[b+4] and round_toss[b+5] == 'H':
            print('Seis seguidos')
            number_streaks += 1
        elif round_toss[b] and round_toss[b+1] and round_toss[b+2] and round_toss[b+3] and round_toss[b+4] and round_toss[b+5] == 'T':
            print('Seis seguidos')
            number_streaks += 1
        else:
            number_streaks += 0
    except:
        False
    
'''