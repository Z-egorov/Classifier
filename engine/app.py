import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Embedding, MaxPooling1D, Conv1D, GlobalMaxPooling1D, Dropout, GRU
from keras import utils
from keras.utils import pad_sequences
from keras.preprocessing.text import Tokenizer
from keras.callbacks import ModelCheckpoint
from keras import utils
import numpy as np
import html2text
import requests
import re
import sys

num_words = 10000
max_len = 35
nb_classes = 33
tokenizer = Tokenizer(num_words=num_words)

# model_gru_save_path = r"/home/zhenia/Muzhichki/engine/best_model_gru.h5"

# model_gru = Sequential()
# model_gru.add(Embedding(num_words, 32, input_length=max_len))
# model_gru.add(GRU(16))
# model_gru.add(Dense(33, activation='softmax'))

# model_gru.compile(optimizer='adam', 
#               loss='categorical_crossentropy', 
#               metrics=['accuracy'])

# model_gru.load_weights(model_gru_save_path)

model_gru = keras.models.load_model('/home/zhenia/Muzhichki/engine/GRU_MODEL')

def get_words(url):
    resp = requests.get(url)
    html = resp.text
    text = html2text.html2text(html)
    words_array = text.split()

    for i in words_array: 
        if len(i) <= 3: words_array.remove(i)
    
    words_non_filtered = ' '.join(words_array)
    words = re.sub(r'http\S+', '', words_non_filtered)
    
    return words

usr_link = sys.argv[1]

usr_words = get_words(usr_link)
sequence_test = tokenizer.texts_to_sequences([usr_words])
data = pad_sequences(sequence_test, maxlen=max_len)
result = model_gru.predict(data, verbose=0)

def get_theme(argument):
    if argument == 0: return "Adult"
    elif argument == 1: return "Arts"
    elif argument == 2: return "Autos"
    elif argument == 3: return "Beauty"
    elif argument == 4: return "Books"
    elif argument == 5: return "Business"
    elif argument == 6: return "Community"
    elif argument == 7: return "Computers"
    elif argument == 8: return "eCommerce"
    elif argument == 9: return "Finance"
    elif argument == 10: return "Food"
    elif argument == 11: return "Gambling"
    elif argument == 12: return "Games"
    elif argument == 13: return "Health"
    elif argument == 14: return "Heavy Industrisy"
    elif argument == 15: return "Home"
    elif argument == 16: return "Hobbies"
    elif argument == 17: return "Internet"
    elif argument == 18: return "Jobs"
    elif argument == 19: return "Law"
    elif argument == 20: return "Lifestyle"
    elif argument == 21: return "News"
    elif argument == 22: return "Online"
    elif argument == 23: return "People"
    elif argument == 24: return "Pets"
    elif argument == 25: return "Real Estate1"
    elif argument == 26: return "Reference"
    elif argument == 27: return "Scinece"
    elif argument == 28: return "Sensitive Subjects"
    elif argument == 29: return "Shopping"
    elif argument == 30: return "Sports"
    elif argument == 31: return "Travel"
    elif argument == 32: return "Vehicles"

theme = get_theme(np.argmax(result))

f = open("/home/zhenia/Muzhichki/engine/data.txt", 'a')
data_to_write = str(usr_link) + ',' + theme + '\n'
f.write(data_to_write)

print(theme)
sys.stdout.flush()