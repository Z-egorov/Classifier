import pymorphy2  # $ pip install pymorphy2

def pos(word, morth=pymorphy2.MorphAnalyzer()):
    "Return a likely part of speech for the *word*."""
    return morth.parse(word)[0].tag.POS


#-----------------------------------------------------------------------------------------------------------------------
'''
words = "Однако я так и не смог закончить".split()
functors_pos = {'INTJ', 'PRCL', 'CONJ', 'PREP'}  # function words
print(*[word for word in words if pos(word) not in functors_pos])
# -> я смог закончить'''
