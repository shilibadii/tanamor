import json

# Charger le fichier JSON
input_file = 'train_nettoye1111.json'
print("Chargement du fichier JSON...")
with open(input_file, 'r', encoding='utf-8') as file:
    data = json.load(file)
print("Fichier JSON chargé avec succès.")

# Filtrer les lignes vides
cleaned_data = [item for item in data if item.strip() != ""]

# Sauvegarder les données nettoyées dans un nouveau fichier JSON
output_file = 'train_nettoye11112.json'
print(f"Sauvegarde des données nettoyées dans {output_file}...")
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(cleaned_data, file, ensure_ascii=False, indent=4)
print(f"Le nettoyage des données est terminé et le fichier nettoyé a été enregistré sous '{output_file}'")
