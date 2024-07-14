# data types

string -> string of characters
e.g. "Hello"[0] -> subscrpting

integer

float
e.g. 3.145

boolean
e.g. True, False


## helper type function

print(type(<var>))

## type conversion or casting

str(num_char)
float(123)

## mathematical operations

3 + 5
7 - 4
3 * 2
6 / 3
2 ** 3

PEMDASLR -> order of priorities
Parentheses -> ()
Exponents **
Multiplication, Division: * / -> equal priority
Addition, Substraction + - -> equal priority
left to right

print(3 * 3 + 3 / 3 - 3)

bmi = weight / height ** 2

## round

print(round(8/3, 2))

## division as int

print ( 8 // 3) -> floor division as int type

## shorthands

score +=1
divide = 4 / 2
divide /= 2

## f-String

```python
score = 0
height = 1.8
isWinning = True
print(f"your score is {score}, your height is {height}, winning is {isWinning}")
```

```python
age = input()
years = 90 - int(age)
weeks = years * 52
print(f"you have {weeks} weeks left)
```

## exercise

```python
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15?"))
people = int(input("How many people to split the bill?"))
tip_as_percent = tip / 100
total_tip = bill * tip_as_percent
total_bill = bill + total_tip
bill_per_person = total_bill / people
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay {final_amount}")
```