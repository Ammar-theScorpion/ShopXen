from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import *
import pickle
import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
import string
import urllib.parse
import json
import random

from nltk import pos_tag
from sklearn.feature_extraction import DictVectorizer
######
###############
# Create your views here.

#d = ChatHistory.objects.all()
#d.delete()
#d = ChatHistory.objects.all()
#d.delete()
with open('data.json', 'r') as json_file:
    data = json.load(json_file)

chatbot_responses = {}
for item in data:
    chatbot_responses[item['tag']] = item['responses']

def chathistory(request):
    response = ''
    body = request.body
    print(body)
    decoded_str = urllib.parse.unquote(body.decode('utf-8'))
    query = decoded_str.split('=')[1]


    feature_dict = preprocess_text_to_features(query)
    pos_tags = extract_pos_tags(query)
    for tag in pos_tags:
        feature_dict[tag] = True
        
    vectorizerfile = open('vectorizer.pickle', 'rb')
    vectorizer = pickle.load(vectorizerfile)

    feature_vector = vectorizer.transform([feature_dict])
    chatfile = open('chatbot.pickle', 'rb')
    chatmodel = pickle.load(chatfile)

    predicted_tag = chatmodel.predict(feature_vector)[0]
    response_options = chatbot_responses[predicted_tag]
    response = random.choice(response_options)
    
    ch, created =  ChatHistory.objects.get_or_create(pk=1)
    ch.add_user_query(query)
    ch.add_bot_response(response)
    ch = ChatHistory.objects.get(pk=1).histoy()

    return HttpResponse(ch)


def preprocess_text(text):
    tokens = nltk.word_tokenize(text)

    tokens = [word.lower() for word in tokens]

    stop_words = set(nltk.corpus.stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words and word not in string.punctuation]

    bigrams_list = list(ngrams(tokens, 1))  # '1' n-gram size

    lemmatizer = nltk.stem.WordNetLemmatizer()
    tokens = [' '.join(bigram) for bigram in bigrams_list]

    return tokens

def extract_pos_tags(text):
    tokens = word_tokenize(text)
    pos_tags = pos_tag(tokens)
    return [tag for _, tag in pos_tags]

def preprocess_text_to_features(text, n=1):
    preprocessed_text = preprocess_text(text)
    feature_dict = {' '.join(bigram): True for bigram in preprocessed_text}
    
    # Extract POS tags and add them as features
    pos_tags = extract_pos_tags(text)
    for tag in pos_tags:
        feature_dict[tag] = True
    
    return feature_dict

def chatbot(request):
    ch = ChatHistory.objects.all()
    if ch:
        ch= ch.get(pk=1).histoy()
    return render(request, 'Xen/chatbot.html', {'history':ch})

def home(request):
    category = Category.objects.all()
    return render(request, 'Xen/store.html', {'categories':category})


def product_detail(request, category_id):
    category = Category.objects.get(category_id=category_id)
    products = category.product_set.all() 
    return render(request, 'Xen/product_details.html', {'products':products})


def preSales(request, product_id):
    product = Product.objects.get(product_id=product_id)
    print(product)
    return render(request, 'Xen/presales.html', {'product':product})
