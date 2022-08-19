# typescript

## basic types

Primitives: number, string, boolean

```
let age: number = 24;
let userName: string;
let isInstructor: boolean = true;
```

-> null  and undefined are possible but cannot be changed so this does not make sense to use like this

More complex types: array, objects

```
let hobbies: string[] = ['Sports', 'Cooking'];
// type asignment -> object type definition
let person: {
    name: string;
    age: number;
};

person = {
    name: 'Max',
    age: 32,
}

// array of objects
let people: {
    name: string;
    age: number;
}[];
```

-> any type should not be used

### type inference

// infered type
let course = 'eact - the complet guide'
// this changes the type fro string to number and this is an error
course = 1234;

### unions

multiple types e.g. string and number could eb allowed

```
let course: string | number =  'React - the bla'
course = 12345;
```

### type aliases

```
type Person = {
    name: string;
    age: number;
};

let people: Person[];
```

## Function types

```
function add(a: number, b: number): number {
    // return type is infered -. above we now explicitly define this
    return a + b
}

// return nothing -> this is :void or undefined
function printOutput(value: any) {
    console.log(value);
}
```

## Generics

// with the T is going to be the type T bot both values
function inserAtBeginning<T>(array: T[], value: T) {
    const newArray = [value, ...array];
    return newArray;
}

const demoArray = [1,2,3]
const updatedArray = inserAtBeginning(demoArray, -1)
const stringArray = inserAtBeginning(['a', 'b'], 'c')

```
Generic Types ("Generics") can be tricky to wrap your head around.

But indeed, we are working with them all the time - one of the most prominent examples is an array.

Consider this example array:

let numbers = [1, 2, 3];
Here, the type is inferred, but if we would assign it explicitly, we could do it like this:

let numbers: number[] = [1, 2, 3];
number[] is the TypeScript notation for saying "this is an array of numbers".

But actually, number[] is just syntactic sugar!

The actual type is Array. ALL arrays are of the Array type.

BUT: Since an array type really only makes sense if we also describe the type of items in the array, Array actually is a generic type.

You could also write the above example liks this:

let numbers: Array<number> = [1, 2, 3];
Here we have the angle brackets (<>) again! But this time NOT to create our own type (as we did it in the previous lecture) but instead to tell TypeScript which actual type should be used for the "generic type placeholder" (T in the previous lecture).

Just as shown in the last lecture, TypeScript would be able to infer this as well - we rely on that when we just write:

let numbers = [1, 2, 3];
But if we want to explicitly set a type, we could do it like this:

let numbers: Array<number> = [1, 2, 3];
Of course it can be a bit annoying to write this rather long and clunky type, that's why we have this alternative (syntactic sugar) for arrays:

let numbers: number[] = [1, 2, 3];
If we take the example from the previous lecture, we could've also set the concrete type for our placeholder T explicitly:

const stringArray = insertAtBeginning<string>(['a', 'b', 'c'], 'd');
So we can not just use the angle brackets to define a generic type but also to USE a generic type and explicitly set the placeholder type that should be used - sometimes this is required if TypeScript is not able to infer the (correct) type. We'll see this later in this course section
```