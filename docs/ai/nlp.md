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

- 