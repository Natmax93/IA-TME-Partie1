#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 12:25:30 2023

@author: 28603668
"""

import gs

print(gs.lec_pref_etu("PrefEtu.txt"))
print()
print(gs.lec_pref_spe("PrefSpe.txt"))
print("Capacité des spés : " + str(gs.get_capacite("PrefSpe.txt")))
print("GS côté étudiant : ")
#gs.GaleShapley_CE("PrefEtu.txt", "PrefSpe.txt")