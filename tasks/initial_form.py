import pymorphy2

morph = pymorphy2.MorphAnalyzer()

def initial(word):
    v = morph.parse(word)[0].normal_form
    return v
