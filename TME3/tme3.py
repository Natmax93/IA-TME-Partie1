import gs

def estPref(etu, listeSpe, k):
    """
    Fonction qui retourne true si l'étudiant est dans les k premiers
    choix de la liste de préférence listeSpe et false sinon.
    """
    
    i = 0
    while i<len(listeSpe) and i<k:
        if listeSpe[i] == etu:
            return True
    return False
        
    
    
def pl_generator_equity_k(fichierEtu, fichierSpe, nom_fichier, k):
    """
    Fonction qui génère un PL permettant de savoir s’il existe une
    affectation où tout étudiant a un de ses k premiers choix
    """
    
    fichier = open(nom_fichier, "w")
    
    matEtu = gs.lec_pref_etu(fichierEtu)
    matSpe = gs.lec_pref_spe(fichierSpe)
    
    for etu in range(len(matEtu)):
        # On parcourt les spécialités qui sont dans les k premiers
        # choix de l'étudiant courant
        for j in range(k):
            # On récupère la liste de préférence de la spécialité
            # courante
            spe = matEtu[etu][j]
            listeSpe = matSpe[spe]
            if not estPref(etu, listeSpe, k):
                return False
    
    fichier.close()