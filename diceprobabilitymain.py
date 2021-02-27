import matplotlib.pyplot
import random
import time

numTentativas = int(input('Quantas vezes deseja realizar lançamentos?'))
totalLancaçamentos = numTentativas

def probabilidade():
    tentativas = 1
    dadosIguais = 0
    while tentativas <= numTentativas:
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        if d1 == d2:
            dadosIguais += 1
            print(f'DADOS IGUAIS! ({d1}, {d2})')
        else:
            print(f'LANÇAMENTO NORMAL! ({d1}, {d2})')
        tentativas += 1
        #time.sleep(.1)
    matplotlib.pyplot.bar('Quantidade de lançamentos iguais', dadosIguais)
    matplotlib.pyplot.bar('Quantidade total de lançamentos', numTentativas)
    matplotlib.pyplot.show()
probabilidade()
        
