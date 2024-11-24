import json
import re

# Fonction pour nettoyer le texte (réduire les espaces multiples à un seul espace)
def clean_text(text):
    # Réduire les espaces multiples à un seul espace et supprimer les espaces en début et fin
    text = re.sub(r'\s+', ' ', text).strip()

    # Liste des caractères spéciaux à supprimer
    special_chars = r'áÁćĆéÉíÍĺĺńŃóÓŕŔśŚúÚýÝźŹàÀèÈìÌòÒùÙâÂĉĈêÊĝĜĥĤîÎĵĴôÔŝŜûÛŵŴŷŶäÄëËïÏöÖüÜÿÿßãÃẽẼĩĨñÑõÕũŨỹỹçÇģĢķĶļĻņŅŗŖşŞţŢđĐůŮǎǒřŘšŠťŤǔŽżāēīōūȳǣǖǘǚǜăăĕĕğğĭĭŏŏŭŭċċėėġġiıżżąąęęįįǫǫųųḍḍḥḥḷḷḹḹṃṃṇṇṛṛṝṝṣṣṭṭłłőőűűŀŀħħððþþœœææøøååəə½⅓⅔¼¾⅛⅜⅝⅞ƒℳm²m³'

    # Supprimer les caractères spéciaux mentionnés
    text = ''.join(c for c in text if c not in special_chars)

    return text

# Charger le fichier JSON d'entrée
input_file = 'train222.json'  # Remplacez par le nom de votre fichier JSON d'entrée
output_file = 'train2222.json'  # Remplacez par le nom de votre fichier JSON de sortie

print("Chargement du fichier JSON...")
with open(input_file, 'r', encoding='utf-8') as file:
    data = json.load(file)
print("Fichier JSON chargé avec succès.")

# Nettoyer les textes dans le fichier JSON
cleaned_data = [clean_text(text) for text in data]

# Sauvegarder les données nettoyées dans un nouveau fichier JSON
print(f"Sauvegarde des données nettoyées dans {output_file}...")
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(cleaned_data, file, ensure_ascii=False, indent=4)

print(f"Le fichier nettoyé a été enregistré sous '{output_file}'")
