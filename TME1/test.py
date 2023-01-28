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
print(gs.GaleShapley_CE("PrefEtu.txt", "PrefSpe.txt"))
print()
print("GS homme-optimal du TD : ")
print(gs.GaleShapley_CE("hommes.txt", "femmes.txt"))
print()