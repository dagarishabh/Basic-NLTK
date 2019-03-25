import nltk
from nltk.corpus import stopwords 
from nltk.stem.wordnet import WordNetLemmatizer
import string
from nltk import WordPunctTokenizer
from nltk.stem import PorterStemmer
from nltk.tokenize import WordPunctTokenizer
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
import operator

stop = set(stopwords.words('english'))
exclude = set(string.punctuation) 
lemma = WordNetLemmatizer()
def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized
tokenizer = WordPunctTokenizer()

def get_bigrams(myString):
    a=list()
    sentence=nltk.sent_tokenize(myString)
    for s in sentence:
        s=clean(s)
        #print(s)
        tokens = tokenizer.tokenize(s)
        a=a+list(nltk.bigrams(tokens))
    return a

f=open("input1.txt","r")
#evalbigrams=get_bigrams("today is a good day. good day i good.")
evalbigrams=get_bigrams(f.readline())

Dict={}
for p in evalbigrams:
    Dict[p]=0
for p in evalbigrams:
    Dict[p]=Dict[p]+1
sorted_dict = sorted(Dict.items(), key=operator.itemgetter(1))
with open("output1.txt","a") as f1:
    for key,val in sorted_dict:
        q1="( "
        for a in key:
            q1=q1+a
            q1=q1+","
        q1=q1 + " )"
        q=q1 + "=>" + str(val)+"\n"
        #print(q)
        f1.write(q)
        

    
