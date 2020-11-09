#https://docs.python.org/fr/3/library/csv.html
import csv, time

nom_fichier_src = 'liste_entreprise.csv'
nom_fichier_csv = 'liste_entreprise_trouvées.csv'
liste_commune = ['LYON 1ER', 'LYON 2EME', 'LYON 6EME', 'LYON 7EME', 'LYON 8EME', 'VILLEURBANNE']
fieldnames = ['Categorie', 'Nom', 'Code Postal', 'Ville', 'Activite principale']
#dict_act = dict()
dict_act = {'61.10Z': 'Telecommunications filaires', '61.20Z': 'Telecommunications sans fil', '61.30Z': 'Télécommunications par satellite','61.90Z': 'Autres activités de télécommunication','62.01Z': 'Programmation informatique','62.02A': 'Conseil en systèmes et logiciels informatiques','62.02B': 'Tierce maintenance de systèmes et d applications informatiques','62.03Z': 'Gestion d installations informatiques','62.09Z': 'Autres activités informatiques','63.11Z': 'Traitement de données, hébergement et activités connexes','63.12Z': 'Portails Internet'}
count = 0

#Ouverture du fichier
with open(nom_fichier_src, "r") as fichier_src, open(nom_fichier_csv, "w", newline="") as fichier_csv:
    writer = csv.DictWriter(fichier_csv, fieldnames=fieldnames, restval="")
    writer.writeheader()
    
    reader = csv.DictReader(fichier_src)
    for row in reader:
        if(row['libelleCommuneEtablissement'] in liste_commune and row['categorieJuridiqueUniteLegale']!="1000"):
            if(row['activitePrincipaleUniteLegale'] in dict_act):
                writer.writerow({
                    'Categorie':row['categorieEntreprise'],
                    'Nom':row['denominationUniteLegale']+" "+row['sigleUniteLegale'],
                    'Ville':row['libelleCommuneEtablissement'], 
                    'Code Postal':row['codePostalEtablissement'],
                    'Activite principale': dict_act[row['activitePrincipaleUniteLegale']]
                })
                count = count + 1
    
print("Nombre d'entreprises trouvées : ", count)
print("Temps d'éxecution :", time.perf_counter(), "secondes.")
