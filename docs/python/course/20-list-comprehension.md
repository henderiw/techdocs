# list comprehensions


```python
numbers =[10,2 ,4, 12, 13, 1, 712, 23, 2, 192]

studnets = [
    {"name": "wim", "score": 90},
    {"name": "hans", "score": 99},
    {"name": "markus", "score": 95},
]

odds = []
for number in numbers:
    if number % 2 == 1:
        odds.append(number)

# list comprehensions
# syntax
# [element for element in iterables]

[number for number in numbers if number % 2 == 1] # list provides the odd numbers only

[student.get("name") for student in students if student.get("score") >= 90] # only students with score is bigger than 90
```