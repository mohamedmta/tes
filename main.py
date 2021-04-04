USD = 1.18
GBP = 0.85

devise = int(input('Quelle monnaie souhaitez-vous avoir? \n'
                   '1-USD \n'
                   '2-GBP\n'))

print(devise)

if devise == 1:
    print('Vous souhaitez des dollars, 1 EUR vaut', USD, 'USD.Entrez le montant à convertir :')
    valeur = int(input())
    montant = valeur * USD
    print('Vous souhaitez convertir', valeur, 'Le montant en dollars est de', montant)
else:
    print('Vous souhaitez des livres, 1 EUR vaut', GBP, 'GBP.Entrez le montant à convertir :')
    valeur = int(input())
    montant = valeur * GBP
    print('Vous souhaitez convertir', valeur, 'Le montant en livres est de', montant)
pass
