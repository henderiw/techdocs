# javascript classes

blueprint or objects
-> properties
-> methods

more convenient way to do constructor function

## class

```
class Dog {
  constructor(name) {
    this._name = name;
    this._behavior = 0;
  }

  get name() {
    return this._name;
  }
  get behavior() {
    return this._behavior;
  }   

  incrementBehavior() {
    this._behavior ++;
  }
}

const halley = new Dog('Halley');
console.log(halley.name); // Print name value to console
console.log(halley.behavior); // Print behavior value to console
halley.incrementBehavior(); // Add one to behavior
console.log(halley.name); // Print name value to console
console.log(halley.behavior); // Print behavior value to console
```

-> constructor called on every instance
-> classes upper camelcase

## inheritance

-> extends
-> super

```
class HospitalEmployee {
  constructor(name) {
    super();
    this._name = name;
    this._remainingVacationDays = 20;
  }
  
  get name() {
    return this._name;
  }
  
  get remainingVacationDays() {
    return this._remainingVacationDays;
  }
  
  takeVacationDays(daysOff) {
    this._remainingVacationDays -= daysOff;
  }

  static generatePassword() {
    return Math.floor(Math.random() * 10000)
  }
}

class Nurse extends HospitalEmployee {
  constructor(name, certifications) {
    super(name);
    this._certifications = certifications;
  } 
  
  get certifications() {
    return this._certifications;
  }
  
  addCertification(newCertification) {
    this.certifications.push(newCertification);
  }
}

const nurseOlynyk = new Nurse('Olynyk', ['Trauma','Pediatrics']);
nurseOlynyk.takeVacationDays(5);
console.log(nurseOlynyk.remainingVacationDays);
nurseOlynyk.addCertification('Genetics');
console.log(nurseOlynyk.certifications);
```

## modern syntax

skip constructor function for properties
arrow function for functions in a class -> no issues with the this keyword

### properties

ES6

constructor() {
  this.myProperty = 'value'
}

ES7

myProperty = 'value'

### functions

ES6

myMethod() {...}

ES7

myMethod = () => {...}

### example

S6/Babel

class Human {
  gender = 'male'

  printGender = () => {
    console.log(this.gender)
  }
}

class Person extends Human {
  name = 'Max'
  gender = 'female'

  printMyName = () => {
    console.log(this.name)
  }
}

const person = new Person();
person.printMyName();
person.printGender();