# break and continue

- break: exists out of the loop
- continue: skip an iteration


```python
for greeting in greetings:
    if greeting == "stop": break
    print(greeting)
```

```python
for greeting in greetings:
    if len(greeting) > 11: continue
    print(greeting)
```