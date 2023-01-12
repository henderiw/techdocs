# jq

[jq doc](https://stedolan.github.io/jq/manual/)

- filter: input -> output
- use cases:
  - extracting a filed or convert number to string
  - combining filters through pipes
  - collect the output of a filter into an arraay
- runs on a stream of JSON data

## Filters

### basic filters

```jq
.
```

### object identifier-index

```jq
.foo
."foo$"
.["foo$]
```

### optional identifier-index

does not produce an output when . is not an array or an object

```
.foo?
.[.foo?]
```

### generic object index

only works for strings

```
.["foo"]
```

### array index

```
.[0]
.[2]
.[-1] # last index
```

### array/string slice

```
.[2:4]
.[:3]
.[-2:]
```

### array/object value iterator

```
.[]
```

### comma

inout is fed into both filters

```
'.foo, .bar'
```

### pipe

`.a.b.c <-> .a | .b | .c`
`.a.b   <-> .a | . | .b`

### parentheses

```
'(. + 2) * 5' -> with inout 1 this gives 15
```

## types and values

same datatypes as JSON

- numbers
- strings
- booleans
- arrays
- objects -> string based keys only
- null


### array construction

```
[.user, .projects[]]
[ .[] | . * 2]
```

### object construction

```
{user: .user, title: .title} -> shortcut {user, title}

```

## Builtin operators and functions

### addition

numbers: added by normal arithmetic
arrays: concatenated into a larger aray
strings: joined into a larger string
objects: merging, the most right one wins

### substraction

### multiplication, division, modulo

