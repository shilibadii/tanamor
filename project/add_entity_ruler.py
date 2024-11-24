import spacy
import json
import os



directory = "toxic_words"  # Spécifiez le répertoire contenant vos fichiers JSON
nlp = spacy.load("toxic_model")
ruler = nlp.add_pipe("entity_ruler")


for filename in os.listdir(directory):
    if filename.endswith(".json"):
        label = os.path.splitext(filename)[0]  # Retirez l'extension ".json" du nom du fichier
        with open(os.path.join(directory, filename), "r", encoding="utf-8") as f:
            data = json.load(f)
        patterns = []
        for item in data:
            pattern = {
                "label": label,
                "pattern": item
            }
            patterns.append(pattern)
        ruler.add_patterns(patterns)


nlp.to_disk("toxic_model")
