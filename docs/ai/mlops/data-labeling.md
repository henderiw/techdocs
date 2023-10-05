## data labeling

humansignal.com
- chris hoge
- Nikolai Liubimov
- Michael Malyuk

moderator: Nishikant Dhanuka (Amsterdam)

Best data is human labeled data, but
- expensive -> need for automation
RLHF (human feedback)

option1: use prompt to classify -> need to verify
- prompt => task -> predicted label -> verify -> 

constrained generation -> output {{ select options = ['Objective', 'Subjective']}}
-> python import guidance

option2:
- prompt -> dataset -> predict label -> verify -> ground truth dataset -> adjust the prompt
-> expensive wrt to adjusting the prompt
- few-shot prompting (examples how we do annotations)
- chain of thought -> prompt (describe reasining step by step)
- self-consistency -> multiple answers

option 3: improve quality/automatically optimize
- initial prompt -> evaluate (against ground trutch label) -> refine best prompt


