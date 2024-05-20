#NLTK
#Natural language Toolkit(NLTK) is popular Python NLP Library

#%% packages
import nltk 
# %%
# Download all the data associated with NLTK
nltk.download('all')
# %%
text = "Mr. Smith loves tacos. He has a Ph.D. in tacology."
# %%
tokenized_sentences = nltk.sent_tokenize(text)
print("Tokenized Sentences")
print()
print (tokenized_sentences)
for sent in tokenized_sentences:
    print('Sentence:')
    print(sent)
    print()
# %%
