# goal

with respect the questions here is what i am thinking.

What we want is this.
- input: high level business intent. e.g. can you deploy a cluster on google (not sure we have to specify the region) -> this could be an interaction potentially but lets not go there yet.
- output: kubectl command or CR/KRM resource to make this happen. I assume KCC for now

So the real q is how do you go about this?

option1: prompt based
- you specify a prompt with some template -> we could generate this template before -> se we dynamically add the template on top of the prompt before sending the foundational model.

option 2: Embedding based. we use a foundational model as is We generate the example based on embeddings we generated from examples. I believe we should build a tokenizer here specialised on our use case to find the relevant examples.

- the examples get generated from blueprint designs and we can also use the CRD schema(s) as input to the vector DB.
- now here we have schema that actually allow us to teach the model what all the potential parameters are so how do provide this to the model or we don't care.

Option 3. fine tuning a model based on the examples and we just interact with the fine tuned model.

Option 4. generate a new model -> least preferred as this will take resources and time.
