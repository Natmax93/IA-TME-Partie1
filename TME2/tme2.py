import numpy as np
import matplotlib.pyplot as plt
import time
import random
import gs

def init_tab_pref_etu(n):
     """
     retourne un tableau des preferences des n etudiants sur les 9 parcours du
     master et génène un fichier des préférences des étudiants sous le bon
     bon format.
     """

     fichier = open("PrefEtuGen.txt", "w")

     # Première ligne
     fichier.write(str(n) + "\n")

     # liste des masters qui n'ont pas été ajoutés
     listeMaster = [i for i in range(0,9)]

     for i in range(n):
         fichier.write(str(i) + "\tEtu" + str(i) + "\t")
         for j in range(9):
             pref = random.randint(0,len(listeMaster)-1)
             fichier.write(str(listeMaster.pop(pref)) + "\t")
         fichier.write("\n")
         listeMaster = [i for i in range(0,9)]

     fichier.close()


def init_tab_pref_master(n):
     """
     retourne un tableau des preferences des 9 parcours du master sur les n
     etudiants.
     Les preferences seront aleatoires
     !!!!Pensez a definir les capacites d’accueil des parcours (la somme
    devant faire n). On pourra generer des capacites de maniere deterministe
    (et par exemple a peu pres  ́equilibrees entre les parcours).
     """

     fichier = open("PrefSpeGen.txt", "w")

     # Première ligne
     fichier.write("NbEtu " + str(n) + "\n")

     # Capacités
     mini = n//9
     nbMax = n%9

     fichier.write("Cap ")
     for i in range(9):
         if nbMax > 0:
             fichier.write(str(mini+1) + " ")
             nbMax -= 1
         else:
             fichier.write(str(mini) + " ")

     # Retour à la ligne
     fichier.write("\n")

     # liste des étudiants qui n'ont pas été ajoutés
     listeEtudiant = [i for i in range(0,n)]

     for i in range(9):
         fichier.write(str(i) + "\tSpe" + str(i) + "\t")
         for j in range(n):
             pref = random.randint(0,len(listeEtudiant)-1)
             fichier.write(str(listeEtudiant.pop(pref)) + "\t")
         fichier.write("\n")
         listeEtudiant = [i for i in range(0,n)]

     fichier.close()

def temps_calcul_GS(n, tabx, taby, gs):
    """
    Calcul le temps de notre algo GS pour un nombre n d'étudiants pour 10
    tests différents et écrit le

    Parameters
    ----------
    n : TYPE
        Le nombre d'étudiant pour le test.

    Returns
    -------
    le temps

    """
    somme_tmp = 0
    for i in range(10):
        init_tab_pref_etu(n)
        init_tab_pref_master(n)
        time1 = time.perf_counter()
        gs("PrefEtuGen.txt", "PrefSpeGen.txt")
        time2 = time.perf_counter()

        somme_tmp += time2-time1

    tabx.append(n)
    taby.append(somme_tmp/10)


def trace_courbe_temps_calcul(mini, maxi, gs):

    tabx = []
    taby = []

    assert mini < maxi

    while mini<maxi:
        temps_calcul_GS(mini, tabx, taby, gs)
        mini += 200

    plt.xlabel("n")
    plt.ylabel("tmp")
    plt.plot(tabx,taby)
    plt.show()


trace_courbe_temps_calcul(200, 2000, gs.GaleShapley_CE)
