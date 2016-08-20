Topic Modeling of my own articles on POCKET web service.

.. image:: img/robot.png

Summary:
--------
This project is derived from my over-zealous saving of web articles.  The reason that I save articles is to learn about a topic.  I hoped by doing this project; I could cluster my articles into bite-size chunks that would allow for easier learning.


Results:
---------
Using Latent Dirichlet(LDA) and Latent Semantic Analysis(LSA) I performed topic modeling on 1000 articles that I saved over the past three years into my Pocket account. 

With LDS modeling, I found that the central topics were: 
#  python 
#  artifical intelligence
#  machine learning
#  data science


With LSA modeling, I found that the central topics were:
#
#
#
#



Run your own analysis:
---------------------
1.  You need an API account with Pocket
2.  Gather Training and Test Data :: $ python get_data.py
3.  Clean Data :: $ python clean_data.py
4.  Apply LDA or LSA modeling :: $python apply_lda.py
5.  Visualize results: lda.ipynb or lsa.ipynb


