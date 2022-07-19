# functions

```
fn add(a: i32, b: i32) -> i32 {
    a + b
}

let x = add(1, 1);
let y = add(3, 0);
let z = add(x, 1);
```
- add: name of function
- (): parameters of the function
- ->: return parameters
- return type
- {} => function body

## closure

it is shorter in notation -> easier to read
you can do fn within fn

```
fn add (a: i32, b:i32) > i32 {
    a = b
}

fn main() {
    let sum = add(1, 1);

    let add = !a: i32, b:i32| -> i32 {
        a + b
    };
    // rust compilar can infer the types
    let add = | a, b| a + b;
    let sum add(1, 1);
}
```

## advanced closure

used when we know a predefined set of functions
can take data from outside environment

```
// op is a Box with data type -> closure Fn(i32, i32) -> i32
fn math(a: i32, b: i32, op: Box<dyn Fn(i32, i32) -> i32>) -> i32 {
    op(a, b)
}

fn main() {
    // defines a clossure -> inline function
    let add = |a, b| a + b;
    // we safe the closure in a Box -> Box is a pointer sicne the size
    let add: Box<_> = Box::new(add);
    println!("{}", math(2, 2, add));

    // other representation
    let add = Box::new(move |a, b|) {
        println!("adding a number for {}!", name);
        a + b
    };
    let sub = Box::new(|a, b| a - b);
    let mul = Box::new(|a, b| a * b);
    println!("{}", math(2, 2, add));
    println!("{}", math(2, 2, sub));
    println!("{}", math(2, 2, mul));
}
```

## map combinator

map works with optional data -> can convert the data

fn maybe_num() -> Option<i32> {
    ...
}

fn main() {
    let plus_one = match maybe_num() {
        Some(num) => Some(num+1),
        None => None,
    }

    // code reduced to the following
    // map is a method on option
    // map only applies if there is a value -> the code does not run
    let plus_one = maybe_num().map(|num| num + 1);

    // map combinator can convert the type (from String to i32)
    let word_length: Option<i32> = maybe_word()
        .map(]word| word.len());

    // map can be chained
    let word_length: Option<i32> = maybe_word()
        .map(|word| word.len())
        .map(|len| len * 2);

}

exercise a21