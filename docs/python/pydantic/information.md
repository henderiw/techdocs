# what is it

framework for defining specialized python classes

- class attributes -> called fields
- specialized class -> called model

simple way to load data from a dictionaty or JSON in a model
    - model instances
    - deserializng/serializng

validate data during deserialization

work with data in an OOP manner

model = class
field language -> string, 1 char min
field version -> must be a string, pattern x.x.x
field year -> must be an integer >= 2000

JSON -- (deserialization) -> model -> (validation) -> (serialize) -> JSON

## pydantic vs data classes

both are python classes
both provide a declarative way for properties

pydantic adds serialization/deserialization
pydantic adds simpler validation

```python
@dataclass
class Model:
    lanuage: str
    version: str
    year: int
```
-> code generator

```python
from pydantic import BaseModel

class Model(BaseModel):
    lanuage: str
    version: str
    year: int
```
-> uses inheritance to add functionality by inheriting from the object class

```python
Model(language='Python', version='3.2.1', year=2020)

#pydantic only
Model.model.validate(
    {
        "language": 'Python'
    }
)

```

## create

```python
from pydantic import BaseModel

class Person(BaseModel):
    first_name: str
    last_name: str
    age: int

p = Person(first_name="Wim", last_name="Henderickx", age=20)

str(p)

repr(p)

p.model_fields
#-> required True
```