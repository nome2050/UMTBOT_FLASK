import nltk
import warnings
warnings.filterwarnings("ignore")


import numpy as np
import random
import string


f=open('questions.txt','r',errors = 'ignore')
raw=f.read()
raw=raw.lower()
#nltk.download('punkt') # first-time use only
#nltk.download('wordnet') # first-time use only
sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)

sent_tokens[:2]
word_tokens[:5]


lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    print(req_tfidf)
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry"
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response




def questionpredict(text):
    user_response = text
    if user_response==None:
        user_response='welcome'
    user_response=user_response.lower()
    text = response(user_response)
    answer = text.split(',')
    size = answer.__len__()
    question = answer[size-1]
    #question = question.replace('.','')
    #question.strip()
    #question.rstrip()
    return question

# user_response = input()
# user_response=user_response.lower()
# text = response(user_response)
# answer = text.split(',')
# size = answer.__len__()
# question = answer[size-1]
# print(question)
