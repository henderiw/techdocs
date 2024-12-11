# ai workshop

LLM: gpt-4o-mini
langchain -> agents (ReAct- reasoning and acting), prompt templates, data augmentation
streaamlit: webUI (python)

flow:
1. prompt template (augment the scripts with some context)
2. prompt
3. LLM
4. thought
5. action
6. execution
7. observation
8. loop until final answer or max trials

Prompt template:
- Header
- tools: tools names, description and arguments
- how to specify the tool
- format: format response: thoughts, action, observations
- additional instructions: avoid loops
- human query
- scratchpad: thoughts, actions, pbservation

perplexity