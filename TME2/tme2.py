
import numpy as np
import random

def init_tab_pref_etu(n):
     """
     retourne un tableau des preferences des n etudiants sur les 9 parcours du master
     """
     tab = np.zeros((n,9))
     for i in range(n):
         for j in range(9):
             tab[i,j] = random.randint(0,9)

     return tab

def init_tab_pref_master(n):
     """
     retourne un tableau des preferences des 9 parcours du master sur les n etudiants.
     Les preferences seront aleatoires
     !!!!Pensez a definir les capacites d’accueil des parcours (la somme
devant faire n). On pourra generer des capacites de maniere deterministe (et par exemple a
peu pres  ́equilibrees entre les parcours).
     """
     tab = np.zeros((9,n))
     for i in range(9):
         for j in range(n):
             tab[i,j] = random.randint(0,9)

     return tab

print(init_tab_pref_etu(3))
