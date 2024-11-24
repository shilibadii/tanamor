import re
import json

# Compile les expressions régulières une seule fois pour une meilleure performance
patterns = {
    "http_width": re.compile(r'[^.!?]*\b(?:http[s]?://\S+|width:)\b[^.!?]*[.!?]'),  # Supprime toute phrase contenant http://, https:// ou width:
    "date_format_1": re.compile(r'\b\d{1,2}[\s/-]?[a-z]+[\s/-]?\d{2,4}\b'),  # Dates comme "22 August 2009" ou "22/08/2009"
    "date_format_2": re.compile(r'\b\d{4}[-/]\d{2}[-/]\d{2}\b'),  # Dates comme "2009-08-22"
    "date_format_3": re.compile(r'\b\d{1,2} [a-z]+\b'),  # Dates comme "9 September"
    "date_format_4": re.compile(r'\b[a-z]+ \d{4}\b'),  # Dates comme "September 2005"
    "date_format_5": re.compile(r'\b\d{4} utc\b'),  # Dates comme "2007 UTC"
    "html_tags": re.compile(r'<.*?>|\[.*?\]'),  # Balises HTML et Markdown
    "special_chars": re.compile(r'[^a-z0-9\s]'),  # Caractères spéciaux
    "multi_spaces": re.compile(r'\s+')  # Espaces multiples
}

def clean_text(text):
    # Conversion en minuscules
    text = text.lower()
    
    # Suppression des phrases avec liens HTTP/HTTPS ou 'width:'
    text = patterns["http_width"].sub('', text)
    
    # Suppression des différents formats de dates
    for pattern in ["date_format_1", "date_format_2", "date_format_3", "date_format_4", "date_format_5"]:
        text = patterns[pattern].sub('', text)

    # Suppression des balises HTML/Markdown
    text = patterns["html_tags"].sub('', text)
    
    # Suppression des caractères spéciaux (garde les lettres et chiffres)
    text = patterns["special_chars"].sub('', text)
    
    # Suppression des séquences de 4 chiffres ou plus (ex: années)
    text = re.sub(r'\b\d{4,}\b', '', text)
    
    # Normalisation des espaces multiples en un seul espace
    text = patterns["multi_spaces"].sub(' ', text).strip()
    
    return text

# Charger et nettoyer le fichier JSON en une seule étape
with open('train2.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    cleaned_data = [clean_text(comment) for comment in data]

# Sauvegarder les données nettoyées dans un nouveau fichier JSON
with open('train_nettoye2.json', 'w', encoding='utf-8') as file:
    json.dump(cleaned_data, file, ensure_ascii=False, indent=4)

print("Le nettoyage des données est terminé et le fichier nettoyé a été enregistré sous 'train_nettoye111.json'")
