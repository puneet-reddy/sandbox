#!/usr/bin/env python
# emotion_classifier.py

from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string

from textblob.classifiers import NaiveBayesClassifier
import pandas as pd

class EmotionClassifier:
    '''
    Generates a probability score for each emotion
    Trained on the ISEAR dataset
    '''
    def __init__(self):
        self.df = pd.read_csv('emotion_data.csv')
        self.stop = set(stopwords.words('english'))
        self.exclude = set(string.punctuation)
        self.lemma = WordNetLemmatizer()
        self.negative = self._load_negative_words()
        self.em_list = []
        self.text_list = []
        self.train = []

    def clean(self, doc):
        '''
        Remove stop words, punctuations and lemmatizes
        '''
        stop_free = ' '.join([
            e for e in doc.lower().split() 
            if i not in self.stop 
            if i not in self.negative])
        punc_free = ''.join([e for e in stop_free if e not in self.exclude])
        norm = ' '.join([self.lemma.lemmatize(e) for e in punc_free.split()])
        return norm

    def _load_negative_words(self, nword_file='negative_words.txt'):
        with open(nword_file, 'r') as f:
            lines = f.readlines()
        words = [e.strip('\n') for e in lines]
        return words

    def train_model(self):
        training_data = [list(e) for e in self.df.itertuples(index=False)]
        nb = NaiveBayesClassifier(training_data)
        self.model = nb

    def classify(self, text):
        return self.model.classify(text)


if __name__ == '__main__':
    pass