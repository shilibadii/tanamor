import csv
import json

# Initialiser une liste pour stocker les valeurs de la deuxième colonne
comments = []

# Ouvrir le fichier CSV et extraire la deuxième colonne
with open('jigsaw-toxic-comment-train-processed-seqlen128.csv', mode='r', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)  # Ignorer l'en-tête
    for row in reader:
        # Assurez-vous que la ligne contient au moins deux colonnes
        if len(row) > 1:
            # Extraire la deuxième colonne et l'ajouter à la liste
            comments.append(row[1])

# Écrire la liste dans un fichier JSON
with open('train2.json', mode='w', encoding='utf-8') as json_file:
    json.dump(comments, json_file, ensure_ascii=False, indent=4)

print("Extraction réussie ! Les données ont été enregistrées dans 'extracted_comments.json'")
