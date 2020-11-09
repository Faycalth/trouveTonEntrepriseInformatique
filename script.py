#https://docs.python.org/fr/3/library/csv.html
import csv,os

#Variables
fieldnames = ['Categorie', 'Nom', 'Code Postal', 'Ville', 'Activite principale']
#création dictionnaire clé valeur
dict_act = {'61.10Z': 'Telecommunications filaires', '61.20Z': 'Telecommunications sans fil', '61.30Z': 'Télécommunications par satellite','61.90Z': 'Autres activités de télécommunication','62.01Z': 'Programmation informatique','62.02A': 'Conseil en systèmes et logiciels informatiques','62.02B': 'Tierce maintenance de systèmes et d applications informatiques','62.03Z': 'Gestion d installations informatiques','62.09Z': 'Autres activités informatiques','63.11Z': 'Traitement de données, hébergement et activités connexes','63.12Z': 'Portails Internet'}
key_list = list(dict_act.keys())
value_list = list(dict_act.values())

def get_nom_fichier():
    nom_fichier = str(input("Entrez le nom du fichier à parcourir (avec l'extension csv): "))
    return nom_fichier


def get_ville():
    liste_ville = []
    i = True
    while(i):
        inp_ville = str(input("Entrez les villes des entreprises (Ecrivez 'stop' pour arrêter): "))
        if(inp_ville!="stop"):
            liste_ville.append(inp_ville.upper())
        else:  
            i=False
    return liste_ville

def get_activite():
    i = True
    liste_activite = []

    while(i):
        affichage_activite()
        inp_activite = input("\nEntrez le numero de l'activite de l'entreprise (Ecrivez 'stop' pour arrêter): ")
        if(inp_activite!="stop"):
            liste_activite.append(key_list.pop(int(inp_activite)))
            value_list.pop(int(inp_activite))    
        else:  
            i=False
    
    return liste_activite

def affichage_activite():
    nb = 0
    for value in value_list:
        print(nb,":",value)
        nb = nb + 1

def recherche(nom_fichier_src, liste_ville, liste_activite):
    #variables
    nom_fichier_sortie = "etablissementsInformatique.csv"
    count = 0

    #Algorithme de recherche
    with open(nom_fichier_src, "r") as fichier_src, open(nom_fichier_sortie, "w", newline="") as fichier_sortie:  #Ouverture des fichiers
        writer = csv.DictWriter(fichier_sortie, fieldnames=fieldnames, restval="")
        writer.writeheader()
        
        reader = csv.DictReader(fichier_src)
        for row in reader:
            if(row['libelleCommuneEtablissement'] in liste_ville and row['categorieJuridiqueUniteLegale']!="1000"):
                if(row['activitePrincipaleUniteLegale'] in liste_activite):
                    writer.writerow({
                        'Categorie':row['categorieEntreprise'],
                        'Nom':row['denominationUniteLegale']+" "+row['sigleUniteLegale'],
                        'Ville':row['libelleCommuneEtablissement'], 
                        'Code Postal':row['codePostalEtablissement'],
                        'Activite principale': dict_act[row['activitePrincipaleUniteLegale']]
                    })
                    count = count + 1
    print("\nNombre d'entreprises trouvées : ", count)


#Programme
recherche(get_nom_fichier(),get_ville(),get_activite())
print("Votre fichier se trouve dans : ", os.getcwd())

