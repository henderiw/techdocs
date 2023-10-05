##

## basics

- dictionary is 600K words
- each word is a unique number
- sentence is a seq of words

are ... -> predict the next word
what is the likelihood of the next word (%), for each word in the dictionary

how are ... -> predict the next word with more context
the guess will be better with more context

Lets assume a dictionary has 50K words
with 2 dimensions -> 50K x 50K = 2,5B
with 3 dimensions -> 50k x 50k x 50k = 125Trillion

-> transformers (Attention is all you need)
100K context solves context in a clever way

AUTOREGRESSIVE MODEL

## creativity