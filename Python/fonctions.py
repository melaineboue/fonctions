import csv


def enregistrer(contents):

    with open('content.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=';', lineterminator='\n', quoting=csv.QUOTE_ALL )
        #Titres
        content = []
        content.append("Code")
        content.append("Niveau hiérarchique")
        content.append("Type hiérarchique")
        content.append("Libellé")
        content.append("Catégorie")
        content.append("Statut")
        content.append("Genre Adjudication")
        writer.writerow(content)

        compteur_generale = 0

        #print("Progression")
        for content in contents:
            #print("Enregistrement "+str(compteur_generale))
            compteur_generale += 1
            writer.writerow(content)




def getFin(valeurs):
    for index in range(0, min(len(valeurs), 6)):

        if valeurs[index].strip() == "":
            return index
    return 6


def getContent(files):
    result = []
    for file in files:
        with open(file + ".csv", newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                #print(row)
                separator = ""
                ligne = separator.join(row)
                print(ligne)
                #break
                tab_texte = ligne.split(";")
                tab_texte_finale = tab_texte[:getFin(tab_texte)]
                #print(tab_texte_finale)
                result.append(tab_texte_finale)
    return result


def extraction(tabLines):
    decoupageCode = [0, 1, 2, 4, 5, 6];
    valeur_precedente = ["Code", "", "", "", "", ""]
    f_statut = "V"
    compteur_niveau_hierarchie = [0, 0, 0, 0, 0, 0]  # Le premier 0 ne sert à rien

    f_code = ""
    f_niveau_hierarchie = ""
    f_type_hierarchie = ""
    f_libelle = ""
    f_categorie = ""
    # f_statut = ""
    f_genre = ""

    result = []

    for line in tabLines:

        codeOrigine = line[0]
        for i in range(1, len(line)):

            # Recuperation des valeurs de chaque case
            if valeur_precedente[i] != line[i]:
                compteur_niveau_hierarchie[i] += 1
                # Je dois réinitialiser les numéros qui viennent après
                for k in range(i + 1, 6):
                    compteur_niveau_hierarchie[k] = 0
            else:
                continue



            f_code = codeOrigine[:decoupageCode[i]]
            f_libelle = line[i]
            f_niveau_hierarchie = "1"
            if i == len(line) - 1:  # c'est le dernier de la liste donc un article
                f_code = codeOrigine[:decoupageCode[i]]
                f_type_hierarchie = "A"
                f_categorie = "F"
                # f_statut = f_statut
                f_genre = "PA"
            else:
                f_type_hierarchie = "F"
                f_categorie = ""
                # f_statut =
                f_genre = ""

            f_niveau_hierarchie = str(compteur_niveau_hierarchie[1])
            for j in range(2,i + 1):  # Pour remplir le niveau hiérarchie, on commence par 2 car j'ai déjà pris le 1 plus haut
                if compteur_niveau_hierarchie[j] > 0:
                    f_niveau_hierarchie = f_niveau_hierarchie + "." + str(compteur_niveau_hierarchie[j])

            content = []
            content.append(f_code)
            content.append(f_niveau_hierarchie)
            content.append(f_type_hierarchie)
            content.append(f_libelle)
            content.append(f_categorie)
            content.append(f_statut)
            content.append(f_genre)
            result.append(content)

            valeur_precedente[i] = line[i]
    return result


def getErreurPosition(files):
    print("debut")
    compteur =0
    for file in files:
        ligne_number = 0
        compteur += 1
        with open(file + ".csv", newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                #compteur += 1
                ligne_number += 1
                #print(row)
                separator = ""
                ligne = separator.join(row)
                #print(ligne)
                #break
                tab_texte = ligne.split(";")
                #print(tab_texte[0])
                if len(tab_texte[0].strip()) < 8:

                    print(file+".csv (ligne "+str(ligne_number)+" ) : "+str(tab_texte[0]))
    print(compteur)



files = [
    "f6_Dispositif_médicaux",
    "f6_Hoteller_Restaurant_Presta_Generale",
    "f6_Informatique",
    "f6_Medicaments",
    "f5_Biomedical",
    "f5_Laboratoire_Biologie",
    "f5_Transports",
    "f5_Travaux_Infrast_Energie"
]
#
# files = [
#     "f5_Laboratoire Biologie"
# ]

tabContent = getContent(files)
res = extraction(tabContent)
enregistrer(res)
#print(len(res))
#for el in res:
#   print(el)

#getErreurPosition(files)
