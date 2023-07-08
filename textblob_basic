from textblob import TextBlob

statement = TextBlob("I like green tea a lot more than coffee")
print(statement.sentiment) # polarity - positivity/negativity, subjectivity - if the author is absolutely sure: Sentiment(polarity=0.15, subjectivity=0.4)

print(statement.tags) # writes the part of speech of every word: [('I', 'PRP'), ('like', 'VBP'), ('green', 'JJ'), ('tea', 'NN'), ('a', 'DT'), ('lot', 'NN'), ('more', 'JJR'), ('than', 'IN'), ('coffee', 'NN')]

err_statement = TextBlob("I have neverr seen this bird befor")
print((err_statement.correct())) # I have never seen this bird before (corrects only spelling mistakes, not grammar)

print(statement.translate(from_lang='en', to='fr')) # J'aime beaucoup plus le thé vert que le café
