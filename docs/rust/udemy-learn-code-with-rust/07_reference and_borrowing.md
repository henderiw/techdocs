# referecing and borrowing

## mutable references

[mutable references](https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html#mutable-references)

options:
- meal: String - full ownership and NO permission to mutate
- mut meal: string - ownership and permission to mutate
- meal: &String - no ownershio, NO permission to mutate
- meal: &mut String - no ownership, permission to mutate

```rust
fn main() {
    let mut current_meal = String:new(); // reference does not change ownership
    current_meal = add_flower(&mut current_meal);
    current_meal = add_sugar(&mut current_meal);
    // we pass in a reference
    show_my_meal(&current_meal);
}

fn add_flower(meal: &mut String)  {
    meal.push_str("Add flower");
}

fn add_sugar(meal: &mut String)  {
    meal.push_str("Add sugar")
}

// meal parm is a reference to a string -> immutable reference
// can read, but not write
fn show_my_meal(meal: &String) {
    println!("Meal steps: {meal}")
}
```

[mutuble references](https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html#the-rules-of-references)

ISSUE:
- a mutable reference can mutate the dat
- some expectations might not be met

Solution:
- you can create as many immutable references as you want, since you cannot modify the data

```rust
fn main() {
    let car = string::from("red");

    // we can use them at the same time
    let ref1 = &car;
    let ref2 = &car;
    println!("{}")
}
```

Solution:
- a variable can not have simultenously have a mutable reference and an immutable or mutable reference.
- You cannot have 1 mutable reference at any given time
- compiler is smar if it is not used, it allows it -> LIFETIME

-> this is like a write Lock.

```rust
fn main() {
    let mut car = string::from("red");

    // we can use them at the same time
    let ref1 = &mut car; // ref1 borrows the string, ownership remains with car; LIFETIME ends here
    let ref2 = &car;
    println!("{ref2}")
}
```

```rust
fn main() {
    let mut car = string::from("red");

    // we can use them at the same time
    let ref1 = &mut car; 
    let ref2 = &car; // this is an issue
    ref1.push_str(" and Silver"); // LIFETIME of ref1 ends here
    println!("{ref2}")
}
```

references, immutable references implement the copy trait
mutable reference do not implement the copy trait -> this is to adhere to the LIFETIME restriction

```rust
fn main() {
    let coffee = String::from("Moche");
    let a = &coffee
    let b = a; // this is ok, since immutable reference are hold on the stack and are cheap to copy

    let ref1 = &mut coffee;
    let ref2 = ref1 // the ownership moves to ref2
    println!("{ref1}, {ref2}") // this fails since ref1 lost ownership
}
```

## dangling references

[dangling reference](https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html#dangling-references)

a pointer to a reference on which the value is gone
-> the compiler checks this

```rust
fn main () {

}

fn create_city() -> &String {
    let city = String::from("new york");
    &city // return a danglign reference -> compiler blocks this
} // scope of city ends here, so the variable gets returned
```

valid code

```rust
fn main () {
    let city = create_city(); // this copies
    println!("{city}");

}

fn create_city() -> String {
    String::from("new york");
}
```

## collection types

ownership nuances 

```rust
fn main () {
    // registration is the owner of the array
    let registrations = [true, false, true];
    // bool implements the copy trait
    // rust creates a copy
    let first = registrations[0]; 
    println!("{first} and {registrauions}")

    // option 1
    let languages = [String::from("rust"), String::from("go")]
    // this is not allowed -> since the copy trait is not implemented for String type -> we need to use a reference or copy (copy here)
    let first = languages[0].clone(); // creates a full copy

    // option 2
    let languages = [String::from("rust"), String::from("go")]
    // this is not allowed -> since the copy trait is not implemented for String type -> we need to use a reference or copy (reference here)
    let first = &languages[0] // we borrow a reference of the first element, w/o moving ownership

}
```

The same applies to tuples