# NLP

## NLP pipeline


+------------------+    +------------------+    +------------------+    +-------------------+
| data acquisition +--->+   text cleaning  +--->+  pre-processing  +--->+feature engineering|
+--------^---------+    +------------------+    +---------^--------+    +---------+---------+
         |                                     improving  |                       |
+--------+---------+    +------------------+    +---------+--------+    +---------^---------+
| monit & updating +<---+   deployment     +<---+    evaluation    +<---+  modeling         |
+------------------+    +------------------+    +------------------+    +-------------------+

### Data acquisition

- heuristics e.g. regex
- NLP techniques
    - public data set
    - scrape data (internet)
    - product intervention: enhance product to get the data
    - data augmentation
- NLP: use small dataset
    - synonym replacement -> use wordnet (not the stop word)
    - back translation
    - TF-IDF
    - Bigram flipping
    - replacing entities
    - adding noise to data
- Advanced techniques:
    - snorkel
    - EDA (easy data augmentation) and NLPAug
    - Active learning -> automatic labeling data

ideal: combination of public, labeled and augmented datasets

### Text cleaning

extract raw text from the input data (remove all the other non textual, markup, metadata, etc)
convert the text to the required encoding format

-> HTML
-> PDF
-> text emedding in an image

unicode normalization: text.encode("utf-8)
spelling correction/checker (e.g. python pyenchant)
image2text: OCR optical character recognition (e.g. python tesseract)
speech2text: ACR automatic speech recognition

### pre-processing

preliminaries: sentence segmentation and tokenization 
- python: nltk, tokenizer 
- go: [tokenizer](https://pkg.go.dev/github.com/sugarme/tokenizer)
frequent steps: 
- stop word removal
- stemming and lemmatization
- removing digits/punctuation
- lowercasing
other steps: 
- normalization: e.g. in social media text rules can be different
- language detection: (library polyglot) - language specific pipeline
- code mixing: mixing languages
- transliteration
advanced processing: 
- POS tagging: POS (Part of Speech) [pos tagging](https://towardsdatascience.com/part-of-speech-tagging-for-beginners-3a0754b2ebba#)
    - NN: Noun
    - VB: Verb 
    - DT: determiner
    - 
- named entity recognition (NER)
- parsing
- coreference resolution

### feature engineering or feature extraction

capture charecteristics of the text into vectors

-> convert data into a format that can be consumed by a machine

traditional approach: (harder to maintain, easier to understand)
- sentiment: count the # of positive and negative words per review
deeplearning approach: (simpler to maintain, but how is the result achieved)
- 

representation:
- image: pixels + intensity
- video: frames of images
- sound: amplitude at a given time
- text: see next chapter

#### text representation

e.g. sentiment analysis
- break the sentence into lexical units such as lexemes, words and phrases
- derive the meaning of each of the lexical units
- understand the syntactic (grammatical) structure of the sentense
- understand the context in which the sentence appears

appraches
- vectorization (VSM: vector space model)
    - [vector space](https://en.wikipedia.org/wiki/Vector_space)
    - [vector decomposition](https://en.wikipedia.org/wiki/Euclidean_vector#Decomposition)
    - cosime similarity
    - implementations:
        - one-hot encoding: (issues: size is variable, vocabulary is large, no notion of similarities, OOV (out of vocabulary))
        - bag of words (BoW): uses words to classify a sentense in a class (bag) (issues: vocabulary is large -> we could limit it, no notation of similarities, word order is lost)
        - bag of N-grams (tokens) chunk = n-gram (n contiguous words) -> provides context, but: still OOV and n > complexity grows
            BOW: 1-gram, bigram model (2), trigram model (3)
        - TF-IDF: so far no notion of importance of words
            TF: Term frequency -> how often a term/word occurs in a doc relative to its length
            IDF: Inverse Document Frequency -> measures the importance of the term accross the corpus/documents
    - summary:
        - discrete implementation: hampers the ability to capture relationships between words
        - sparse and high-dimensional represntation: hampers learning, computational inefficient
        - OOV is not handled
- distributed representation:
    - use neural networks to create dense, low-dimensional representation of words
    - terms:
        - distributional similarity: meaning of the word can be understood from the context
            - commotation: meaning is defined by context
            - denotation: literal meaning of a word
            - NLP rocks -> literal meaning is stones, but here it means good
        - distributional hypothesis
            - words that occur in similar context have similar meaning (e.g. cat & dogs)
        - distributional representation
            - like the TF-IDF, etc
        - distributed representation: dense and low dimensional
        - embedding: mapping between vector space coming from distributinal representation to vector space coming from distributed representation
        - vector semantics:
    - word embeddings:
        - pre trained: word2vec (google), etc
        - train own embeddings
            - CBOW: predict the center word given context of the surrounding words
            - SkipGram: predict the context words from the center word
    - going beyond words:
        - sum or average
        - Doc2Vec: 
    - issue remains: OOV
- universal language representation
    - RNN/Transformers -> transfer learning
    - Visualization: [t-SNE](https://towardsdatascience.com/t-sne-clearly-explained-d84c537f53a)
- handcrafted features
    - domain specific knowledge results in specific solution

### modeling

- start with simple heuristics
    - e.g. spam: blacklist
    - e.g. e-commerce: # of ordering towards buying experiences from other people
    - regex: Stanfords NLP's token regex and spaCy's rule-based matching -> using NLP techniques
- building your model
    - heuristics can be hard to maintain -> complex rule based systems
    - approaches
        - create a feature from the heuristics to your ML world
        - pre-process your input to the ML model
- building THE model
    - model stacking: using the output of one model to another model
    - model ensembling: using various models in parallel
    - transfer learning: transfer preexisting knowledge from a big ell trained model to a newer model at its initial phase
        like teacher transfering wisdom and knowledge to a student
    - use heuristics to find errors at the end of the modeling pipeline
- active learning: when we have small data set -> use user feedback to get more data

### evaluation

- use the right metric for evaluation
- intrinsic evaluation
    - use a training set (can eb automated)
    - popular metrics:
        - accuracy
        - precision
        - AUC/MRR/MAP/RMSE/MAPE/BLEU/METEOR
- extrinsic evaluation
    - business problem we try to solve

### deployment

- through a web/api service (spam detection)
- batch processing task

### monitoring and model updating


## example: text classification

### using embeddings:

- option 1: use a positive and negative word dictionary -> count the positive and negative words
- option 2: use cloud api(s)
- option 3: BoW representation
    - step1: split data into train and test data
    - step2: convert text into feature vectors -> BoW 
    - step3: train and evaluate the classifier
        - naive bayes classifier
        - logistic regression
        - support vector machine: SVM
- option 4: word embedding:
    using word2vec:
        - step2: loading and pre-processing: find word in the embedding and if found avg all words per sentence
            -> resulting vector is the feature vector representing the entire text
        - step3: see before train and evaluate the classifier
        - Issue: bulky model
    subword embedding and fasttext:
        - step2: we can use subwords to deal with OOV issue
        - issue: bulky model
    document embedding:
        - tweets are not regular text -> they are short, they have smileys and hashtags
- option 5: deep learning
    - step1: tokenize the txt and convert them into word index vectors
    - 

LIME: used to validate the classifier

What is we have no data?
- weak supervision
- crowd sourcing

## example Information Extraction

IE Applications:
- tagging/labeling news
- chatbots
- social media
- extracting data from forms and receipts

IE tasks -> extract knowledge from text
- keyword and keyphrase extraction -> KPE
- named entity recognition -> NER
- named entity disambiguation and linking
- relation extraction -> organization
- event extraction
- template filling (news extraction)

This is a domain specific approach leveraging rule based and ML/DL approaches

        | text
+-------+-------+
| sentense      |
| segmentation  |
+-------+-------+
        |
+-------+-------+
| word          |
| tokenization  |
+-------+-------+
        |
+-------+-------+     +-------+-------+ 
| port of speech+-----+    syntatic   |
| tagging       |     |     parsing   |
+-------+-------+     +-------+-------+
   Named Entity               | entity disambiguation
   Recognition        +-------+-------+
                      | coreference   |
                      | resolution    |
                      +---------------+
                            relation extraction
                            event extraction

Keyphrase Extraction
- goal: extract important words and phrases that capture the gist of the text
- the most popular method is unsupervised learning where words/phrases are placed as nodes in a weighted graph -. look at the most connected nodes

Named entity recognition
- goal: identity entities in a doc

## SRL: semantic role labeling

example: Marvin walked in the park, Marvin is the agent

predicate -> main verb (describe something about the subject) => V (walked)
noun -> zelfstandig naamwoord (argument of the predicate) => ARGO (Marvin)
adjactive -> modifier => ARGM LOC (in the park)


