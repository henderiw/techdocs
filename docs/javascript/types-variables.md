# javascript

## logging

console.log()

## data types

- Number
- String: '' or ""
- Boolean
- Null: null -> absence of a value
- Undefined: undefined -> a given value does not exist
- symbol
- objet: collection of related data

boolean, number, string -> primitive types (copy)
array, object -> reference type (pointer) 

const person = {
  name: 'Max'
}

// copy the object iso referecning them
const secondPerson = {
  ...person
}

## methods

[dev environment](https://jsbin.com/?js,output)

[js string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)
[built in](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects)

## variables

-> use let iso var
-> const for immutable

### variables
```
var favoriteFood = 'pizza';
var numOfSlices = 8;
console.log(favoriteFood);
console.log(numOfSlices);
```

### modifiable variables

let allows to change the variable

```
let changeMe = true;
changeMe = false;
console.log(changeMe);
```

### const

const entree='Enchiladas';
console.log(entree);

### template literal

uses backticks

let myName='Wim';
let myCity='San Francisco';
console.log(`My name is ${myName}. My favorite city is ${myCity}.`)

### typeof

let newVariable = 'Playing around with typeof.';
console.log(typeof newVariable);
newVariable = 1;
console.log(typeof newVariable);

## arrays

let concepts = ['creating arrays', 'array structures', 'array manipulation'];

we can ressagn an entry in an arry even if it is a const definition, but we cannot remap the const to a different array

```
const objectives = ['Learn a new language', 'Read 52 books', 'Run a marathon'];
console.log(objectives.length)
```

methods:
- length
- push
- pop
- shift
- slice[1,4]
- indexOf('pasta')

[array methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)

### array forEach

```
const fruits = ['mango', 'papaya', 'pineapple', 'apple'];

// Iterate over fruits below
fruits.forEach(fruit => console.log(`I want to eat a ${fruit}.`))
```

### array map

creates a new array

```
const numbers = [1, 2, 3, 4, 5]; 
 
const bigNumbers = numbers.map(number => {
  return number * 10;
});
```

```
const animals = ['Hen', 'elephant', 'llama', 'leopard', 'ostrich', 'Whale', 'octopus', 'rabbit', 'lion', 'dog'];

// Create the secretMessage array below
const secretMessage = animals.map(animal => {
  return animal[0]
})

console.log(secretMessage.join(''));

const bigNumbers = [100, 200, 300, 400, 500];

// Create the smallNumbers array below
const smallNumbers = bigNumbers.map(num => {
  return num/100
})
console.log(smallNumbers);
```

## array filter

const randomNumbers = [375, 200, 3.14, 7, 13, 852];

// Call .filter() on randomNumbers below
const smallNumbers = randomNumbers.filter(num => {
  return num < 250
})

console.log(smallNumbers)

const favoriteWords = ['nostalgia', 'hyperbole', 'fervent', 'esoteric', 'serene'];


// Call .filter() on favoriteWords below
const longFavoriteWords = favoriteWords.filter(word => {
  return word.length > 7
})

console.log(longFavoriteWords)

### array findIndex method

const animals = ['hippo', 'tiger', 'lion', 'seal', 'cheetah', 'monkey', 'salamander', 'elephant'];

const foundAnimal = animals.findIndex(animal => {
  return animal === 'elephant'
})

const startsWithS = animals.findIndex(animal => {
  return animal[0] === 's'
})

### array reduce method

```
const newNumbers = [1, 3, 5, 7];

const newSum = newNumbers.reduce((accumulator, currentValue) => {
  console.log('The value of accumulator: ', accumulator);
  console.log('The value of currentValue: ', currentValue);
  return accumulator + currentValue;
})

console.log(newSum)
```

```
The value of accumulator:  1
The value of currentValue:  3
The value of accumulator:  4
The value of currentValue:  5
The value of accumulator:  9
The value of currentValue:  7
16
```

```
const newNumbers = [1, 3, 5, 7];

const newSum = newNumbers.reduce((accumulator, currentValue) => {
  console.log('The value of accumulator: ', accumulator);
  console.log('The value of currentValue: ', currentValue);
  return accumulator + currentValue;
}, 10);

console.log(newSum)
```

### array iterator doc

[array iterator doc](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#Iteration_methods)

## objects

```
let spaceship = {
  homePlanet: 'Earth',
  color: 'silver',
  'Fuel Type': 'Turbo Fuel',
  numCrew: 5,
  flightPath: ['Venus', 'Mars', 'Saturn']
};

// Write your code below
let crewCount = spaceship.numCrew
let planetArray = spaceship.flightPath
```

### access object with bracket notation

```
let spaceship = {
  'Fuel Type' : 'Turbo Fuel',
  'Active Mission' : true,
  homePlanet : 'Earth', 
  numCrew: 5
 };

let propName =  'Active Mission';

// Write your code below
let isActive = spaceship[propName]
console.log(isActive)
```

### manipulate object at runtime

```
let spaceship = {
  'Fuel Type' : 'Turbo Fuel',
  homePlanet : 'Earth',
  color: 'silver',
  'Secret Mission' : 'Discover life outside of Earth.'
};

// Write your code below
spaceship.color = 'glorious gold'
spaceship.numEngines = 6
delete spaceship['Secret Mission']
```

### function parameters in objects

```
let retreatMessage = 'We no longer wish to conquer your planet. It is full of dogs, which we do not care for.';

// Write your code below

let alienShip = {
  retreat() {
    console.log(retreatMessage)
  },
  takeOff() {
    console.log('Spim... Borp... Glix... Blastoff!')
  }
};

alienShip.retreat();

alienShip.takeOff();
```

### object for..in

```
let spaceship = {
    crew: {
    captain: { 
        name: 'Lily', 
        degree: 'Computer Engineering', 
        cheerTeam() { console.log('You got this!') } 
        },
    'chief officer': { 
        name: 'Dan', 
        degree: 'Aerospace Engineering', 
        agree() { console.log('I agree, captain!') } 
        },
    medic: { 
        name: 'Clementine', 
        degree: 'Physics', 
        announce() { console.log(`Jets on!`) } },
    translator: {
        name: 'Shauna', 
        degree: 'Conservation Science', 
        powerFuel() { console.log('The tank is full!') } 
        }
    }
}; 

// Write your code below
for (let crewMember in spaceship.crew) {
  console.log(`${crewMember}: ${spaceship.crew[crewMember].name}`);
}

for (let crewMember in spaceship.crew) {
  console.log(`${spaceship.crew[crewMember].name}: ${spaceship.crew[crewMember].degree}`);
}
```

## objects this

```
const robot = {
  model: '1E78V2',
  energyLevel: 100,
  provideInfo() {
    return `I am ${this.model} and my current energy level is ${this.energyLevel}.`
  }
};

console.log(robot.provideInfo())
```

## getters and private objects

```
const robot = {
  _model: '1E78V2',
  _energyLevel: 100,
  get energyLevel() {
    if (typeof this._energyLevel === 'number') {
      return `My current energy level is ${this._energyLevel}`
    } else {
      return `System malfunction: cannot retrieve energy level`
    }
  }
};

console.log(robot.energyLevel)
```

## setters

```
const robot = {
  _model: '1E78V2',
  _energyLevel: 100,
  _numOfSensors: 15,
  get numOfSensors(){
    if(typeof this._numOfSensors === 'number'){
      return this._numOfSensors;
    } else {
      return 'Sensors are currently down.'
    }
  },
  set numOfSensors(num){
    if (typeof num === 'number' && num >= 0) {
      this._numOfSensors = num
    } else {
      return 'Pass in a number that is greater than or equal to 0'
    }
  }
};

console.log(robot.numOfSensors) // 15
robot.numOfSensors = 100
console.log(robot.numOfSensors) // 100
```

### object factory

allows to create multiple object quikly

```
const robotFactory = (model, mobile) => {
  return { 
    model: model,
    mobile: mobile,
    beep() {
      console.log('Beep Boop')
    }
  }
};

const tinCan = robotFactory('P-500', true);
tinCan.beep(); 
```

shortcut

```
const robot = {
  model: '1E78V2',
  energyLevel: 100,
  functionality: {
    beep() {
      console.log('Beep Boop');
    },
    fireLaser() {
      console.log('Pew Pew');
    },
  }
};

const { functionality } = robot;

functionality.beep()
```

### object methods

```
const robot = {
	model: 'SAL-1000',
  mobile: true,
  sentient: false,
  armor: 'Steel-plated',
  energyLevel: 75
};

// What is missing in the following method call?
const robotKeys = Object.keys(robot);

console.log(robotKeys);

// Declare robotEntries below this line:
const robotEntries = Object.entries(robot);

console.log(robotEntries);

// Declare newRobot below this line:
const newRobot = Object.assign(
  {laserBlaster: true, voiceRecognition: true}
)

console.log(newRobot);
```