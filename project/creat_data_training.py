import spacy
import json

# Charger le modèle SpaCy
nlp = spacy.load("toxic_model")

def test_model(text):
    doc = nlp(text)
    entities = []
    for ent in doc.ents:
        entity_info = (ent.start_char, ent.end_char, ent.label_)
        entities.append(entity_info)
    return entities

# Charger les données à partir de votre fichier JSON "description_carrfour.json"
with open("validation.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Créer une liste pour stocker les résultats
TRAIN_DATA = []

# Parcourir chaque phrase dans les données
for text in data:
    entities_found = test_model(text)
    
    # Créer un tuple pour stocker les résultats de cette phrase
    phrase_result = (text, {"entities": entities_found})
    TRAIN_DATA.append(phrase_result)

# Enregistrer les résultats dans un fichier JSON
with open("toxic_valid_data.json", "w", encoding="utf-8") as output_file:
    json.dump(TRAIN_DATA, output_file, indent=4, ensure_ascii=False)

print("Résultats sauvegardés dans 'describtion_training_data.json'")