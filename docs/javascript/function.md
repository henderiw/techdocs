# javascript functions

## function

```
greetWorld(); // Output: Hello, World!
 
function greetWorld() {
  console.log('Hello, World!');
}
```

```
function sayThanks(name) {
  console.log('Thank you for your purchase '+ name + '! We appreciate your business.');
}

sayThanks('Cole')
```

## function expression

```
const plantNeedsWater = function(day){
  if (day === 'Wednesday') {
    return true;
  } else {
    return false;
  }
}
```

## arrow functions

avoids writing function every time
no more issues with the this keyword -> this is always

```
const plantNeedsWater = (day) => {
  if (day === 'Wednesday') {
    return true;
  } else {
    return false;
  }
}
```

## concise body arrow function

```
const plantNeedsWater = (day) => {
  return day === 'Wednesday' ? true : false;
};
```

```
const plantNeedsWater = day => day === 'Wednesday' ? true : false
```

## function as data

fucntions can be assigned to variables

```
const checkThatTwoPlusTwoEqualsFourAMillionTimes = () => {
  for(let i = 1; i <= 1000000; i++) {
    if ( (2 + 2) != 4) {
      console.log('Something has gone very wrong :( ');
    }
  }
};

// Write your code below
const isTwoPlusTwo = checkThatTwoPlusTwoEqualsFourAMillionTimes

isTwoPlusTwo()
console.log(isTwoPlusTwo.name)
```

## function as parameters

```
const addTwo = num => {
  return num + 2;
}

const checkConsistentOutput = (func, val) => {
  let checkA = val + 2
  let checkB = func(val)

  if (checkA == checkB) {
    return checkB
  } else {
    return 'inconsistent results'
  }
}

console.log(checkConsistentOutput(addTwo, 5));
```