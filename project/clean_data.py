import re
import json

def clean_text(text):
    # Suppression des balises HTML/Markdown
    text = re.sub(r'<.*?>', '', text)  # Supprime les balises HTML
    text = re.sub(r'\[.*?\]', '', text)  # Supprime les balises de type [Lien]

    # Suppression des caractères spéciaux (conserve les lettres et les chiffres)
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    # Normalisation des espaces multiples en un seul espace
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

# Charger le fichier JSON
with open('train.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Nettoyer les textes dans le fichier JSON
cleaned_data = [clean_text(comment) for comment in data]

# Sauvegarder les données nettoyées dans un nouveau fichier JSON
with open('train_nettoye.json', 'w', encoding='utf-8') as file:
    json.dump(cleaned_data, file, ensure_ascii=False, indent=4)

print("Le nettoyage des données est terminé et le fichier nettoyé a été enregistré sous 'votre_fichier_nettoye.json'")
