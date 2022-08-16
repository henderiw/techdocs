# javascript descrutering

easily extract array element or object properties and store them in variables

## array destructuring

[a, b] = ['Hello', 'Max]
console.log(a) // Hello
console.log(b) // Max

const numbers = [1, 2, 3];
[num1, , num3] = numbers;
console.log(num1, num3);

## object destructuring

{name} = {name: 'Max', age: 28}
console.log(name) // Max
console.log(age) // undefined

