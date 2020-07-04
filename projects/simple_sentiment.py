#!/usr/bin/env python
# simple_sentiment.py

import re
import csv
from textblob import TextBlob

class SimpleSentiment(object):
    '''
    The most generic possible sentiment analysis
    '''
    def __init__(self):
        '''Just holds config values (for now)'''
        self.p_thresh = 0.1
        self.n_thresh = -0.1
        self.data = []
        self.output = []

    def load_data(self, filename):
        '''
        Expects the input file to have one sentense per line.
        '''
        with open(filename, 'r') as f:
            lines = f.readlines()
        print('Loaded {} lines'.format(len(lines)))
        self.data = lines

    def clean_line(self, line):
        '''
        Get rid of symbols, extra spaces, etc. using regex magic
        '''
        re_magic = "(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"
        return ' '.join(re.sub(re_magic, " ", line).split())

    def get_sentiment(self, line):
        '''
        Classifies a line as positive, negative or neutral
        '''
        polarity = self.get_polarity(line)
        if polarity > self.p_thresh:
            return 'positive'
        elif polarity < self.n_thresh:
            return 'negative'
        else:
            return 'neutral'
    
    def get_polarity(self, line):
        '''
        Just applies TextBlob's sentiment method and returns the polarity
        '''
        res = TextBlob(self.clean_line(line))
        return res.sentiment.polarity

    def process(self):
        '''
        Generates polarities and sentiment classifications for the input data
        '''
        self.output = []
        for line in self.data:
            polarity = self.get_polarity(line)
            sentiment = self.get_sentiment(line)
            self.output.append((line, polarity, sentiment))

    def to_csv(self, filename, delimiter=',', quotechar='"'):
        '''
        Writes the processed data to the CSV specified
        '''
        with open(filename, 'wb') as csvfile:
            writer = csv.writer(
                csvfile, 
                delimiter=delimiter, 
                quotechar=quotechar, 
                quoting=csv.QUOTE_MINIMAL)
            writer.writerows(self.output)
        print("Wrote {} lines to {}".format(len(self.output), filename))

if __name__ == '__main__':
    ss = SimpleSentiment()
    ss.load_data('netflix.txt')
    ss.process()
    ss.to_csv('netflix_sentiment.txt')