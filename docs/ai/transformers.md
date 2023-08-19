# transformers

- RNN
- Attention
- Transfer Learning
- Scaling up

[huggingface transformers](https://github.com/huggingface/transformers)

## Recurrent neural networks

[rnn](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)
- uses LTSM: long term short term memory

- used a lot in translation systems
- Encoder-Decoder or Sequence2Sequence architecture
- uses hidden state

Weakness 1: final hidden state creates a information bottleneck 
-> Solution: Attention (allow access to all hidden states of the encoders)
-> Attention: the decoder assigns a different amount of weigth (attention) to each of the encoder statesat every decoding timestep.

Weakness 2: sequential, cannot be parallelized accross the input sequence
-> Solution: Self Attention
-> Allows attention to operate on all the states in the same layer of the neural network

## Transfer Learning

Train on 1 task and finetune it on a new task -> split model in body and head
- head is task specific
- during training the weigths of the body learn broad features

compared to supervised learning the approach typically produces high quality models
- trained more effectively on a variety of downstream tasks
- with much less labeled data

ULMFIT -> framework to adapt pretrained LTSM models for various tasks
ULMFIT steps:
- pretraining: predict the next word based on the previous word (language modeling)
    - pro: 
        - no labeled data is required
        - sources: Internet
- domain adaptation
    - adopt to a specific domain: predict the next word in a specific context
- fine tuning
    - classify

## transformer examples

- GPT: trained on BookCorpus
- BERT: trained on BookCorpus and English Wikipedia

## hugging face transformers

- implement the model architecture in code: TensorFlow/PyTorch
- load the pretrained weights from a server
- preprocess the input -> pass them through the model and apply some task specific postprocessing
- implement data loaders and define loss functions and optimizers to train the model

Deep learning frameworks:
- Tensorflow
- PyTorch
- JAX

use cases:
-> sentiment
-> named entity recognition (NER)
-> Q&A
-> summerization
-> translation
-> text generation

## challenges with transformers

- Language: mainly English
- Data availability: use transfer learning -> chapter 9
- Long documents: self-attention (ok for paragraph text) -> chapter 11
- Opacity: -> chaper 2 and 4 (how to detect errors)
- Bias: -> chapter 10