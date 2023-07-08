import nltk

text_ = "one two three"
tokens_ = nltk.word_tokenize(text_) #dividing the phrase into separate words - tokens ['one', 'two', 'three']
print(tokens_)

from nltk.corpus import wordnet
word_ = wordnet.synsets("spectacular") # finding synonyms
print(word_)
print(word_[1].definition()) # writing the definition of the 2 word

from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
print(stemmer.stem("wolves")) # prints the word without affixes: wolves->wolv

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("wolves")) # prints the root of the word: wolves -> wolf
