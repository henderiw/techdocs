# inference

prompting phase
- initial text
- compute BW

token phase
- predict the enxt word
- memory bound


apps:
- chat: token heavy
- summary/translation: prompt heavy

KV caching:
- how to program the accelerator
- used during token (mem lookup of prior phase)