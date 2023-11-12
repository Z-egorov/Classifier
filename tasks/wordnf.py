import pymorphy2

def nf(word):
    morph = pymorphy2.MorphAnalyzer()
    v = morph.parse(word)[0].normal_form
    return v











