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
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from nltk import pos_tag
from sklearn.feature_extraction import DictVectorizer
from nltk.stem import PorterStemmer
import json
import pickle  # Unchanged
import urllib.parse
import random
import string
import nltk
import numpy as np
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem import PorterStemmer
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestClassifier
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ChatHistory  # Import your ChatHistory model

# Load your model
with open('your_model.pickle', 'rb') as model_file:
    chatmodel = pickle.load(model_file)

# Load other resources
with open('vectorizer.pickle', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

with open('train_data.json', 'r') as json_file:
    data = json.load(json_file)

# i don't konw
sim_tfidfile = open('similarity_tfidf.pickle', 'rb')
sim_tfidf = pickle.load(sim_tfidfile)

# i don't konw
pat_tfidfile = open('tfidf_matrix.pkl', 'rb')
pat_tfidf = pickle.load(pat_tfidfile)

chatbot_responses = {}
for item in data:
    chatbot_responses[item['tag']] = item['responses']


# Unchanged check_similarity function
def check_similarity(query):
    query_ = []
    stemmer = PorterStemmer()
    query = query.split(' ')
    for pattern in query:
        pat = ''
        pat += stemmer.stem(pattern.lower())+' '
        
        query_.append(' '.join(word_tokenize(pat)))
    g = sim_tfidf
    uqv = sim_tfidf.transform(query).toarray()
    cosine_similarities = cosine_similarity(uqv, pat_tfidf).flatten()
  
    idxs = np.where(cosine_similarities>0.3)
    if len(list(idxs[0]))==0:
        return -1

    return 1

import json

# Function to load product data from the database file
def load_product_data(file_path):
    with open(file_path, 'r') as file:
        product_data = json.load(file)
    return product_data

# Load product data from the database
product_data = load_product_data('product_fixture.json')

# Function to retrieve product information from the database
def get_product_info(product_name, predicted_tag):
    for product in product_data:
        if product["fields"]["name"] == product_name:
            if predicted_tag == "product_warranty":
                return {"product_warranty": product["fields"]["warranty_period_months"]}
            elif predicted_tag == "product_return":
                return {"product_return": product["fields"]["return_period_days"]}
            elif predicted_tag == "product_discount":
                return {"product_discount": product["fields"]["discount_percentage"]}
            elif predicted_tag == "product_features":
                return {"product_features": product["fields"]["feature_list"]}
            elif predicted_tag == "product_price":
                return {"product_price": product["fields"]["price"]}
            elif predicted_tag == "product_colors":
                return {"product_colors": product["fields"]["colors"]}
            elif predicted_tag == "product_weight":
                return {"product_weight": product["fields"]["weight_grams"]}
            elif predicted_tag == "product_images":
                return {"product_images": product["fields"]["image_link"]}
            # Add more conditions for other tags as needed
    print("No item")
    return {}

def read_training_data(file_path):
    with open(file_path, 'r') as file:
        training_data = json.load(file)
    return training_data
training_data = read_training_data('train_data.json')

# Function to get the appropriate response based on the predicted_tag
def get_response(predicted_tag, product_name=None):
    for data in training_data:
        if data["tag"] == predicted_tag:
            product_info = get_product_info(product_name, predicted_tag)
            response = data["responses"][0].format(product_name=product_name, **product_info)
            return response
    return "Sorry, I don't have a response for that."

# Done
def preprocess_text(text):
    tokens = nltk.word_tokenize(text)

    tokens = [word.lower() for word in tokens]

    stop_words = set(nltk.corpus.stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words and word not in string.punctuation]

    bigrams_list = list(ngrams(tokens, 1))  # '1' n-gram size

    lemmatizer = nltk.stem.WordNetLemmatizer()
    tokens = [' '.join(bigram) for bigram in bigrams_list]

    return tokens

# Done
def extract_pos_tags(text):
    tokens = word_tokenize(text)
    pos_tags = pos_tag(tokens)
    return [tag for _, tag in pos_tags]

# Done
def preprocess_text_to_features(text, n=1):
    preprocessed_text = preprocess_text(text)
    feature_dict = {' '.join(bigram): True for bigram in preprocessed_text}
    
    # Extract POS tags and add them as features
    pos_tags = extract_pos_tags(text)
    for tag in pos_tags:
        feature_dict[tag] = True
    
    return feature_dict

import spacy

# Replace 'path_to_output_directory' with the actual path to your saved model
model_path = "path_to_output_directory"
# Load the trained NER model
nlp = spacy.load(model_path)

def extract_product_name(user_input):
    doc = nlp(user_input)
    product_names = [ent.text for ent in doc.ents if ent.label_ == "PRODUCT"]
    return product_names

user_context = {}

@csrf_exempt
def chathistory(request):
    response = ''
    body = request.body
    decoded_str = urllib.parse.unquote(body.decode('utf-8'))
    query = decoded_str.split('=')[1]
    response = 'Sorry, but I cannot help you with that'
    global user_context

    # Check for similarity
    if check_similarity(query) != -1:
        # like get_tag function that returns the predicted_tag
        feature_dict = preprocess_text_to_features(query)
        pos_tags = extract_pos_tags(query)
        for tag in pos_tags:
            feature_dict[tag] = True
        feature_vector = vectorizer.transform([feature_dict])
        predicted_tag = chatmodel.predict(feature_vector)[0]
        ########
        product_names = extract_product_name(query)

        # flag to save if there is a product name or not
        flag = 1 
        if not product_names:
            flag = 0
            # Try to extract product names from the last query
            last_query = user_context.get("last_query", "")
            product_names = extract_product_name(last_query)
            print("there is no products name")
         
        responses = []
        # Iterate over product_names and retrieve product information
        for product_name in product_names:
            # print(f"predicted_tag {predicted_tag}")
            response = get_response(predicted_tag, product_name)
            # print(response)
            responses.append(response)

        if responses:
            final_response = "\n".join(responses)
        else:
            final_response = f"Sorry, I couldn't find information about {predicted_tag.replace('_', ' ')} for the specified products."

        # Save context for future queries
        if flag != 0:
            user_context["last_query"] = query
        user_context["last_response"] = final_response

        print(final_response)
        response = final_response

    ch, created =  ChatHistory.objects.get_or_create(pk=1)

    # The rest of your code to save the chat history and return the response

    ch.add_user_query(query)
    ch.add_bot_response(response)
    # ch = ChatHistory.objects.get(pk=1).histoy()

    # text = ''
    # for i in ch:
    #     print(i.keys())
    #     text += i['User'] + '@' + i['Bot'] + '@'
    
    return HttpResponse(response)
    

# Unchanged Django views (chatbot, home, product_detail, preSales, delchat)

def chatbot(request):
    ch = ChatHistory.objects.all()
    if ch:
        ch= ch.get(pk=1).histoy()
    return render(request, 'Xen/index.html', {'history':ch})

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

def delchat(request):
    d = ChatHistory.objects.get(pk=1)
    d.delete()
    return HttpResponse('')