import nltk
from nltk.corpus import stopwords 
from nltk.stem.wordnet import WordNetLemmatizer
import string
stop = set(stopwords.words('english'))
exclude = set(string.punctuation) 
lemma = WordNetLemmatizer()
def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized


doc1=" Great place to visit, the service here is awesome, courteous staff. The food is also good. The mocktails are really nice. We have ordered a Virgin sex on the beach it was nice had a berry taste, then a virgin mojito (orange) I personally loved it, and a virgin margarita (kiwi), each and every mocktail was great. Then we ordered Moroccan cheese cigar which wasn't that good actually the pull was missing and it wasn't that juicy as we expected, though the sause with it was great. Then we had Lasagne de Verde which was really nice and the portion size was also good. Then we had Pizza Kuzina, it was thin crust pizza, the crust was crunchy and pizza was good in overall view. We didn't had any space for dessert. The best thing about the restaurant was it's service. The best service in the locality, it shows how view changes due to this one thing. The cost is also good a bit costly , though it's worth it."


doc_complete = [doc1]
doc_clean = [clean(doc).split() for doc in doc_complete] 



import gensim
from gensim import corpora

# Creating the term dictionary of our courpus, where every unique term is assigned an index. 
dictionary = corpora.Dictionary(doc_clean)

# Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]



# Creating the object for LDA model using gensim library
Lda = gensim.models.ldamodel.LdaModel

# Running and Trainign LDA model on the document term matrix.
ldamodel = Lda(doc_term_matrix, num_topics=1, id2word = dictionary, passes=50)
print(ldamodel.print_topics(num_topics=1, num_words=4))
