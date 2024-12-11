# dictionaries

- mutable, unordered container of key, value pairs

```python
scores = {"Wim": 94, "Hans": 100, "Markus": 88}
## accessing data
scores["wim"] # 94
scores.get("andy")

## add
scores["tom"] = 69

## delete
scores.pop("wim") # value of the key is removed
```

Key, Value can be any object and within the dict they can also be any type, so they can be mixed in the same dict.
-> key should be an immutable data type

```python
scores = {
    "Wim": 94, # int
    "Jessica": {96, 22, 33}, # list
    "tom": { # dict
        "bio" = 94,
        "phys" = 79,
    }
}

# methods

scores.keys() # data types dict_keys
scores.values() # data types dict_values
scores.items() # collection of k, v as tuples
```