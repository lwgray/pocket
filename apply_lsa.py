from gensim import corpora, models, similarities
from time import time
import numpy as np

corpus_filename = 'larry.mm'
dict_filename   = 'larry.dict'
lsa_filename    = 'larry.lsa'
lsa_params      = {'num_topics': 9, 'passes': 200, 'alpha': 'auto'}

corpus = corpora.MmCorpus(corpus_filename)
dictionary = corpora.Dictionary.load(dict_filename)

print("Running LSA with %s " % lsa_params)
lsa = models.LsiModel(corpus, id2word=dictionary,
                      num_topics=lsa_params['num_topics'])

print()
print(lsa.show_topics())
lsa.save(lsa_filename)
print("lsa saved in %s " % lsa_filename)
