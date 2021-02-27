#Importing libraries
import matplotlib.pyplot #pip install matplotlib
import random #Natibe lib
import time #Native lib

#Asking for input
numTentativas = int(input('[EN] How many times do you wanna roll the dices? / [PT-BR] Quantas vezes deseja jogar os dados?')) 
totalLancaçamentos = numTentativas

#Defining the function and the loop
def probabilidade():
    tentativas = 1
    dadosIguais = 0
    while tentativas <= numTentativas:
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        if d1 == d2:
            dadosIguais += 1
            print(f'[PT-BR] DADOS IGUAIS! / [EN] EQUAL DICES! - ({d1}, {d2})')
        else:
            print(f'[PT-BR] LANÇAMENTO NORMAL! / [EN] NON EQUAL DICES! - ({d1}, {d2})')
        tentativas += 1
        #time.sleep(.1) - You can use that if you want a nice interval of between results
    matplotlib.pyplot.bar('[EN] Number of equal dices / [PT-BR] Números de lançamentos iguais', dadosIguais)
    matplotlib.pyplot.bar('[EN] Total number of launches / [PT-BR] Número total de lançcamentos', numTentativas)
    matplotlib.pyplot.show() 
    #Showing the graphs/results 
probabilidade()
        
