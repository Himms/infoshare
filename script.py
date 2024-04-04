# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
#from pip._vendor import requests
from bs4 import BeautifulSoup
import spacy
from collections import Counter
from string import punctuation
from gensim.models import Word2Vec
#from pprint import pprint

import sys


a = "https://www.tripwire.com/state-of-security?_gl=1*t3em0b*_up*MQ..&gclid=Cj0KCQiArrCvBhCNARIsAOkAGcVbSSCZ0gzCcbMYk3uuhS6CENXDJGgqhTDET-9G1T0WzNHQ0kbHbLsaAnY7EALw_wcB"
b = "https://darkobds5j7xpsncsexzwhzaotyc4sshuiby3wtxslq5jy2mhrulnzad.onion"
c = "https://aracari7pazm6nxcbgzj3nl4hddaxzsniqrlddwhqh4vebbfzd5hseyd.onion"
URL = a
page = requests.get(URL, timeout=(10,200) )
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="content")

infos = results.find_all("h3", class_= "node--title")

for info in infos:
    print(info.text, end="\n"*2)

for info in infos:
    #print(info)
    #spacy.cli.download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")
    def get_hotwords(text):
        result = []
        pos_tag = ['PROPN', 'ADJ', 'NOUN', 'VERB'] 
        doc = nlp(text.lower()) 
        for token in doc:
            if(token.text in nlp.Defaults.stop_words or token.text in punctuation):
                continue
            if(token.pos_ in pos_tag):
                result.append(token.text)
        return result

    new_text = info.text
    
    output = set(get_hotwords(new_text))
    most_common_list = Counter(['cybersecurity', 'attack', 'cyber', 'money' , 'threat' , 'financial' , 'bank' , 'intelligence' , 'fraud', 'detection', 'intrusion', 'million', 'billion','thousand']).most_common()
    word2vec = Word2Vec(most_common_list, min_count=0)
    #comp=word2vec.wv.most_similar('money')
    #print('comp', comp)
    #compare=word2vec.wv.most_similar(['cyber', 'money' , 'threat' , 'financial' , 'bank' , 'intelligence' , 'fraud'])
    for item in most_common_list:
        #print(item[0])
        compare=word2vec.wv.most_similar(item[0])
        if(compare is True):
                print('info.text')
        #print(compare)
        #print(item[0])
        #for info in infos:
            #print(info)
            #if(compare is True):
                #print(info.text)
       # comp1 = nlp(item[0])
       # comp2 = nlp('cyber' or 'money' or 'threat' or 'financial' or 'bank' or 'intelligence' or 'fraud')
       # comp1.similarity(comp2)
sys.exit ()