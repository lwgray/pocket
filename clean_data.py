# Author: Lawrence Gray <lwgray at gmail.com>
# License:
# Python 3.5

'''
Add Doc String
'''

import pickle
import re
from nltk.corpus import stopwords
from gensim import corpora
from gensim.models import Phrases
from nltk.stem.porter import PorterStemmer
from progress.bar import Bar

p_stemmer = PorterStemmer()


def load(filename, datatype):
    '''
    1. load in pickled data
    2. Extract info based on datatype parameter:
        'title' --> Use article title for data
        'excerpt' --> Use article excerpt for data
        'content' --> Use article text for data
    '''
    print "Loading Data"
    data = []
    with open(filename, 'rb') as dataset:
        original_data = pickle.load(dataset)
    # Grab item_ids
    item_id = [value['item_id'] for item in original_data
               for key, value in item.iteritems()]
    # If you want to use just the title
    if datatype == 'title':
        data = [value['resolved_title'] for info in original_data
                for key, value in info.items()]
    # If you would like to use both the title and article excerpt
    if datatype == 'excerpt':
        data = [" ".join([value['resolved_title'], value['excerpt']])
                for info in original_data for key, value in info.items()]
    # If you would like to use he article content
    if datatype == 'content':
        with open('web_data.p', 'r') as web:
            data = pickle.load(web)
    return (data, item_id)


def preprocess(data, datatype):
    ''' add docstring '''
    # clean up data
    # words = [clean(x) for x in data[0]]
    words = []
    bar = Bar('Cleaning Article --> ', max=len(data[0]))
    for index, x in enumerate(data[0]):
        w = clean(x)
        bar.next()
        words.append(w)
    bar.finish()
    # create bigrams
    bigram_transformer = Phrases(words)
    words = bigram_transformer[words]
    # Build a dictionary where each title and each word has its owdn id
    if datatype == 'test':
        # words = [x for x in words]
        return words
    dictionary = corpora.Dictionary(words)
    dictionary.filter_extremes(no_below=10, no_above=0.50)
    dictionary.compactify()
    # and save the dictionary for future use
    dictionary.save('larry.dict')
    # Build the corpus: vectors with occurence of each word for each title
    # convert tokenized titles into vectors
    corpus = [dictionary.doc2bow(w) for w in words]
    # and save in Market Matrix format
    corpora.MmCorpus.serialize('larry.mm', corpus)


def clean(data):
    '''
    Clean up data by removing stop words,
    numbers, punctuations, carriage returns,spaces,
    words <= 2 characters, and converting words to lowercase
    '''
    words = re.sub("[^a-zA-Z]", " ", data)
    words = words.lower().split()
    words = [w for w in words if len(w) > 1]
    # remove "English" stop words
    stop_words = stopwords.words('english')
    words = [w for w in words if w not in stop_words]
    # stem words
    # words = [p_stemmer.stem(w) for w in words]
    return words

if __name__ == '__main__':
    DATA = load('training_data.p', 'excerpt')
    print 'Loaded Data, Now Processing'
    preprocess(DATA, 'title')
