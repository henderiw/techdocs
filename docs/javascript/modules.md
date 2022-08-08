# javascript modules

## what

modules are: 
- reusable pieces of code in a file 
- that can be exported 
- that can be imported for use in another file. 

A modular program is one whose components can be separated, used individually, and recombined to create a complex system.

## modules in node

### export module

/* shape-area.js */

```
const PI = Math.PI;

// Define and export circleArea() and squareArea() below
module.exports.circleArea = function(radiusLength) {
  return PI * radius * radius;
};

module.exports.squareArea = function(sideLength) {
  return sideLength * sideLength;
};
```

or 

```
module.exports = squareArea;
```

### import -> require()

```
/* app.js */ 

const radius = 5;
const sideLength = 10;

// Option 1: import the entire shape-area.js module here.
// const areaFunctions = require('./shape-area.js');

// Option 2: import circleArea and squareArea with object destructuring

const { circleArea, squareArea } = require("./shape-area.js")

// use the imported .circleArea() and .squareArea() methods here

const areaOfCircle = circleArea(radius);
const areaOfSquare = squareArea(sideLength);
console.log(areaOfCircle)
console.log(areaOfSquare)
```

## implementing module in browser

### html files

```
<!-- secret-messages.html --> 
<html>
  <head>
    <title>Secret Messages</title>
  </head>
  <body>
    <button id="secret-button"> Press me... if you dare </button>
    <p id="secret-p" style="display: none"> Modules are fancy! </p>
    <script type="module" src="./secret-messages.js"> </script>
  </body>
</html>
```

- The secret-messages.html page renders a button element and a hidden paragraph element.
- It then loads the script secret-messages.js using the file path "./secret-messages.js". 
- module is used to reference an imported function

#### import js files

named imports

```
/* secret-messages.js */
import { toggleHiddenElement, changeToFunkyColor } from '../modules/dom-functions.js';
 
const buttonElement = document.getElementById('secret-button');
const pElement = document.getElementById('secret-p');
 
buttonElement.addEventListener('click', () => {
  toggleHiddenElement(pElement);
  changeToFunkyColor(buttonElement);
});
```

- In secret-messages.js, the functions toggleHiddenElement() and changeToFunkyColor() are imported from the module ../modules/dom-functions.js. The ../ indicates that the modules/ folder is in the same folder as the parent folder, secret-messages/.
- When the button is clicked, the now imported toggleHiddenElement() function is called with pElement as an argument.
- In addition, changeToFunkyColor() is called with buttonElement as an argument, changing its background color to a random one!


##### rename input to avoid collision of the name

alias

```
import { greet as greetEspanol } from 'greeterEspanol.js';
import { greet as greetFrancais } from 'greeterFrancais.js';
```

```
import * as bundled from 'greeterEspanol.js'
```

### export js file

```
/* dom-functions.js */
const toggleHiddenElement = (domElement) => {
    if (domElement.style.display === 'none') {
      domElement.style.display = 'block';
    } else {
      domElement.style.display = 'none';
    }
}
 
const changeToFunkyColor = (domElement) => {
  const r = Math.random() * 255;
  const g = Math.random() * 255;
  const b = Math.random() * 255;
 
  domElement.style.background = `rgb(${r}, ${g}, ${b})`;
}
 
export { toggleHiddenElement, changeToFunkyColor };
```

alternative syntax export per function

```
export const toggleHiddenElement = (domElement) => {
  // logic omitted...
}
 
export const changeToFunkyColor = (domElement) => {
  // logic omitted...
}
```

- The function toggleHiddenElement() is declared. It accepts a domElement as an input and either shows or hides that element depending on its current display style value.
- A new function changeToFunkyColor() is declared. It accepts a domElement as an input and then sets its background color to a random rgb() color value.
- The two functions are exported using the ES6 export statement.


### default export

- the default export value is an object containing the entire set of functions and/or data values of a module.

export

```
const resources = { 
  valueA, 
  valueB 
}
export { resources as default };
/// export default resources;
```

import

```
import importedResources from 'module.js';
// shortcut for import { default as importedResources } from 'module.js 
```

#### default example

export

default is exporting all the function as an object instead

```
/* dom-functions.js */
const toggleHiddenElement = (domElement) => {
    if (domElement.style.display === 'none') {
      domElement.style.display = 'block';
    } else {
      domElement.style.display = 'none';
    }
}
 
const changeToFunkyColor = (domElement) => {
  const r = Math.random() * 255;
  const g = Math.random() * 255;
  const b = Math.random() * 255;
 
  domElement.style.background = `rgb(${r}, ${g}, ${b})`;
}
 
const resources = { 
  toggleHiddenElement, 
  changeToFunkyColor
}
export default resources;
```

import

```
import domFunctions from '../modules/dom-functions.js';
 
const { toggleHiddenElement, changeToFunkyColor } = domFunctions;
 
const buttonElement = document.getElementById('secret-button');
const pElement = document.getElementById('secret-p');
 
buttonElement.addEventListener('click', () => {
  toggleHiddenElement(pElement);
  changeToFunkyColor(buttonElement);
});
```