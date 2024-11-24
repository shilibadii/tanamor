import json
import re

def clean_text(text):
    # Supprimer les URLs (mots commençant par http)
    text = re.sub(r'http\S+', '', text)

    # Supprimer les retours à la ligne et autres caractères inutiles
    text = re.sub(r'\n+', ' ', text)

    # Supprimer les citations inutiles
    text = re.sub(r'"', '', text)

    # Supprimer les espaces multiples (réduire à un seul espace)
    text = re.sub(r'\s+', ' ', text)

    # Supprimer les caractères spéciaux (exemple: virgules, points d'exclamation, parenthèses, etc.)
    text = re.sub(r'[^\w\s]', '', text)

    # Supprimer "UTC" dans le texte
    text = re.sub(r'\butc\b', '', text)

    # Supprimer les mois de l'année en anglais (January, February, etc.)
    months = r'(january|february|march|april|may|june|july|august|september|october|november|december)'
    text = re.sub(r'\b' + months + r'\b', '', text, flags=re.IGNORECASE)

    # Supprimer les nombres avec plus de 4 chiffres
    text = re.sub(r'\b\d{2,}\b', '', text)

    return text

# Charger le fichier JSON
input_file = 'train22.json'  # Remplacez par le nom de votre fichier JSON d'entrée
output_file = 'train222.json'  # Remplacez par le nom de votre fichier JSON de sortie

print("Chargement du fichier JSON...")
with open(input_file, 'r', encoding='utf-8') as file:
    data = json.load(file)
print("Fichier JSON chargé avec succès.")

# Nettoyer les textes dans le fichier JSON
cleaned_data = []
for index, comment in enumerate(data):
    cleaned_text = clean_text(comment)
    cleaned_data.append(cleaned_text)

# Sauvegarder les données nettoyées dans un nouveau fichier JSON
print(f"Sauvegarde des données nettoyées dans {output_file}...")
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(cleaned_data, file, ensure_ascii=False, indent=4)

print(f"Le nettoyage des données est terminé et le fichier nettoyé a été enregistré sous '{output_file}'")
