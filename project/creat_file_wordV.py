import spacy
import json
from gensim.models.word2vec import Word2Vec
from gensim.models.keyedvectors import KeyedVectors
import multiprocessing


def training(model_name):
    with open("train222222.json", "r", encoding="utf-8") as f:
        texts = json.load(f)

    sentences = texts  

    cores = multiprocessing.cpu_count()
    w2v_model = Word2Vec(min_count=1,
                        window=2,
                        vector_size=500,  
                        sample=6e-5,
                        alpha=0.03,
                        min_alpha=0.0007,
                        negative=20,
                        workers=cores-1)
    w2v_model.build_vocab(sentences)  
    w2v_model.train(sentences, total_examples=w2v_model.corpus_count, epochs=100)
    w2v_model.save(f"{model_name}.model")
    w2v_model.wv.save_word2vec_format(f"{model_name}.txt")

training("toxicc_model")
