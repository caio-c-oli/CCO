def conta_letras(palavra):
    contagens={}
    for i in palavra:
        if i in palavra:
            contagens[i] = contagens[i] +1
        else:
            contagens[i] = 1
            print(i)
    

conta_letras('abacaxi')