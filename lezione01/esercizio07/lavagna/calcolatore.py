def ottieniRisposta(numeroMagico, potenza):
    if(int(input("Il numero pensato è tra i seguenti? (1 per dire sì)"))==1):
        numeroMagico = numeroMagico+pow(2, potenza) 
    return numeroMagico