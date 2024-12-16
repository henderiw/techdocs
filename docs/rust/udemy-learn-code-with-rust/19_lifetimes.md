# lifetimes

## concrete lifetimes for values

Describes how long something is alive/useful/valid
- the lifetime of a value refers to how long it is valid within the code (capable of being utilized)
- lifetime is the time during which it exists at a particular memory address
Other:
- concrete lifetime; clearly defined
- often connected to scopes, but not necessary

```rust
fn main() {
    let a = 1; //a is alive here -> start to become valid here

    // nest block - nest scope
    // fn call
    [
        let b = 2;
    ] // b's lifetime ends here
    // b is no longer valid here

    let c = String::from("Winter"); // lifetime of c starts here
    let d = c; // lifetime of c ends here, since ownership move to d (no copy trait)

    drop(d) // lifetime of d ends here
} // a is no longer alive after this clossure
```
## lifetime for references

[dangling references](https://doc.rust-lang.org/book/ch10-03-lifetime-syntax.html#preventing-dangling-references-with-lifetimes)
[borro checker](https://doc.rust-lang.org/book/ch10-03-lifetime-syntax.html#the-borrow-checker)

reference:
- is a value, memory address of another value (dpendening on the exisance of the value)
- lifetime start when it is stored
- lifetime stops when the location removed
- is linked to a starter value (the borrow) -> cannot outlive the value
- lifetime is contained within the reference value

example:
- address to a house; if the house dissapeared, the ref should disappear

the borrow checker is a part of the rust compiler that validates that all borrows (i.e. reference) are valid

dog -> referent is the value being borrowed
my_pet -> reference is the actual borrow

```rust
fn main() {
    let dog = String::from("Watson"); 
    {
        let my_pet = &dog
        println!("{my_pet}");
    }
    println!("{dog}");
    {
        let my_pet = &dog
        println!("{my_pet}");
    }
}
```

## non lexical lifetimes

Lexical means lasting until the end of the block.
Non lexical means not lasting until the end of the block.

The borrow checker treats the end of a reference's lifetime as the last place it is used; a reference has a non lexical scope

```rust
fn bar() {
    let mut data = vec!['a', 'b', 'c'];
    let slice = &mut data[..];
    capitalize(slice); // slice lifetime end as it is last used here
    data.push('d'); // this creates a new mutable ref, but since slice is no longer used after this, this is no allowed
    data.push('e');
    data.push('f');
}
```

### invalid lifetimes I

A dangling reference is a ref to data that no longer exists

```rust
fn main() {
    let cities = vec![
        String::from("A");
        String::from("B");
        String::from("C");
    ]

    let favorite_cities = &cities[0..2]; // slice to a potion of the data
    drop(cities); // the referent is invalid -> danfling reference
    println!("{favorite_cities:?}");
}
```

The borrow lives to long

```rust
fn main() {
    let some_cities = {
        let cities = vec![
            String::from("A");
            String::from("B");
            String::from("C");
        ]
        &cities[0..2] // this returns a slice to cities, but cities lifetime end after the block stops
    }
}
```

```rust
fn main() {
    
    let cities = vec![
        String::from("A");
        String::from("B");
        String::from("C");
    ]
    let favorite_cities = &cities[0..2];
    let places = cities; // places becomes the owner, cities lifetime ends jere
    println!("{favorite_cities:?}"); // this is a dangling ref
}
```

## fns cannot return refs to owned values or parameters

A fn cannot return a ref created inside its own body
A fn cannot return a ref to an owned param

The above is relevant for any type

Solution: return a value


```rust
fn create() -> &i32 {
    let age = 100;
    &age // creates a dangling reference, since age ends here
}
```

```rust
fn create_slcide(items: Vec<i32>) -> &[i32] { // items take ownership
    &items[0..2] // dangling ref
} // items param lifetime ends here
```

This error is also relevant if the type implements the copy trait, the copy trait copies, but the ref is to the original value

```rust
fn create_nbr_ref(nbr: i32) -> &[i32] { // items take ownership
    &number // dangling ref
} // items param lifetime ends here
```

## refs as fn parameters

In this examples the data lives outside of the function

```rust
// due to ref we dont loose ownership
// &[String] -> deref coercion allows vectors or arrays
fn select_first_two_elements(items: &[String]) {
    let selected_items = &items[..2];
    println!("{selected_items:?}");
}

fn main() {
    let cities = vec![
        String::from("A"),
        String::from("B"),
        String::from("C"),
    ]

    select_first_two_elements(&cities);

    {
        let coffees = [
            String::from("A"),
            String::from("B"),
        ]
        select_first_two_elements(&coffees);
    }
}
```

new case with returning a ref, ok as long as the returning ref is connected to the lifetime of the input param reference
-> this is the only way a ref can be returned;

```rust
// due to ref we dont loose ownership
// &[String] -> deref coercion allows vectors or arrays
fn select_first_two_elements(items: &[String]) -> &[String] {
     &items[..2]
}

fn main() {
    let cities = vec![
        String::from("A"),
        String::from("B"),
        String::from("C"),
    ]

    two_cities = select_first_two_elements(&cities);
    println!("{two_cities:?}")

    {
        let coffees = [
            String::from("A"),
            String::from("B"),
        ]
        two_coffees = select_first_two_elements(&coffees);
        println!("{two_coffees:?}")
    }
}
```

## generic lifetimes

[generic lifetimes in fn](https://doc.rust-lang.org/book/ch10-03-lifetime-syntax.html#generic-lifetimes-in-functions)
[lifetime annotation syntax](https://doc.rust-lang.org/book/ch10-03-lifetime-syntax.html#lifetime-annotation-syntax)
[lifetime annotation fn signatures](https://doc.rust-lang.org/book/ch10-03-lifetime-syntax.html#lifetime-annotations-in-function-signatures)
[thinking in terms of lifetimes](https://doc.rust-lang.org/book/ch10-03-lifetime-syntax.html#thinking-in-terms-of-lifetimes)

- concrete lifetime: is the region of code that a value exists in the program
- generic lifetime is more abstract: it is a hypotectical lifetime, a non specific lifetime, a future lifetime that can vary
- we can annotation generic lifetimes in our code. This enables fns that are flexible enough to handle varying lifetimes

- a lifetime annotation is a name or label for a lifetime
- lifetime annotation dont change the ref lifetime. They dont affect the logic in any way

it is like a marker between parameters and return values
-> below: we indicate that the items param lifetime to the return lifetime
-> the returned ref can not outlife the referent ref

We explicitly declare a promise to the borrow checker

```rust
// due to ref we dont loose ownership
// &[String] -> deref coercion allows vectors or arrays
fn select_first_two_elements<'a>(items: &'a[String]) -> &'a[String] {
     &items[..2]
}

fn main() {
    let cities = vec![
        String::from("A"),
        String::from("B"),
        String::from("C"),
    ]

    two_cities = select_first_two_elements(&cities);
    println!("{two_cities:?}")

    {
        let coffees = [
            String::from("A"),
            String::from("B"),
        ]
        two_coffees = select_first_two_elements(&coffees);
        println!("{two_coffees:?}")
    }
}
```

## lifetimes and referents

returned reference is connected to the referent

when rust sees an equal sign it always looks at the right

```rust
// due to ref we dont loose ownership
// &[String] -> deref coercion allows vectors or arrays
fn select_first_two_elements<'a>(items: &'a[String]) -> &'a[String] {
     &items[..2]
}

fn main() {
    let cities = vec![
        String::from("A"),
        String::from("B"),
        String::from("C"),
    ]

    two_cities = {
        let cities_ref = &cities // the referent is cities
        select_first_two_elements(&cities_ref)
    } 
    println!("{two_cities:?}")
    {
        let coffees = [
            String::from("A"),
            String::from("B"),
        ]
        two_coffees = select_first_two_elements(&coffees);
        println!("{two_coffees:?}")
    }
}
```

## lifetime Elision Rules I

[lifetime elision](https://doc.rust-lang.org/book/ch10-03-lifetime-syntax.html#lifetime-elision)

Elision is the act of omitting something. Lifetime elision means omitting generic lifetime annoitations in situations where the borrow checker can infer the lifetime relationship automatically

3 rules:
- the compiler assigns a lifetime to each parameter that is a reference
- if there is 1 ref parameter and the return value is a ref, the borrow checker will infer that their lifetimes are related
- in a method definition, if there are multiple ref parameters but one of them is self, the borrow checker will assume the lifetime of the instance is connected to the lifetime of the return value

when there are more then 1 parameter ref the relationship is unclear -> we need to help the borrow checker

```rust
fn choose_favorite<'a>(first: &'a str, second: &str) -> &'a str {
    first
}
```

```rust
// 'a first and second can both be returned
fn longest<'a>(first: &'a str, second: &'a str) -> &'a str {
    if first.len() > second.len() {
        return first
    } else {
        return second
    }
}

fn main() {
    let a = String::from("a");
    {
        let b = String::from("b");
        let result = longest(&a, &b)
        println!({result});
    }
}
```

The below does not compile -> dangling reference

```rust
fn longest<'a>(first: &'a str, second: &'a str) -> &'a str {
    if first.len() > second.len() {
        return first
    } else {
        return second
    }
}

fn main() {
    let a = String::from("a");
    let result = {
        let b = String::from("b");
        longest(&a, &b) 
    }// b's lifetime is no longer valid after this and hence this results in a dangling reference
}
```

This works for thr borrow checker -> but does not not really use the 2nd parameter


```rust
fn longest<'a, 'b>(first: &'a str, second: &'b str) -> &'a str {
    first
}

fn main() {
    let a = String::from("a");
    let result = {
        let b = String::from("b");
        longest(&a, &b) 
    } 
}
```

Rule 3

```rust
struct DentistAppointment {
    doctor: String.
}

impl DentistAppointment {
    // it assumes that the return ref lives as long as DentistAppointment lives
    fn book<'a, 'b, 'c>(&'a self, check_in_time: &'b str, check_out_time: &'c str) -> &'a str {
        println!("You are booked from {} to {} with doctor {}",
            check_in_time,
            check_out_time,
            self.doctor,

        )
        &self.doctor
    }
}

fn main() {
    let a = DentistAppointment{
        doctor: String::from("wim"),
    }
    let result = a.book("03:00PM", "04:00PM")
    println!("{result}");

}
```

## lifetimes in structs

[lifetime annoitation in structs](https://doc.rust-lang.org/book/ch10-03-lifetime-syntax.html#lifetime-annotations-in-struct-definitions)

so far: save
- types that have a copy trait
- struct owned by the type

what about refs in a struct?
-> the str ref must outlive the Struct

```rust
#[derive(Debug)]
struct trainSystem<'a> { // the struct cannot outlive the ref
    name: &'a str, 
}

fn main() {
    let name = String::from("A")
    let transit = Trainsystem {name: &name};
    println!("transit:#?");
}
```

the below will not work

```rust
#[derive(Debug)]
struct trainSystem<'a> { // the struct cannot outlive the ref
    name: &'a str, 
}

fn main() {
    let transit = {
        let name = String::from("A")
        Trainsystem {name: &name};
    } // the name is out of scope here, so gets deallocation -> this will fail compilation byt the borrow checker
    println!("transit:#?");
}
```

## multiple lifetimes

```rust
#[derive(Debug)]
struct TravelPlan<'a> { 
    from: &'a str, 
    to: &'a str,
}


fn main() {
    let from = String::from("A")

    let plan = {
        let to = String::from("B");

        let plan = TravelPlan {
            from: &from,
            to: &to
        }
        plan.from
    }; // the borrow checker will fail since to field is a dangling ref
}
```

solution: decouple lifetimes

```rust
#[derive(Debug)]
struct TravelPlan<'a, 'b> { 
    from: &'a str, 
    to: &'b str,
}


fn main() {
    let from = String::from("A")

    let plan = {
        let to = String::from("B");

        let plan = TravelPlan {
            from: &from,
            to: &to
        }
        plan.from // since from is available this code works, even if to gets deallocated
    }; 
}
```

## static lifetime

[static lifetime](https://doc.rust-lang.org/book/ch10-03-lifetime-syntax.html#the-static-lifetime)

ref that guarantees to exist for the duration of the program
- string Slice -> it has a 'static lifetime

```rust
const COUNT: i32 = 400;

fn say_hello() -> &'static str {
    "Hello"
}

fn value() -> &'static i32 {
    &COUNT
}

```