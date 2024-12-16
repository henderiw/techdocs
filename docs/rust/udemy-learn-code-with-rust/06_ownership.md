# ownership

[ownership](https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html#what-is-ownership)
[ownership rules](https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html#ownership-rules)

- compiler feature
    - rules that the compiler checks for such that the program is free of memory errors
- memory stores information your program uses.
- its ideal to free memory when it is no longer in use
    - deallocation
- programming languages implement different strategies for memory management

examples:
- C and C++: programmer is responsible for memory management
    - forget to deallocate memory
    - deallocate that is already been deallocated
    - burden is on the developper
- Java, Python, Rugby and Go
    - implement garbage collection
    - automates the cleanup process
    - garbage collection use memory and can run at times you don't want

- RUST uses ownership with the compiler
    - speed
    - safety using ownership with a compiler

What is ownership?
    - owner is who/what is responsible for deallocating
    - every value has 1 owner
    - the owner can change, but there can be 1 owner at the time
    - the owner is usually a name
        - the variable can be an owner
        - a parameter can be an owner
    - ownership also extend to composite types that own their elements
        - a tuple and array own theu values

[stack and heap](https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html#the-stack-and-the-heap)

- stack and heap are 2 different parts/regions of the computers memory
- the stack and heap read

- stack: faster, but only at fixed and knwon at compiler time
- heap: dyanmic data that can change

## stack

- stores values in the sequential order it receives them
- LIFO: last in, first out
- adding data -> Pushing onto the stack
- removing data -> popping off the stack
- All stack data has a fixed, consistent size that is known at compile time
- data types like integers, floatingpoint, booleans, char, arrays have a fixed size -> stores them in the stack at runtime
- The pieces of data on the stack will not grow or shrink in size as the program runs

## heap

- large area of storage space
- data whose size is not known at compile time (user input, a files content, etc)
- when rust program needs dynamic space, it requests it from the ehap. A program called the memory allocator finds a spot
    - rference
    - the memory allocators returns a reference, which is an address
    - the ref to the memory address of the data
    - references have a fixed size, so rust stores them on the stack, the data is on the heap
    - address to the house -> pointer
- allocating on the heap is slower than pushing to the stack, the memory allocator has to spend time searching for an open spot large enough to fit the data
- accessing data is faster on the stack then the heap as well. With a heap, the program has to follow the pointer to find the memeory address
- a stack stores the data in sequence, so there is less jumping around from point to point.

Dynamic data -> HEAP
Static data, known at compile time -> STACK

ownership:
- purpose is to assign responsibility for deallocating memory (primarily heap memory)
- is a compiler feature for reducing duplicate heap data and cleaning up heap data that is no longer needed

[scope](https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html#variable-scope)

scopes
- a boundary/region where a variable name is valid
- scopes are related to a block
- when a blocks end the variables get deallocated

```rust
fn main() {
    let age = 33;

    {
        let is_handsome = true; // is_handsome variable is the owner -> responsible for removing the stack variable
    } // is_handsome goes out of scope

    // age variable exists here
} // age variable goes out of scope here -> deallocate memory
// deallocation happend in LIFO
```

- the variable become the owner of the data
- the owner knows how to cleanup memory when the variable goes out of scope.

## copy trait

[copy trait](https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html#stack-only-data-copy)

trait is a contract, promises the methods of the type

copy trait 
- ensures the data can be copied using the copy trait
- all simple types implement the copy trait

```rust
fn main() {
    let time = 2025;
    let year = time; // rust will create a copy on the stack -> 2 duplicate entries on the stack -> 2 owners

    println!("{time}, {year}");
} 
```

## string

- stored on the heap
- &str
    
    - known at compile time
    - stored in the binary
- String 
    - string literal, strign slide
    - UTF8 encoded characters
    - mutable
        - mutation, adding, deletign chars
    - stored on the HEAP
    - String namespace is being navigated by the 


```rust
fn main() {
    let food: &str = "pasta"; // stored in the binary, since it is known
    let text: String = String::new() //string namespace, ::new we navigate in the namespace -> new function of that type -> returns an empty type
    let candy = String::from("KitKat") // kitkat is in the binary -> used to create the string on the HEAP
} 
```

[updating string](https://doc.rust-lang.org/book/ch08-02-strings.html#updating-a-string)
- push_str methos

```rust
fn main() {
    // data on the heap and stack
    // stack: reference to the heap, length: in bytes, capacity (how much is available in that location): -> capacity is used for the length to expand 
    let mut name = String::from("Baris");
    println!("{Name}")
    // option1: new capacity is sufficient -> update the capacity
    // option2: capacity is not sufficient -> moved to a new location
    name.push_str("Pask");
    println!("{Name}")
}
```

## moves

[move](https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html#variables-and-data-interacting-with-move)

a move is the transfer of ownership from one owner to another
-> who is responsible for cleaning up data

```rust
fn main() {
    let person = String::from("Baris"); 
    // String does not implement copy trait, so this does not get copied -> they are expensive
    // rust copied the reference on the stack, but the heap does not get copied
    // we have 2 reference to the same heap
    // we is responsible for cleaning it up -> genius; person goes out of scope -> person variable can no longer be used
    let genius = person; 
} // 
```

## the drop function

what happens when an owner goes out of scopes
-> drop function is called when a variable goes out of scope
-> drop is called automatically for HEAP by rust

we can also call it manually


```rust
fn main() {
    let person = String::from("Baris"); 
    
    drop(person) // manual deallocation
} 
```

## clone method

[clone](https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html#variables-and-data-interacting-with-clone)

clone
- forces duplicate data on the heap
- the type determines how to clone the heap
- 2 owners for 2 pieces of data, with a copy


```rust
fn main() {
    let person = String::from("Baris"); 
    let genius = person.clone();
    
    drop(person) // manual deallocation
} 
```

## reference

[reference and borrowing](https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html#references-and-borrowing)

borrow 
- means using something
- we never change ownership

reference: 
- is an example of a pointer/address to the data
    - reference is a type of pointer (the value is guaranteed, which is not true in other languages)
    - reference must never outlive the referent (original value)
- borrow is the verb, reference is the noun
- typically used for heap data, but can also be used for stack although less used


```rust
fn main() {
    let my_stack_value = 2; 
    let my_int_reference = &my_stack_value; // this is a borrow from a stack -> this is not typical

    let my_heap_value = String::from("Toyota");
    let my heap_ref = &my_heap_value; // this is a borrow for heap data; 
    // heap_ref is the owner of the reference, but not the owner of the data
} 
```

dereference operator
- an operator is a symbol that applies an operation to a value
- means to access the data at the memory address that the reference points to
- *

```rust
fn main() {
    let my_stack_value = 2; 
    let my_int_reference = &my_stack_value; // this is a borrow from a stack -> this is not typical
    println!("{*my_int_reference}") // dereference operator

    let my_heap_value = String::from("Toyota");
    let my heap_ref = &my_heap_value; // this is a borrow for heap data; 
    // heap_ref is the owner of the reference, but not the owner of the data
     println!("{*heap_ref}") // dereference operator
} 
```

## String, &String, str, &str

```rust
fn main() {
   /*
    String - a dynamic piece of text stored on the heap at runtime
    &String ("ref String) -  a ref to a heap String
    str = a hardcoded, read-only piece of test encoded in the binary
    &str (ref str) - a reference to the text in the memory that has loaded the binary file
    &str
   */

  let ice_cream = "Cookies and Cream"; // this text is contained in the binary
  println!("{}", ice_cream)
} 
```

## copy trait

stack types implement the copy trait
references also implement the copy trait

```rust
fn main() {
    ley ice_cream: &str = "Cookies and Cream"; // this is a reference
    let dessert = ice_cream; // this is a copy of the reference -> they point to a data location
}
```

## ownership and fucntion and parameters

- parameter is the same as a variable
- some implement the copy trait


```rust
fn main() {
    let apples: i32 = 6;
    print_my_value(apples); // this is the same as let value == apples; -> copy since this is a stacked entry
    println!("{apples}");


    let oranges: i32 = String::from("Oranges");
    print_my_string(oranges); // let name = oranges; -> ownership gets transferred
    // oranges is no longer the owner of the string
    println!("{oranges}"); // this fails since the heap data is cleaned up, due to the move of ownership
}

// receives a copy of the value 6
fn print_my_value(value: i32) {
    println!("Your value is {value}");
}

fn print_my_string(name: String) {
    println!("Your name is {name}");
    // deallocates the text
}
```

## mutable parameters

fn parameters are immutable by default
- when we change ownership, we can also change the mutability

```rust
fn main() {
    let burger = String::from("Burger");
    add_fries(burger) // ownership moves from burger to meal -> let meal = burger // meal is not mutable
}

fn add_fries(mut meal: String) {
    meal.push_str(" and fries")
}
```

## return values

[return values](https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html#return-values-and-scope)

```rust
fn main() {
    let cake = bake_cake(); // moves ownership from invoked fn to the instantiation fn
    println!("{cake}");


}

fn bake_cake() -> String {
    String::from("chocolate mousse") // return preserves the string
}
```

challenges
- the below, needs to return the string to avoid copying and that ownership moves back

```rust
fn main() {
    let mut current_meal = String:new();
    current_meal = add_flower(current_meal);
    current_meal = add_sugar(current_meal);
}

fn add_flower(mut meal: String) -> String {
    meal.push_str("Add flower");
    meal
}

fn add_sugar(mut meal: String) -> String {
    meal.push_str("Add sugar")
    meal
}
```

better approach
-> use references: see section 7

Ownership:
- compiler feature
- a value has 1 owner at the time
- owner is responsible for cleaning up a values
- stack:
    - faster for read/write
    - LIFO
    - fixed size : known ahead of the compilation
- heap
    - dynamic size (runtime, can change, not at compile time)
    - memory allocator finds an empty spot
- ownership
    - scope is the boundary within a program where a name is valid
    - a scope ends when a blocm concludes
    - the owner cleans up its data when its name goes out of scope
- a copy trait
    - scalar types implement the copy trait
    - reference implement the copy trait
- str Type
    - string literal or string slice
    - put in the binary
- String type
    - lives on the heap
    - dynamic