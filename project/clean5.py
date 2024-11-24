import re
import json

def remove_long_words(text, index):
    # Afficher l'index du commentaire en cours de traitement
    print(f"Nettoyage du commentaire {index}...")

    # Découper le texte en mots
    words = text.split()

    # Filtrer les mots qui ont 10 caractères ou moins
    filtered_words = [word for word in words if len(word) <= 12]

    # Rejoindre les mots filtrés pour reformer le texte
    cleaned_text = ' '.join(filtered_words)

    # Afficher le texte avant et après nettoyage pour suivi
    print(f"Avant nettoyage: {text}")
    print(f"Après nettoyage : {cleaned_text}")
    
    return cleaned_text

# Charger le fichier JSON
input_file = 'train2222.json'
print("Chargement du fichier JSON...")
with open(input_file, 'r', encoding='utf-8') as file:
    data = json.load(file)
print("Fichier JSON chargé avec succès.")

# Nettoyer les textes dans le fichier JSON
cleaned_data = []
for index, comment in enumerate(data):
    cleaned_text = remove_long_words(comment, index)
    cleaned_data.append(cleaned_text)

# Sauvegarder les données nettoyées dans un nouveau fichier JSON
output_file = 'train22222.json'
print(f"Sauvegarde des données nettoyées dans {output_file}...")
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(cleaned_data, file, ensure_ascii=False, indent=4)
print(f"Le nettoyage des données est terminé et le fichier nettoyé a été enregistré sous '{output_file}'")
