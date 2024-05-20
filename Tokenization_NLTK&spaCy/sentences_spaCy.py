# spaCy
#%% import pakages

import spacy

# %% Load English tokenizer , tagger , parser and NER

parser = spacy.load("en_core_web_sm")

# %% Tokeniation
text = "Mr. Smith loves tacos. He has a Ph.D. in tacology."
tokens = parser(text)
print("tokens: ")
print (tokens)
for sent in tokens.sents:
    print("Sentence")
    print(sent)
    print()

# %%
