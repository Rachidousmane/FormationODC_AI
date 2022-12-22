from processing import *
from DataTrans import *
from ExceptClass import *

reply1 = 1
#Boucle de la console
while(reply1 == 1):
    #Choix entre Exo1 et Exo2 et gestion de l'entrée du clavier
    try:
        reply= int(input("1- pour l'exo1\n"
                    "2- pour l'exo2\n"))
    except ValueError:
        print("Veuillez Taper 1 ou 2")
    else:
        if(reply == 1):
            print("Bienvenue au calcul de R, Exo1")
            Q1 = input("Voulez-vous continuer?\n(Oui ou Nom)")
            #Boucle de l'Exo1
            while(Q1 == "O" or Q1 == "oui" or Q1 == "o"):
                try:
                    N = int(input("Donnez la valeur limite de la liste\n"))
                    if N <= 0 :
                        raise Exception
                except ValueError:
                    print("Veillez entrer un nombre entier")
                except Exception:
                    print("Veillez entrer un nombre entier strictement positif")
                else:
                    task1 = processing(N)
                    print("Début d'un nouveau traitement ")

                    task1.execute()
                    print("Fin detraitement ")

                    Q2 = input("Voulez-vous quitter? (O ou N)")
                    if(Q2 == "oui" or Q2 == "O" or Q2 == 'o'):
                        quit()
                    else: continue
        elif(reply ==2):
            print("Bienvenue à l'Exo2")
            Q1 = input("Voulez-vous continuer?\n(Oui ou Nom)")
            #Boucle de l'exo2
            while(Q1 == "O" or Q1 == "oui" or Q1 == "o"):
                try: 
                    print("Donner le nombre de liste : ")
                    n = int(input())
                    print("Donner une taille chaque liste : ")
                    s = int(input())
                    if (n<0 or n==0):
                        raise ExceptClass(n) #Lévée d'une exception personnalisée
                    if (s<0 or n==0):
                        raise ExceptClass(s) #Lévée d'une exception personnalisée
                        
                except IndexError as err:
                    print(err)
                except ValueError:
                    print("Pour les nombres entrés, ils doivent être entiers")
                except ExceptClass: # Exception de la classe ExceptClass
                    pass
                except NameError:
                    print("Une variable non declare") #Pour aider nous programmeur
                else:
                    A1 = DataTrans(n, s)
                    D = list()
                    i = 0
                    while i < n:
                        D.append(A1.G())
                        i += 1
                    print("La liste est D : ", D)
                    L = list()
                    p = 0
                    while p<n:
                        print("\nLe Min de la", p ,"ième liste est", A1.MIN(D[p]))
                        L.append(A1.MIN(D[p]))
                        p+=1
                    u = 0
                    while u<n:
                        print("\nLe Max de la", u ,"ième liste est", A1.MAX(D[u]))
                        L.append(A1.MAX(D[u]))
                        u+=1

                    print("\nle minimun global de la liste D est : ",A1.MIN(L))
                    print("\nle maximun global de la liste D est : ",A1.MAX(L))
                    D1 = list(())
                    i = 0
                    while i < n:
                        D1.append(A1.image(D[i]))
                        i += 1
                    print("\nla liste D1 est : ",D1)

                    Q2 = input("Voulez-vous quitter? (O ou N)\n")
                    if(Q2 == "oui" or Q2 == "O" or Q2 == 'o'):
                        quit()
                    else: continue
        else:
            reply1= int(input("taper 1 pour Reessayer\n"
                "Taper n'immporte quelle touche pour Quitter la console\n"))
            if(reply1 != 1):
                quit()
            else:
                continue 