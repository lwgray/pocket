from gensim import corpora, models, similarities
from time import time
import numpy as np

corpus_filename = 'larry.mm'
dict_filename   = 'larry.dict'
lda_filename    = 'larry.lda'
lda_params      = {'num_topics': 4, 'passes': 200, 'alpha': 'auto'}

corpus = corpora.MmCorpus(corpus_filename)
dictionary = corpora.Dictionary.load(dict_filename)

print("Running LDA with %s " % lda_params)
lda = models.LdaModel(corpus, id2word=dictionary,
                      num_topics=lda_params['num_topics'],
                      passes=lda_params['passes'],
                      alpha = lda_params['alpha'])

print()
print(lda.show_topics())
lda.save(lda_filename)
print("lda saved in %s " % lda_filename)
