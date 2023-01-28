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
        liste_tmp = contenu[i].split()
        liste_tmp.pop(0)
        liste_tmp.pop(0)
        for j in range(len(liste_tmp)):
            liste_tmp[j] = int(liste_tmp[j])
        mat.append(liste_tmp)
        
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
        liste_tmp = contenu[i].split()
        liste_tmp.pop(0)
        liste_tmp.pop(0)
        for j in range(len(liste_tmp)):
            liste_tmp[j] = int(liste_tmp[j])
        mat.append(liste_tmp)
        
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
    for j in range(len(liste)):
        liste[j] = int(liste[j])
    return liste

def interne_libre(matEtu, statutsEtu):
    """
    Fonction qui cherche et retourne un étudiant non affecté
    qui n'a pas demandé à tous les parcours.
    Retourne -1 si aucun étudiant à été trouvé. 
    """
    
    # Parcours des étudiants
    for etu in range(len(matEtu)):
        if len(matEtu[etu]) > 0 and statutsEtu[etu] == False:
            return etu
    return -1

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
       
    # On boucle tant qu'il y a un étudiant non affecté qui n'a pas demandé
    # à tous les parcours
    etu = interne_libre(matEtu, statutsEtu)
    while etu != -1:
        
        # Specialite en tete de la liste de l'etu courant
        speDemandee = matEtu[etu].pop(0)
        if speDemandee not in mariage:
            mariage[speDemandee] = set()
        # La specialite a de la place
        if len(mariage[speDemandee]) < capaciteSpe[speDemandee]:
            # On ajoute l'étudiant
            mariage[speDemandee].add(etu)
            statutsEtu[etu] = True
        # Sinon on regarde si la spécialité ne préfère pas l'etu courant
        # à un etu qu'elle a déjà
        else:
            # Parcours de la liste de préférences de la spécialité du pire
            # au meilleur
            i = len(matSpe[speDemandee])-1
            while i>0:
                etuCur = matSpe[speDemandee][i]
                if etuCur == etu:
                    break
                if etuCur in mariage[speDemandee]:
                    mariage[speDemandee].remove(etuCur)
                    mariage[speDemandee].add(etu)
                    statutsEtu[etuCur] = False
                    statutsEtu[etu] = True
                    break
                i -= 1

        etu = interne_libre(matEtu, statutsEtu)
    
    return mariage

    