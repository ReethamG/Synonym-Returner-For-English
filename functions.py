import nltk
from nltk.corpus import wordnet

def removesPunctuation(test_str):
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    for ele in test_str:
        if ele in punc:
            test_str = test_str.replace(ele, "")

    return test_str

def getSynonymsFromInput():
    inputFromUser = input("What words do you need synonyms for?\n")
    inputFromUser = str(removesPunctuation(inputFromUser))

    synonyms = []
    
    for word in inputFromUser.split(" "):
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                synonyms.append(lemma.name())
        print(word + ":" , synonyms , "\n")
        synonyms.clear()    