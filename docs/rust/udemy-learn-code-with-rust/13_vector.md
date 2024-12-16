# vector 

[vector](https://doc.rust-lang.org/book/ch08-01-vectors.html#creating-a-new-vector)

vector similar to an array, but the # element can change
array is a sequence of element of the same type: 
- fixed size/length
- in order
- cannot grow/shrink

vector: (stored on the heap)
- same type in order
- in order
- cannot grow/shrink
- implement debug trait, not debug trait


```rust
[&str; 3]
```

```rust
fn main() {
   let pizza_diameters: Vec<i32>  = Vec::new();
   // turbofish operator 
   let pizza_diameters = Vec::<i32>:new();
   println!("{pizza_diameters}")

   let pasta: Vec<&str> = Vec::new();
   let pasta = Vec::<&str>:new();
   println!("{pizza_diameters}")

    // vec![] vec macro, allows for providing initial values
    let pizza_diameters = vec![8, 10, 12, 14];
    let pasta = vec!["fugi", "margaritha"];
}
```

## updating vectos

[updating vectors](https://doc.rust-lang.org/book/ch08-01-vectors.html#updating-a-vector)

push: add single element at the end
insert: in a certain index

```rust
fn main() {
    let mut pizza_diameters = vec![8, 10, 12, 14];
    pizza_diameters.push(16);
    pizza_diameters.push(16);
    println!("{pizza_diameters:?}")

    // index is first param, value is 2nd param
    pizza_diameters.insert(3, 17);

    // pop removes last value, returns an Option
    // None or Some
    let last: Option<i32> = pizza_diameters.pop();

    // if the index does not exist, runtime panic
    pizza_diameters.remove(2);
}
```

## reading

[reading](https://doc.rust-lang.org/book/ch08-01-vectors.html#reading-elements-of-vectors)

```rust
fn main() {
    // i32 
    let mut pizza_diameters = vec![8, 10, 12, 14];
    // the result will depend on the type of the vector
    // we create a copy -> pizza diameter remain owner
    let val = pizza_diameters[2]
    // borrow a slice
    let pizza_slice = &pizza_diameters[1..3];

    let pepperoni = String::from("pepperoni");
    let mushroom = String::from("mushroom");
    let sausage = String::from("sausage");
    // heap allocated -> ownership moves from values, to pizza (vector is owner of its parameters)
    let pizza_toppings = vec![pepperoni, mushroom, sausage];
    // we can no longer access pepperoni, mushroom or sausage
    // the below will not compile -> no copy trait
    let value = pizza_toppings[2]
    // the reference will work -> ref to a String
    let value = &pizza_toppings[2]
    // accessing on index that does not exist, we will panic
    // in an array this is possible
    let pizza_slice = &pizza_toppings[1..];
}
```

# get method

the get method extracts an element by index position. return an Option enum

-> ref to an element in the index position


```rust
fn main() {
    let pepperoni = String::from("pepperoni");
    let mushroom = String::from("mushroom");
    let sausage = String::from("sausage");
    // heap allocated -> ownership moves from values, to pizza (vector is owner of its parameters)
    let pizza_toppings = vec![pepperoni, mushroom, sausage];
    // returns an Option index -> return a reference
    let option = pizza_toppings.get(2)
    match option {
        Some(topping) => println!("{topping}")
        None => println!("no value")
    }
}
```

## ownership

```rust
fn main() {
    let pepperoni = String::from("pepperoni");
    let mushroom = String::from("mushroom");
    let sausage = String::from("sausage");
    // heap allocated -> ownership moves from values, to pizza (vector is owner of its parameters)
    let pizza_toppings = vec![pepperoni, mushroom, sausage];
    // ownership gets transferred

    let mut delicious_toppings = pizza_toppings;
    // borrow
    // 1 mutable reference
    // multiple immutable references are possible

    // rust can move memory in the heap -> references could become invalid
    // this reference is not used, so although the ref could move, it is not used
    // the ref co
    let topping_reference = &delicious_toppings[1];

    println!("the topping is {topping_reference}")
    
}
```

## writing vectors

overwrite a vector

```rust
fn main() {
    let pepperoni = String::from("pepperoni");
    let mushroom = String::from("mushroom");
    let sausage = String::from("sausage");
    // heap allocated -> ownership moves from values, to pizza (vector is owner of its parameters)
    let pizza_toppings = vec![pepperoni, mushroom, sausage];
    
    pizza_toppings[1] = String::from("olives");

    // the below would transfer ownership, so this is not possible without a mutable reference
    // Note we cannot have a 2nd reference, once a mutable
    let target_topping = &mut pizza_toppings[2];
    target_topping.push_str(" and Meatballs");
    // due to lifetimes when adding the 2nd mut reference
    // after the last usage of the first mut ref it is possible here
    let another_target_topping = &pizza_toppings[2];
    
}
```

## vector capacity behind the scenes

The vector capcity is the max number of enties in the vector

```rust
fn main() {
    let mut seasons: Vec<&str> = Vec::with_capacity(4)
    println!("length: {}, capacity: {}", seasons.len(), seasons.capacity())

    seasons.push("Summer");
    seasons.push("Fall");
    seasons.push("Winter");
    seasons.push("Spring");

    println!("length: {}, capacity: {}", seasons.len(), seasons.capacity())

    seasons.push("Summer");
    println!("length: {}, capacity: {}", seasons.len(), seasons.capacity())
}
```