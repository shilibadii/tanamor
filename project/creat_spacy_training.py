from spacy.tokens import DocBin
import spacy
import json
from tqdm import tqdm


def load_data(file):
    with open (file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return (data)

camp_train = load_data("toxic_train_data.json")
print (camp_train[0])

camp_valid = load_data("toxic_valid_data.json")

nlp = spacy.blank("en")
def create_training(TRAIN_DATA):
    db = DocBin()
    for text, annot in tqdm(TRAIN_DATA):
        doc = nlp.make_doc(text)
        ents = []
        for start, end, label in annot["entities"]:
            span = doc.char_span(start, end, label=label, alignment_mode="contract")
            if span is None:
                print ("Skipping entity")
            else:
                ents.append(span)
        doc.ents = ents
        db.add(doc)
    return (db)

camp_train = create_training(camp_train)
camp_train.to_disk("describ_train.spacy")

camp_valid = create_training(camp_valid)
camp_valid.to_disk("describ_valid.spacy")