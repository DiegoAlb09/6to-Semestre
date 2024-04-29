#Modelo SVM

#Librerias
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pandas as pd
from collections import Counter
import sklearn as sk
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import matplotlib.pyplot as plt

#nltk.download('punkt')
#nltk.download('stopwords')

#Variables Globales
global dataset
dataset = pd.read_csv("C:/Users/diego/Desktop/Universidad/6to-Semestre/Aprendizaje_Inteligente/comments.csv")
print(dataset.head())

#Funcion para obtener los indices de las reviews positivas y negativas  
def get_indices():
    positive_indices = []
    negative_indices = []
    for i in range(len(dataset)):
        if dataset["rating"][i] == 1:
            positive_indices.append(i)
        else:
            negative_indices.append(i)
    return positive_indices, negative_indices

#Funcion para obtener las palabras de las reviews positivas y negativas
def word_vectors():
    positive_indices, negative_indices = get_indices()
    positive_words = []
    negative_words = []
    for i in range(len(dataset)):
        if i in positive_indices:
            positive_words.append(dataset["comment"][i])
        else: 
            negative_words.append(dataset["comment"][i])
    return positive_words, negative_words

#Funcion para filtrar las palabras que no queremos de las reviews
def filter_words(words):
    filtered_words = []
    for comment in words:
        tokens = word_tokenize(comment)
        english_stopwords = set(stopwords.words('spanish'))
        filtered_words.extend([word.lower() for word in tokens
                                if word.isalpha() and word.lower()
                                not in english_stopwords])
    return filtered_words

#