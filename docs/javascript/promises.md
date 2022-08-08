# javascript promises

Promises are objects that represent the eventual outcome of an asynchronous operation.

- pending
- fullfilled: onResolve(param)
- rejected: onRejetc(reaason)

We refer to a promise as settled if it is no longer pending

- timeout: setTimeout() is a Node function which delays the execution of a callback function using the event-loop
- use .then() with a success handler callback containing the logic for what should happen if a promise resolves.
- use .catch() with a failure handler callback containing the logic for what should happen if a promise rejects.
- composition enables us to write complex, asynchronous code that’s still readable. We do this by chaining multiple .then()‘s and .catch()‘s -> order maters
  - To use promise composition correctly, we have to remember to return promises constructed within a .then().
- promise.all: all promisees need to complete -> order does not matter
    - input is an array

## constructing a promise

```
const inventory = {
  sunglasses: 1900,
  pants: 1088,
  bags: 1344
};

// Write your code below:
const myExecutor = (resolve, reject) => {
  if (inventory.sunglasses > 1) {
    resolve('Sunglasses order processed.')
  } else {
    reject('That item is sold out.')
  }
}
const orderSunglasses = () => {
  return new Promise(myExecutor);
} 

const orderPromise = orderSunglasses()

console.log(orderPromise)
```

- promise takes an executor function as input
- the executor function has 2 function parameters
  - resolve()
  - reject()

## consume promises

```
let prom = new Promise((resolve, reject) => {
  let num = Math.random();
  if (num < .5 ){
    resolve('Yay!');
  } else {
    reject('Ohhh noooo!');
  }
});
 
const handleSuccess = (resolvedValue) => {
  console.log(resolvedValue);
};
 
const handleFailure = (rejectionReason) => {
  console.log(rejectionReason);
};
 
prom.then(handleSuccess, handleFailure);
```

- prom is a promise that will resolve to either 'Yay' or 'Ohhh noooo!'
- We pass two handler functions to .then(). The first will be invoked with 'Yay!' if the promise resolves, and the second will be invoked with 'Ohhh noooo!' if the promise rejects.


### catch

seperates success from failure

```
// Write your code below:
checkInventory(order)
  .then(handleSuccess)
  .catch(handleFailure)
```

### chaining promises

```
checkInventory(order)
    .then((resolvedValueArray) => {
        return processPayment(resolvedValueArray)
    })
    .then((resolvedValueArray) => {
        return shipOrder(resolvedValueArray)
    })
    .then((successMessage) => {
        console.log(successMessage);
    });
```

### promis.all

```
let myPromises = Promise.all([returnsPromOne(), returnsPromTwo(), returnsPromThree()]);
 
myPromises
  .then((arrayOfValues) => {
    console.log(arrayOfValues);
  })
  .catch((rejectionReason) => {
    console.log(rejectionReason);
  });
```

example

```
const {checkAvailability} = require('./library.js');

const onFulfill = (itemsArray) => {
  console.log(`Items checked: ${itemsArray}`);
  console.log(`Every item was available from the distributor. Placing order now.`);
};

const onReject = (rejectionReason) => {
	console.log(rejectionReason);
};

// Write your code below:
let checkSunglasses = checkAvailability('sunglasses', 'Favorite Supply Co.')
let checkPants = checkAvailability('pants', 'Favorite Supply Co.')
let checkBags = checkAvailability('bags', 'Favorite Supply Co.')

 Promise.all([checkSunglasses, checkPants, checkBags])
  .then(onFulfill)
  .catch(onReject);
```