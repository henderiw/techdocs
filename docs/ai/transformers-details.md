# transformers

## terminology

- stack:
    - indentically sized layers
    - can be encoder or decoder
    - transformers: learn and see more as they rise in the stack
    - analogy: empire state building: the higher you go the more you see
- sublayer:
    - each layer contains sub-layers. Each sub-layer of different layer has an identical structure -> boosts HW performance
    - original transformer has 2 sublayers
        - a self attention sub-layer
        - a classical feedforward network with some tweaking
- attention heads:
    - a self attention sublayer is divivided in n independent and idential layers call heads
    - original tranformer had 8 heads
    - hw optimized

## attention 

runs dot between word/token vectors -> determine strong relationships with all the words in the sentense including itself

encoder
- embedding layer is only present at the bottom level of the stack:
    - tokenizer e.g. BPE
    - embedding: skipgram from word2vec -> skipgram : center word + previous 2 words + next 2 words
    - you can compare 2 vectors using cosine simularity
    - positional encoding (provide context where the work resides in the sentense)
- a multi-headed attention sublayer
    - split in 8 pieces
    - within a head
        - A Q (query) matrix with dimension d64. It seeks for all the KV paire of the other word matrices
        - A K (key) matrix with dimension d64 -> trained to provide an attention value
        - A V (value) matrix with dimension d64 -> trained to provide another attention value
        - Attention (Q, K, V) = softmax(QK(T)//dk)V
    - concatenate the results from the various heads
    - post layer normalization
- a fully connected feedforward network
- info:
    - the d-model is constant accross all operatoins (e.g. 512 vectors)

decoder
- output embeddings (only at the lowest layer) + positional encoding
- a multi-headed masked attention mechanism
    - masks the future words
- a multi-headed attention mechanism
    - only attends the words, not future words
    - takes K, V from the encoder into account -> decoder uses the encoders trained data
- fully connected position-wise feedforward network

## fine tuning BERT

BERT added new mechanisms to the lego bricks
-> bidirectional multi-head attention sub-layer => allows to look at all words of the sentense at the same time

original Transformer model:
- stack: N=6
- dimensions: d-model = 512
- attention heads: 8
- dimensions of head: d-model/heads = 512/8 = 64

BERT model
- no decoder layers
- stacks: N=12
- dimensions: d-model = 768
- attention heads: 12
- dimensions of head: d-model/heads = 768/12 = 64
- parameters: 110 Million

BERT Large model
- no decoder layers
- stacks: N=24
- dimensions: d-model = 1024
- attention heads: 16
- dimensions of head: d-model/heads = 1024/16 = 64
- parameters: 340 Million

dimensions -> working memory

Train the model to make predictions:
- MLM: Masked language modeling -> mask the next part of the sentenses (we are blind)
- Next Sentence Prediction (NSP) -> randomly mask a word
    - 10% don't mask
    - 10% replace a token with a random token
    - 80% mask

BERT was also trained for next sentense prediction 
- tokens [CLS] -> predict the next sentense [SEP] signals the sentense separation

BERT is a 2 step framework:
- step1: pre-taining
    - Model: see before -> 110Million
    - Unlabeled training tasks: Masked LM (MLM), next sentence prediction (NSP)
    - Training Data: book corpus, wikipedia
- step2: finetuning
- step2: finetune downstream tasks


Steps:
- pre-training
    - define model architecture
    - training the model on MLM and NSP tasks
- fine tuning substep1
    - Initializing the downstream model chosen with the trained parameters of the pretrained BERT model
    - Fine-tuning the parameters for specific downstream tasks
        - RTE: recognizing textual entailment
        - Q&A:
        - SWAG