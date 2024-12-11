# lists methods or functions

builtin functions

```python
ages = [23, 29, 12, 12.1]


# functions
max(ages) # 39
min(ages) # 12
len(ages) # 4
sorted(ages) # [12, 12.1, 23, 29]
sorted(ages, reverted) # [29, 23, 12.1, 12]

# methods -> function bound to a given object

ages.append(24)
ages.pop(-1) # remove last index and return the element
ages.remove(24) # remove by item value

"*".join(["wim", "hans", "markus"])

```

