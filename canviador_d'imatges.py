def escriu_capçalera(nom_fitxer):
    with open(nom_fitxer, mode='w') as imatge:
        imatge.write('P1\n')
        imatge.write('3 3')
if __name__=='__main__':
    nom_fitxer=input()
    escriu_capçalera(nom_fitxer)
    