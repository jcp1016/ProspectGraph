import sys
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer

def get_synonyms(word):
    syns = []
    for synset in wn.synsets(word):
        for lemma in synset.lemmas():
            syns.append(lemma.name())
    return(syns)
