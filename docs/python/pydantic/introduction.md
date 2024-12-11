


## date and time

## list

## dict

## sets, tuple

## union

## optional, defaults

## uuid

## immutability

## additional properties

-> extra paraemeters are not blocked but forgotten by pydantic

class Config:
    extra = "ignore"

## enums

## literal

better performance, alternative to enums
enum is more extensible than literal

## custom validation

```python
from pydantic import field_validator
```

## model validation

```python
from pydantic import model_validation
```

## error messages

## serialization

transform a model to something that can be stored or send

-> json
-> xml
-> csv
-> dict

## include/exclude

```python
print("model json",course.model_dump_json(indent=2, include=["department", "course_number"]))
```

exclude_unset
exclude_defaults

## schema

