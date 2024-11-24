import spacy

# Load the best-performing model
import os
nlp = spacy.load(os.path.join("C:/Users/Charanko/Desktop/badiaa_project/output1", "model-best"))

# Test the model
doc = nlp("John is going to kill himself")

for ent in doc.ents:
    print(f"Entity: {ent.text}, Label: {ent.label_}")
