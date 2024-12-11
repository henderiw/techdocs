# sets

unordered container of unique values


```python
countries = {"US", "BE", "NL"}

# methods
countries.add("DE")
countries.discard("US")

# methods operators -> fast operations

countries1 = {"US", "BE", "NL"}
countries2 = {"US", "BE", "DE"}

countries1.intersection(countries2) #  {"US", "BE"}
countries1.union(countries2) #  {"US", "BE", "NL", "DE}
countries1.difference(countries2) # {"NL"}
countries2.difference(countries1) # {"DE"}


# task remove all the unique elements from a list of degress

highest_degree_earned = ['BA', 'BA', 'BA', 'Phd']
# convert list to set
set(highest_degree_earned) # only retains the unique values
```
