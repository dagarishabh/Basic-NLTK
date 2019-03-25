import nltk
from nltk.corpus import state_union
from nltk.tokenize import word_tokenize
for i in word_tokenize("Today is a beautiful day."):
    words = nltk.word_tokenize(i)
    tagged = nltk.pos_tag(words)
    print(tagged)
