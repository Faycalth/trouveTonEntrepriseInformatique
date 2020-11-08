#https://docs.python.org/fr/3/library/csv.html
import csv
nom_fichier_src = "liste_entreprise.csv"
nom_fichier_csv = "liste_entreprise_triees.csv"
liste_commune = ["LYON", "PARIS 8", "VILLEURBANNE", "CRETEIL"]
fieldnames = ['Nom', 'Ville', 'Code Postal', 'Categorie']

#
#Ouverture du fichier
with open(nom_fichier_src, "r") as fichier_src, open(nom_fichier_csv, "w") as fichier_csv:
    writer = csv.DictWriter(fichier_csv, fieldnames=fieldnames, restval="")
    writer.writeheader()
    
    reader = csv.DictReader(fichier_src)
    for row in reader:
        if(row['libelleCommuneEtablissement'] in liste_commune):
            writer.writerow({
                'Nom':row['denominationUniteLegale'], 
                'Ville':row['libelleCommuneEtablissement'], 
                'Code Postal':row['codePostalEtablissement'], 
                'Categorie':row['categorieEntreprise']
            })

"""
    
    
    #Parcours du fichier
    lignes = fichier_src.read()
    i=0

    while i<10:
        print(lignes)
        i = i +1
 """       
    
    
print("Programme terminé")
