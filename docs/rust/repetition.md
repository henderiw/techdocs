## loops

2 types of loops
- while loop
- infinite loops

both can be stopped by a break

## loop

infinite loop

```
let mut a = 0;
loop {
    if a == 5 {
        break;
    }
    println("{:?}", a);
    a = a + 1;
}
```

## while

conditional loop

```
let mut a = 0;
while a != 5 {
    println!("{:?}", a);
    a = a + 1;
}
```

## while..let

- perform looping when you have specific data
- useful when working with iterators

```
fn main() {
    let mut data = Some(3);
    // runs the loop as long as there is data
    while let Some(i) = data {
         println!("loop");
         data = None;
    }
    println!("done");

    // example with itertors
    let numbers = vec![1,2,3];
    let mut number_iter = numbers.iter();
    while let Some(num) = number_iter.next() {
        println!("num = {:?}", num);
    }
    println!("done");
}
```