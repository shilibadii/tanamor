import json
from sklearn.model_selection import train_test_split

# Chargez les descriptions depuis le fichier JSON
with open("train222222.json", "r", encoding="utf-8") as f:
    descriptions = json.load(f)

# Divisez les données en ensembles d'entraînement (70%) et de validation (30%)
train_data, valid_data = train_test_split(descriptions, test_size=0.3, random_state=42)

# Enregistrez les ensembles d'entraînement et de validation dans des fichiers JSON distincts
with open("training.json", "w", encoding="utf-8") as train_file:
    json.dump(train_data, train_file, ensure_ascii=False, indent=4)

with open("validation.json", "w", encoding="utf-8") as valid_file:
    json.dump(valid_data, valid_file, ensure_ascii=False, indent=4)
