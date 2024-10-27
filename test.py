# test_packages.py
import spacy
import tensorflow as tf

print("spaCy version:", spacy.__version__)
print("TensorFlow version:", tf.__version__)

nlp = spacy.load("en_core_web_sm")
doc = nlp("Hello, world!")
for token in doc:
    print(token.text, token.pos_)

hello = tf.constant('Hello, TensorFlow!')
tf.print(hello)