# lambdas

- anonymous functions: don't have a name

```python

# parameters is x
# returns are not needed
lambda x: x ** 3

# how do we invoke it
# option1 not the right way
cube_it = lambda x: x ** 3
cube_it(20)

# options2
list(map(lambda x: x ** 3), numbers)
```