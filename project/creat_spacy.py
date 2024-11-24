""" import spacy

nlp=spacy.blank("en")

nlp.to_disk("toxic_model1") """


import spacy

nlp=spacy.load("toxic_model1")
nlp.add_pipe("ner")

nlp.to_disk("toxic_model1")