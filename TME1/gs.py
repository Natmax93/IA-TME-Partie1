#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 11:03:34 2023

@author: 28603668
"""

def lec_pref_etu(nom_fic):
    """
    Lit les préférences des étudiants dans le fichier 'nom_fic' et
    retourne la matrice de préférences correspondante.
    """
    
    monFichier = open(nom_fic, "r") # Ouverture en lecture. Indentation par rapport a la ligne d'avant (<-> bloc).
    contenu = monFichier.readlines() # Contenu contient une liste de chainces de caracteres, chaque chaine correspond a une ligne       
    monFichier.close() #Fermeture du fichier
    
    # matrice résultat
    mat = []
    
    for i in range(1, len(contenu)):
        mat.append(contenu[i].split())
        mat[i-1].pop(0)
        mat[i-1].pop(0)
        
    return mat

def lec_pref_spe(nom_fic):
    """
    Lit les préférences des spécialités dans le fichier 'nom_fic' et
    retourne la matrice de préférences correspondante.
    """
    
    monFichier = open(nom_fic, "r") # Ouverture en lecture. Indentation par rapport a la ligne d'avant (<-> bloc).
    contenu = monFichier.readlines() # Contenu contient une liste de chainces de caracteres, chaque chaine correspond a une ligne       
    monFichier.close() #Fermeture du fichier
    
    # matrice résultat
    mat = []
    
    for i in range(2, len(contenu)):
        mat.append(contenu[i].split())
        mat[i-2].pop(0)
        mat[i-2].pop(0)
        
    return mat

def get_capacite(nom_fic):
    """
    Renvoie le tableau des capacités de chaque spécialités définies
    dans le fichier nom_fic
    """
    
    monFichier = open(nom_fic, "r") # Ouverture en lecture. Indentation par rapport a la ligne d'avant (<-> bloc).
    contenu = monFichier.readlines() # Contenu contient une liste de chainces de caracteres, chaque chaine correspond a une ligne       
    monFichier.close() #Fermeture du fichier
    
    liste = contenu[1].split()
    liste.pop(0)
    return liste

def GaleShapley_CE(fic_etu, fic_spe):
    """
    Retourne un mariage parfait et stable côté étudiant sous forme
    d'ensemble de couple.
    """
    
    mariage = dict()
    matEtu = lec_pref_etu(fic_etu)
    matSpe = lec_pref_spe(fic_spe)
    capacite = get_capacite(fic_spe)
    
    # Initialisation de la capacité des spés
    capaciteSpe = dict()
    i = 0
    for c in capacite:
        capaciteSpe[i] = c
        i += 1
    
    # Initialisation du statut des étudiants (affecté ou non)
    statutsEtu = dict()
    for i in range(len(matEtu)):
        statutsEtu[i] = False
        
    # Parcours de la matrice des étudiants
    etu = 0
    for prefs in matEtu:
        spe = prefs.pop(0)
        if capaciteSpe[spe] > 0:
            capaciteSpe[spe] -= 1
            statutsEtu[etu] = True
        else:
            # On cherche un étudiant qui est moins préféré par la spécialité
            # que l'étudiant courant
            dernier = mariage[spe][0]
            place = 0
            
            for i in range(1, len(mariage[spe]) - 1):
                affecte = mariage[spe][i]
                if matSpe[spe][affecte] < matSpe[spe][dernier]:
                    dernier = affecte
                    place = i
                    
            if matSpe[spe][dernier] < matSpe[spe][etu]:
                mariage[spe][place] = etu
                statutsEtu[etu] = True
                statutsEtu[dernier] = False
        etu += 1

    