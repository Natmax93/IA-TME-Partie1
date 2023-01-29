#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 12:25:30 2023

@author: 28603668
"""

import gs

print("Préférences des étudiants :")
print(gs.lec_pref_etu("PrefEtu.txt"))
print()
print("Préférences des spécialités :")
print(gs.lec_pref_spe("PrefSpe.txt"))
print()
print("Capacité des spés : " + str(gs.get_capacite("PrefSpe.txt")))
print()
print("GS côté étudiant : ")
mariage_cote_etu = gs.GaleShapley_CE("PrefEtu.txt", "PrefSpe.txt")
print(mariage_cote_etu)
print("paire instable : " + str(gs.unstable_pair("PrefEtu.txt", "PrefSpe.txt", mariage_cote_etu)))
print()
print("GS homme-optimal du TD : ")
mariage_homme_opti = gs.GaleShapley_CE("hommes.txt", "femmes.txt")
print(mariage_homme_opti)
print("paire instable : " + str(gs.unstable_pair("hommes.txt", "femmes.txt", mariage_homme_opti)))
print()
print("GS côté spécialité : ")
mariage_cote_spe = gs.GaleShapley_CP("PrefEtu.txt", "PrefSpe.txt")
print(mariage_cote_spe)
print("paire instable : " + str(gs.unstable_pair("PrefEtu.txt", "PrefSpe.txt", mariage_cote_spe)))
print()
print("GS femme-optimal du TD : ")
mariage_femme_opti = gs.GaleShapley_CP("hommes.txt", "femmes.txt")
print(mariage_femme_opti)
print("paire instable : " + str(gs.unstable_pair("hommes.txt", "femmes.txt", mariage_femme_opti)))
print()
mariage_instable = {1:{1}, 2:{0}, 3:{2}, 0:{3}}
print("Un mariage du TD : " + str(mariage_instable))
print("Paire instable : " + str(gs.unstable_pair("hommes.txt", "femmes.txt", mariage_instable)))

