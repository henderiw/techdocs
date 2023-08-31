#

[go chatbot with llama](https://blog.stackademic.com/creating-a-chatgpt-clone-that-runs-on-your-laptop-with-go-bf9d41f1cf88)

## models

llama.cpp -> llama inference code in C++
Allows to run the model on the laptop

```
./main -m models/llama-2-7b-chat.gguf.q4_K_S.bin --temp 0 \
  -p "The first man on the moon was?"
```

### conversion

virtual environment

```python
pip install torch numpy sentencepiece 
```

```python

python convert-llama-ggmlv3-to-gguf.py -i models/llama-2-7b-chat.ggmlv3.q4_K_S.bin -o models/llama-2-7b-chat.gguf.q4_K_S.bin

python convert-llama-ggmlv3-to-gguf.py -i models/llama-2-13b-chat.ggmlv3.q4_K_S.bin -o models/llama-2-13b-chat.ggufv3.q4__K_S.bin

python convert-llama-ggmlv3-to-gguf.py -i models/llama-2-70b-chat.ggmlv3.q4_1.bin -o models/llama-2-70b-chat.ggufv3.q4_1.bin --gqa 8
```

### quantization

- reduces the number of bits to represent the weights in the transformer models (weigth => floating point)
- can be done during or after training -> PTQ (post training quantization)

PTQ techniques:
- [GPTQ](https://arxiv.org/abs/2210.17323)
- GGML/GGUF: [gguf](https://github.com/philpax/ggml/blob/gguf-spec/docs/gguf.md)

quantization
- FP32: 32 bit
- FP16: 16 bit
- q8_0: 8 bit
- q6_K: 6 bit
- q5_K_S: 5 bit
- q4_K_S: 4 bit
- q3_K_S: 3 bit
- q2_K: 2 bit

areas:
- file size -> GGML/GGUF
- memory -> FP16 -> 16bit -> 2 byte -> 7B -> 7x2 = 14GB
- response time -> 
    memory MAC: 400GB/sec
    memory latency: latency = (2 x no of parameters x no of bytes x batch size)/memory bandwidth
        e.g. 7B in FP16 (2 bytes) -> (2 x 7 x 2 x 1)/400 = 0,07 -> 70 msec
        e.g. 7B in 4 bit (2 bytes) -> (2 x 7 x 0,5 x 1)/400 = 0,07 -> 17,5 msec
    compute power: 26,98 TFLOPS
    compute latency = (2 x no of parameters)/ no of FLOPS
        e.g. 7B (2 x 7)/ 26980 which is 0,52 msec
    
    -> memory constraint -> 70 msec is time it takes to generate 1 token -> 7B FP16 = 14,3 tokens/sec
    -> 


## llama.cpp usage

```
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
LLAMA_METAL=1 make
```

## run the model

./main -m models/llama-2-7b-chat.ggmlv3.q4_K_S.bin -ngl 38 --temp 0 \
  -p "What is the capital of France?"

./main -m models/llama-2-13b-chat.ggmlv3.q4_K_S.bin -ngl 38 --temp 0 \
  -p "What is kubernetes?"

## benchmark

[hellaswag](https://paperswithcode.com/sota/sentence-completion-on-hellaswag)
[mmlu](https://paperswithcode.com/sota/multi-task-language-understanding-on-mmlu)