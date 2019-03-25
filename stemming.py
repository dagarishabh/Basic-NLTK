from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
ps=PorterStemmer()
w={"run","runs","running"}
for x in w:
    print(ps.stem(x))
