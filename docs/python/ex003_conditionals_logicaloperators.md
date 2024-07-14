# conditional

```python
print("Welcone to the rollercoaster")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster")
else:
    print("You can NOT ride the rollercoaster")
```

```python
number = int(input())

if number % 2 == 0:
    print("even")
else:
     print("odd")
 
```

```python
height = float(input())
weight = int(input())
bmi = weight / (height ** height)
if bmi < 18.5:
    print(f"your bmi is {bmi}, you are underweigth")
elif bmi < 25:
    print(f"your bmi is {bmi}, you have a normal weigth")
elif bmi < 30:
    print(f"your bmi is {bmi}, you are slightly ovrweigth")
elif bmi < 35:
    print(f"your bmi is {bmi}, you are obuse")
else:
    print(f"your bmi is {bmi}, you are clinically obuse")
```

## logical operators

and
or
not

```python
a = 15
if a > 15 and a < 13:
    print("between ")
```

```python
name1 = input("Whats your name?")
name2 = input("Whats your name?")
lower_names = (name1 + name2).lower()

t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
r = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))
print(score)
```

## adventure exercise

```python
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcom to Tresure Island")
direction = input("do you want to go l or r? ")
direction_lower = direction.lower()

game_over = False
if direction == "r":
    choice
else:
    print("game over")

if not game_over:
    direction = input("do you want to go l or r? ")



```