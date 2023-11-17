import pymorphy2

morph = pymorphy2.MorphAnalyzer()
def initial(word):
    v = morph.parse(word)[0].normal_form
    return v

def pos(word, morth=pymorphy2.MorphAnalyzer()):
    "Return a likely part of speech for the *word*."""
    return morth.parse(word)[0].tag.POS
