# prompt engineering

[advanced prompt engineering](https://towardsdatascience.com/advanced-prompt-engineering-f07f9e55fe01)

## zero shot learning

1. task description
2. prompt

Examples:

classification
- task: classify the following sentence as either funny or not funny
- prompt: <text>
- output: <funny | not funny>

Math
- task: solve the following addition problem
- prompt: <3 + 5>
- output: the answer is 8

Translate
- task: translate the following sentense
- prompt: <text>
- output: <translated text>

## few shot learning

augment the prompt with high quality input/output examples

## next step

- allow an LLM to access and external knowledge base
- enable comples, reasoning based problems to be solved
- provide unlimited memory to an LLM by allowing the model to store and access prior informatiion from a conversation

## overview

minI(input) -> maxR(output)

d(T) = dialogue with transformers
d(T) = minI(prompt) -> maxR(response)

if the context is not clear the chances of a good response is small