# javascript async wait

- async keywaord is used to write functions that handle asynchronous actions
- async functions return a promise
- async return in 1 of 3 ways:
  - if nothing is returned from the fn, it will return a promise with a resolved value of undefined
  - if there a non-promise value returns from the fn, it will return a promise resolved to that value
  - if a promise is returned from the fn, it will simply treturn that promise

- await: 
  - can only be used inside an aync function
  - await is an operator: it returns the resolved value of the promise
  - await halts or puses, the execution of our async function until a given promise is resolved

```
async function myFunc() {
    // function body
};

myFync();
```

alternative syntax

```
const myFunc = async () => {

}

myFunc();
```

## async example

```
async function withAsync(num) {
  if (num === 0) {
    return 'zero'
  } else {
    return 'not zero'
  }
}

withAsync(0)
  .then((resolveValue) => {
  console.log(` withConstructor(0) returned a promise which resolved to: ${resolveValue}.`);
});
```

## await example

```
async function asyncFuncExample(){
  let resolvedValue = await myPromise();
  console.log(resolvedValue);
}
 
asyncFuncExample();
```

example

```
const brainstormDinner = require('./library.js');


// Native promise version:
function nativePromiseDinner() {
  brainstormDinner().then((meal) => {
	  console.log(`I'm going to make ${meal} for dinner.`);
  });
}


// async/await version:
async function announceDinner() {
  // Write your code below:
  let meal = await brainstormDinner();
  console.log(`I'm going to make ${meal} for dinner.`);
}

announceDinner()
```

```
async function getBeans() {
  console.log(`1. Heading to the store to buy beans...`);
  let value = await shopForBeans();
  console.log(`3. Great! I'm making ${value} beans for dinner tonight!`);
}

getBeans();
```

## chaining async

```
async function asyncAwaitVersion() {
  let firstValue = await returnsFirstPromise();
  console.log(firstValue);
  let secondValue = await returnsSecondPromise(firstValue);
  console.log(secondValue);
}
```

```
const {shopForBeans, soakTheBeans, cookTheBeans} = require('./library.js');

// Write your code below:
async function makeBeans() {
  let type = await shopForBeans()
}

async function isSoft(type) {
  let isSoft = await soakTheBeans(type)
}

async function dinner(isSoft) {
  let dinner = await cookTheBeans(isSoft)
}

console.log(dinner)
makeBeans()
```

## error handling

```
async function usingTryCatch() {
 try {
   let resolveValue = await asyncFunction('thing that will fail');
   let secondValue = await secondAsyncFunction(resolveValue);
 } catch (err) {
   // Catches any errors in the try block
   console.log(err);
 }
}
 
usingTryCatch();
```

```
const cookBeanSouffle = require('./library.js');

// Write your code below:
async function hostDinnerParty() {
  try {
    let x = await cookBeanSouffle();
    console.log(`${x} is served!`)
  } catch(error) {
    console.log(error)
    console.log('Ordering a pizza!')
  }
}

hostDinnerParty()
```

## await concurrent

let {cookBeans, steamBroccoli, cookRice, bakeChicken} = require('./library.js');

// Write your code below:
async function serveDinner() {
  let vegetablePromise = steamBroccoli()
  let starchPromise = cookRice()
  let proteinPromise = bakeChicken()
  let sidePromise = cookBeans()

  console.log(`Dinner is served. We're having ${await vegetablePromise}, ${await starchPromise}, ${await proteinPromise}, and ${await sidePromise}.`)
}

serveDinner()

## await promis.all()

```
async function asyncPromAll() {
  const resultArray = await Promise.all([asyncTask1(), asyncTask2(), asyncTask3(), asyncTask4()]);
  for (let i = 0; i<resultArray.length; i++){
    console.log(resultArray[i]); 
  }
}
```

example

```
let {cookBeans, steamBroccoli, cookRice, bakeChicken} = require('./library.js');

// Write your code below:

async function serveDinnerAgain() {
  const foodArray = await Promise.all([steamBroccoli(), cookRice(), bakeChicken(), cookBeans()]);

  let vegetable = foodArray[0];
  let starch =  foodArray[1];
  let protein =  foodArray[2];
  let side =  foodArray[3];
  
  console.log(`Dinner is served. We're having ${vegetable}, ${starch}, ${protein}, and ${side}.`);
}
serveDinnerAgain()
```