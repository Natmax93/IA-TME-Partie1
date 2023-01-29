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

def specialite_non_pleine(matSpe, capaciteSpe, mariage):
    """
    Fonction qui cherche une spécialité qui n'est pas pleine et qui n'a
    pas demandé à tous les étudiants de sa liste de préférence.
    Retourne -1 si aucune spécialité n'est trouvée.

    Parameters
    ----------
    matSpe : list[list[int]]
        matrice des spécialités.
    capaciteSpe : dict[int:int]
        capacité de chaque spécialité.
    mariage : dict[int:set[int]]
        mariage que l'on considère.

    Returns
    -------
    Le numéro de la spécialité trouvée.
    -1 si aucune spécialité n'est trouvée.

    """
    
    # Parcours des spécialités
    for spe in range(len(matSpe)):
        # La spécialité n'a pas une capacité nulle
        if capaciteSpe[spe] > 0:
            # Le nombre d'étudiant courant dans la spécialité
            if spe in mariage:
                nbEtu = len(mariage[spe])
            else:
                nbEtu = 0
            assert nbEtu <= capaciteSpe[spe]
            # La spécialité n'est pas pleine
            if nbEtu < capaciteSpe[spe]:
                # La spécialité n'a pas demandé à tous les étudiants de sa
                # liste de préférences
                if len(matSpe[spe]) != 0:
                    return spe
    return -1
                
def GaleShapley_CP(fic_etu, fic_spe):
    """
    Retourne un mariage parfait et stable côté spécialité sous forme
    de dictionnaire (une spécialité associée à un ensemble d'étu)
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
    
    # On boucle tant qu'il y a une spécialité non pleine qui n'a pas demandé
    # à tous les étudiants
    spe = specialite_non_pleine(matSpe, capaciteSpe, mariage)
    while spe != -1:
        
        # Etu en tête de la liste de la spécialité courante
        etuDemande = matSpe[spe].pop(0)
        
        # L'étudiant n'a pas déjà été affecté
        if not statutsEtu[etuDemande]:
            if spe not in mariage:
                mariage[spe] = set()
            mariage[spe].add(etuDemande)
            statutsEtu[etuDemande] = True
        else:
            # On récupère la spécialité dans lequel l'étudiant est affecté
            speEtu = -1
            for i in range(len(mariage)):
                if etuDemande in mariage[i]:
                    speEtu = i
                    break
            assert speEtu != -1
            # On regarde si l'étudiant ne préfère pas la spécialité
            # demandée à celle dans lequel il est affecté
            verif = False
            for speCur in matEtu[etuDemande]:
                # L'étudiant préfère la spécialité qui demande à celle dans
                # lequel il est affecté
                if speCur == spe:
                    if spe not in mariage:
                        mariage[spe] = set()
                    mariage[speEtu].remove(etuDemande)
                    mariage[spe].add(etuDemande)
                    verif = True
                    break
                # L'étudiant préfère la spécialité dans lequel il est
                # affecté à celle qui demande
                elif speCur == speEtu :
                    verif = True
                    break
            assert verif
        
        spe = specialite_non_pleine(matSpe, capaciteSpe, mariage)
        
    return mariage
        
        
def unstable_pair(fic_etu, fic_spe, mariage):
    """
    Cherche la liste des paires instables dans un mariage.
    Hypothèse : le mariage est parfait

    Parameters
    ----------
    fic_etu : string
        Première matrice des préférences.
    fic_spe : string
        Deuxième matrice des préférences.
    mariage : dict[int:set[int]]
        Le mariage (affectation) à vérifier.

    Returns
    -------
    La liste des paires instables.

    """
    
    matEtu = lec_pref_etu(fic_etu)
    matSpe = lec_pref_spe(fic_spe)
    listeInstable = []
    
    # On parcourt tous les étudiants
    for etu in range(len(matEtu)):
        # On récupère la spécialité dans lequel il est affecté
        spe = -1
        for i in mariage:
            if etu in mariage[i]:
                spe = i
                break
        assert spe != -1
        # On récupère la liste des spécialités que l'étudiant préfère à
        # celle dans lequel il est affecté
        listePref = []
        for i in matEtu[etu]:
            if i == spe:
                break
            listePref.append(i)
        # Parmi les spécialités que l'étudiant préfère on cherche toutes
        # celles qui aurait préféré l'avoir plutôt qu'un autre étudiant qui
        # est affecté à cette spécialité
        for speCur in listePref:
            assert speCur in mariage
            for etuAff in mariage[speCur]:
                for etuPref in matSpe[speCur]:
                    if etuPref == etu:
                        listeInstable.append((speCur,etu))
                        break
                    elif etuPref == etuAff:
                        break
                    
    return listeInstable