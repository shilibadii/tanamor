import re
import json

def clean_text(text, index):
    # Afficher l'index du commentaire en cours de traitement
    print(f"Nettoyage du commentaire {index}...")

    # Conversion en minuscules pour normaliser les comparaisons
    text = text.lower()
    
    # Découper le texte en phrases en utilisant les ponctuations comme délimiteurs
    sentences = re.split(r'(?<=[.!?])\s+', text)
    cleaned_sentences = []

    # Parcourir chaque phrase et la conserver uniquement si elle ne contient pas "width100", "width", ou un mot contenant "http"
    for sentence in sentences:
        if "width100" not in sentence and "width" not in sentence and not re.search(r'\b\w*http\w*\b', sentence):
            cleaned_sentences.append(sentence)
    
    # Joindre les phrases nettoyées en une seule chaîne de texte
    cleaned_text = ' '.join(cleaned_sentences).strip()

    # Afficher le texte avant et après nettoyage pour suivi
    print(f"Avant nettoyage: {text}")
    print(f"Après nettoyage : {cleaned_text}")
    
    return cleaned_text

# Charger le fichier JSON
input_file = 'train2.json'
print("Chargement du fichier JSON...")
with open(input_file, 'r', encoding='utf-8') as file:
    data = json.load(file)
print("Fichier JSON chargé avec succès.")

# Nettoyer les textes dans le fichier JSON
cleaned_data = []
for index, comment in enumerate(data):
    cleaned_text = clean_text(comment, index)
    cleaned_data.append(cleaned_text)

# Sauvegarder les données nettoyées dans un nouveau fichier JSON
output_file = 'train22.json'
print(f"Sauvegarde des données nettoyées dans {output_file}...")
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(cleaned_data, file, ensure_ascii=False, indent=4)
print(f"Le nettoyage des données est terminé et le fichier nettoyé a été enregistré sous '{output_file}'")
