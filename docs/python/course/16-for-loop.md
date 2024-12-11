# for loop

- excecute a block of code multiple times (for loops, while loops)
- iterate over a collection

```python
greetings = ['hey', 'hi', 'hello']
language = 'python'

for greeting in greetings:
    # do something
```

- range: immutable sequence of numbers

```python
#range(start, stop, step) ->start is includes, stop is excludes
range(3, 10, 1) # [3,4,5,6,7,8,9]


for i in range(say_hi): # range with 1 parameter uses it as a stop and start=0, step =1
    print('hi')
```