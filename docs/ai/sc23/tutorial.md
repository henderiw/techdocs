presenters

Dhabaleswar K. (DK) Panda Ohio State University
Aamir Shafi Ohio State University
Chen Chun Chen Ohio State University
Hari Subramoni Ohio State University
Nawras Alnaasan Ohio State University
Jinghan Yao Ohio State University


[slide](https://web.cse.ohio-state.edu/~subramoni.1/sc23-hidl.pdf)

training:

https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=4,2&seed=0.06901&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false

inference

use cases
- model -> prediction -> explanation -> human


CNN:
- convolution operation
    - convolution operation
        input -> filter -> aggregate 
        different filters will give a different feature

## Frameworks:

Tensorflow
- lazy execution versus eager execution
    edge: flow of knowledge
    tensor: represent data (scalar, multi-dimensional arrays, etc)

Keras: higher level language

PyTorch (meta) -> python, c++/c
- ease of expression

How do people select the framework to use?
- TPU HW means tensorflow
- PyTorch is more modular compared to tensorflow

How does JAX fit in this framework -> new initiative of Google

## overview of execution environment

- hw and sw stack need to be aligned
- parallelizing: K-Means
- support for parallel and distributed execution
    - dask -> seem important -> big data framework (run in parallel on multiple nodes)
    - cuML
- cuML -> multi-node 

## tutorial

### lab1 (ML)

find 100 clusters, iterations 3000 -> 1 GPU
find 100 clusters, iterations 6000 -> 2 GPU -> uses mpi library

-> uses cumlHanle with MPI communicator
-> uses fit_predict() function

## deep learning DNN

distributed deeplearning network training

3 layers -> input is not counted
forward pass/backward pass -> goal is adjust parameters

input multiplied by the weigth by every neuron
output -> prediction, error = Loss(Pred, Output) -> with supervised learning we know the output, so we can calculate the loss
backward pass -> adjusts the weigths

g function -> activation function -> examples  RELU, Leaky RelU Sigmoid, tanh (non linearity functions)

slide60

- inputs get multiplied by weights
- summation and bias (bias)
- activation (introduce non linearity)
- output

you define per layer the # neurons + could define your own activation fn

### leanring rate

learning rate -> based on the error how should we adjust the weigths
-> gradient decent

-> important for good accuracy and be fast
What value to start with and how to adjust it?
-> option 1: try and error, or look at others
-> option 2: hyperparameter optimization (automatic)

### batch size

batch gradien descent -> complete batch size
stochastic gradient descent -> batch size = 1 -> slow
mini-batch gradient descent -> mini batch (32/64/128) -> fwd/bwd pass
-> batch size is also dependent on the underlying HW size

one full pass over N is called an epoch of training

### parallel training and distributed 

A100 with 80GB
-> Language Models -> BERT, GPT3: 170B parameters
-> Vision Models -> AlexNet -> ResnET -> NASNet -> Vision Transformers

Moved to multi-GPU training

larger models -> better accuracy
more data -> better accuracy

model size: layers

### overfitting and underfitting

overfitting: model big and data is small -> model memorizing 
underfitting: model small and data is big

### parallelism

data parlalism -> same model on different machine with different dat
model parallism -> 
hybrid parallism ->

## Vision and language models

### NLP

interaction between computer and human language
- machine translation
- information retrieval
- sentiment analysis
- information extraction
- Q&A/Chat

Transformers
Model size grows a lot

Seq2Seq
-> slide 73 -> S is a representation

slide 73 -> if input is big the model is big
slide 74 -> embedding
    -> vocabulary of size 4
    -> vocabulary size of 65K or 12K -> 12K dimensionins -> group them in clusters/spatials -> can encode other features

RNN shortcoming -> if input is big, model is big or we loose context
RNN require recursion -> cannot proceed w/o the previous input

Transformers -> attention is all you need -> allows massive parallel operation -> can take 

encoder
- n decoder blocks
decoder
- n decoder blocks

self attention
- potitional encoder (where )
- multi-head attenation -> NxN (N=word)

Q, K, V vectors
-> a way to do reteival (datbase -> user give a query, compare query to all keys in the db -> value is the output)

context window is 16K or 32K tokens in transformers -> there is a limit, but the limits are bigger

BERT -> only encoder block
GPT -> only decoders

training and inference are different

increasing model size -> 

### ComputerVision

fiels of AI that enables meaningfull info from digital images, videos, etc

- where are the objects in the image
- classification

families:
- CNN (Alexnet)
- Vision transformer architecture

convolution operation
- input + filter (supposed to extract information)

-> filter for vertical edge
-> sobel filter -> vertical and horizontal edges

In CNN we can 

slide 90: example operation
Input -> feature learning (convolution) -> classification

ImageNet -> 2012 introduced deep learning with RNN

Alexnet
- 8 trainable layers
- 62.3

slide 93: inter GPU communication
slide 95: 

### vision transformer

split the image in patches

slide98
transformers
-> context is bigger with transformer
-> positional encoding -> knows the eye is not in the right place

with CNN you are limited to the filter size and as such

today state of the art is CNN + vision transformer
BEiT is superior over CNN(s)

## data parallelization

different data on 5 different machi
issue: we train 5 different models

solution: MPI: AllReduce

each machine has different gradients -> AllReduce -> reduced gradient
reduced gradient is equal to all machines for 
this happens multiple times in parallel - epoch

How to proof convergence -> you can't

slide 110
- model size matters

slide112
- async -> higher epoch per second (EPS) -> lower accuracy per epoch (APE)

## exercise 2

DNN training
- horavad
    - broadcast

## HPC cluster architectures

availability of curated datasets
higher performance elements

Hardware architectures
- interconnects (infiniband, ROCE, omni-path)
    requirements
        - low latency
        - high BW
        - low CPU overhead
    Openfabric
- processors 
    TPU(s): CISC style instruction set
    IPU: intelligent processing unit

Communication middleware
- MPI: message passing interface (MPI
    Options:
        - shared memory
        - distributed memory model (complex but scalable)
        - partitioned global address space (PGAS)
    - AllReduce:
        - babys need to talk to eachother -> 
    - MVAPI
- NVIDEA NCCL (nicle)
    - based 

## systems - distributed 
- NCCL2: slide144 focus on large message size
- MVAPICH2-GDR: slide145

sw stack for

ML/DL - Tensorflow/pytorch/Mxnet - Horovad - MVAPICH2 (CPU) or MVAPICH2-GDR (GPU)
-> pure data parallelism

AccDP:
- multiple model replicas on the same GPU
- 

## model/hybrid parallism
- GPipe
- FLexFlow:
    - looks at the model and optimizes the ezecution
- HyPar-Flow:
    - combines data/model parallism
- GEMS:
    - GPU enabled memory Aware Model parallism
    - underutilizing memory -> start the next model but comunicate between eachother
    - goal train on large images
- SUPER:
    - 
- Hy-Fi:
- ZERO: (Microsft/Deepspeed)
    - no need to store the data on the GPU when not needed
    - more communication but less memory consumption per GPU
- 3D Parallism:
    - pipeline, tensor and 
    - you need to know the architecture of the model and the topology of the network
        -> tensor parallism should stay on the same node

# inference

- online/batch inference
    - online inference -> latency
    - batch inference -> throughput

- edge vs HPC/Cloud infernece
    - edge: latency
    - cloud: throughput

solutions
- NVIDEA Jetson -> very compact and power efficient

techniques:
- cell phone, vehicle: low memory
    - quantization (inference accuracy is not impacted) -> cut down memory requirements
- deepspeed: 175B model -> int8 will not fit in the memory
    - deepspeed: zero inference -> leverage the CPU and SSD memory
        - model has many layers - input fades with the layer
        - we sacrifice latencies for the model
- colosalAI: another techniques

triton server:
- complete solution
    - dynamic batching
        - user input is small, but we have many, trainign has large batch sizes
        - will never reach MFLOPS of horse power
        - batch request within 5 sec window
    - fatsre transformer

Main issue with dynamic batching:
- for every word we need to geenrate the output
- if a req comes just after the batch finishes
- concurrent instances -> memory BW constraint
- proposed temporal fusion
    1 model instance -> add the 
- 

# hyper parameter optimization

hyper defined by the user ahead of time
- leanring rate, batch size, epoch, etc
parameters -> estimated during the training 

why do we need to optimize them?
- trial and error -> costly

how does the network look like, optizer

algorithms
- grid search -> tries all combinations, can be done in parallel
- random search -> picky (not based on any info)
- bayesian optimization -> takes previous data into account
    - sequential dependency introduced
- aging evolution -> mutation + crossover
- 

=> deep hyper (implements the hyper parameter optimization)

## open issues



## info

large message collectives:
- MPI has defined 13 collectives
- broadcast


hyper-parameters: a parameter whose value is used to control the 
- learning rate
- batch size
- epoch