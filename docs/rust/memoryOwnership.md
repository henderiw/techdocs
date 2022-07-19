# memory recap

## memory

memory is stored using binary
- bots 0 or 1

computer optimized for bytes
- 1 byte = 8 bits

## addreses

all data in memory has an address
- used to locate data
- always the same  only data changes
usually dont utilize addresses directly
- variabale handle most of the work

## offsets

- items can be located at an address using an offset
- offset begin at 0
- represent the number of bytes away from the original address
  - normlly deal with indexes instead

## summary

memory uses addresses and offsets
addresses are permanent, data differs
offsets can be used to index into some data

## ownerships

- programs must manage meory in some way to prevent leaks
  - if they fail to do so, a leaak occurs
- rust utilizes an ownership model to manage memory
  - the owner of the memory is responsible for cleaning up the memory
  - this occurs automatically at the end of the scope/function
- memory can either be moved or borrowed
  - default behavior is to move the memory to a new owner
    - this means a copy and can slow down
  - borrow of memory is done using the ampersane (&)

```
enum Light {
    Bright,
    Dull,
}

fn display_light(light: &Light) {
    match light {
        Light::Bright => println!("bright"),
        Light::Dull => println!("bright"),
    }
}

fn main() {
    // owns the moemory
    let dull = Light::Dull;
    // Light gets moved -> function deletes this memory
    // using the & we borrow the data
    display_light(&dull);
    display_light(&dull);
}
```

exercise a11

## stack

- data placed sequemtially
- limited space
- variables stored on the staack
- very fast to work wiith
  - offsets to access

## heap

- data placed algorithmically
  - slower than stack
    - Requested from the OS -> takes time
- unlimited space (ram/disk limits apply)
- uses pointers
  - pointers are a fixed size
  - usize aand isize data type
- vectord and hashmaps stored on the heap

## Lifetimes

- issue is if we want to borrow the data -> lifetime annotations
- Answer exists in the form and will exists until the Form exists

```
#derive(Debug)]
enum Answer {
  Yes,
  No,
}

#derive(Debug)]
// 'a is a lifetime
enum Form<'a> {
  question: &'a Answer,
}

// ownership of the data is within the curly braces
// data that is owned is released after the }
fn main() {
  let answer = Answer

  // answer owned by form from here, answer is borrowed
  let form = Form { question: &answer};

  println("{:?}", form);

  // other way to represents the same
  let form;
  {
    let answer = Answer::Yes;
    form =Form { question: &answer};
  }
  println("{:?}", form);
}
```

lieftime in functions
the issue here is because we borrow 2 x the same Object

```
#[derive(Debug)]
struct Quiz {
  question: Answer,
}

fn get_first_question<'a>(q1: 'a &Quiz, q2: &Quiz) -> &'a Answer {
  &q1.question
}

```