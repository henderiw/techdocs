# derive

special macro for print

```
// Clone, Copy -> iso borrow it will copy the data
// We should be careful about this
#[derive(Debug, Clone, Copy)]
enum Position {
    Manager,
    SUpervisor,
    Worker,
}

#[derive(Debug, Clone, Copy)]
struct Employee {
    position: Position,
    work_hourse: i64,
}

fn main() {
    let me = Employee {
        position: Position::Worker,
        work_hours: 40,
    };
    println("{:?}". me)
}
```

