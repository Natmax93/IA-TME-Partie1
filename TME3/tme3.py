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
        i += 1
    return False    
    
    
def pl_generator_equity_k(fichierEtu, fichierSpe, nom_fichier, k):
    """
    Fonction qui génère un PL permettant de savoir s’il existe une
    affectation où tout étudiant a un de ses k premiers choix
    """
    
    fichier = open(nom_fichier, "w")
    
    matEtu = gs.lec_pref_etu(fichierEtu)
    matSpe = gs.lec_pref_spe(fichierSpe)
    
    dicoSpe = dict()
    dicoEtu = dict()
    variables = set()
    capacites = gs.get_capacite(fichierSpe)
    
    fichier.write("Maximize\n")
    fichier.write("obj: ")
    
    for etu in range(len(matEtu)):
        # On parcourt les spécialités qui sont dans les k premiers
        # choix de l'étudiant courant
        for j in range(k):
            # On récupère la liste de préférence de la spécialité
            # courante
            spe = matEtu[etu][j]
            listeSpe = matSpe[spe]
            if estPref(etu, listeSpe, k):
                # On crée une nouvelle variable pour le PL qui correspond au
                # couple etu-spe courant
                variables.add("x" + str(etu) + "_" + str(spe))
                # dictionnaire stockant les etudiants à leur spe dans
                dicoSpe[spe].append(etu)
                dicoEtu[etu].append(spe)
                
    # Cas où il n'y a pas de variables
    if not variables:
        print("Aucune possible pour ce k")
        return
                
    # Ecriture du fichier
    
    # Fonction objectif
    fichier.write("Maximize\n")
    fichier.write("obj: ")
    fichier.write(variables[0])
    
    for var in range(1, len(variables)):
        fichier.write(" + " + variables[var])
        
    # Contraintes
    
    fichier.write("Subject To\n")
    
    # Contraintes sur la capacité des hôpitaux
    i = 1
    for spe in dicoSpe:
        if dicoSpe[spe]:
            fichier.write("c" + str(i) + ": ")
            i += 1
            fichier.write("x" + str(dicoSpe[spe][0]) + "_" + str(spe) )
            for j in range(1, len(dicoSpe[spe])):
                fichier.write(" + " + "x" + str(dicoSpe[spe][j]) + "_" + str(spe))
                
        fichier.write(" <= " + capacites[spe] + "\n")
    
    # Contraintes pour l'unicité
    for etu in range(len(dicoEtu)):
        if dicoEtu[etu]: 
            fichier.write("c" + str(i) + ": ")
            i += 1
            fichier.write("x" + str(dicoEtu[etu][0]) + "_" + str(spe) )
            for j in range(1, len(dicoEtu[etu])):
                fichier.write(" + " + "x" + str(dicoEtu[etu][j]) + "_" + str(spe))
        fichier.write(" <= 1\n")
    
    fichier.write("Binary\n")
    for var in variables:
        fichier.write(var + " ")
    fichier.write("\nEnd")
    
    
    fichier.close()
    
pl_generator_equity_k("PrefEtu.txt", "PrefSpe.txt", "equity.pl", 2)