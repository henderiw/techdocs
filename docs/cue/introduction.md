# cue

## introduction

- poor or no validation (type checking)
- inheritance is the biggest source of complexity and prevents automation
    -> reduce bolerplate
    -> introduces complexities
    -> not worth it
    -> new: constraint are also able to reduce boilerlate

## concepts

types are values

json equivalent in CUE

```
moscow: {
    name: "Moscow"
    pop: 11,92M
    capital: true
}
```

go struct equivalent in CUE

```
municipality: {
    name: string
    pop: int
    capital: bool
}
```

instance of the go struct

```
largeCapital: {
    name: string
    pop: > 5M
    capital: bool
}
```

lattice of Values -> you get the same result if you merge them

municipality (go struct) -> largeCapital (instance) -> moscow (json)

## other highlights

- path shorthand: a: {b: {c:5}}} == a b c:5
- sum types/enums: a | b |c
- default values: number | *1
- arithemtic: 4+5
- string interpolation: "Hello \(person)"
- List and field comprehensions [ x for x in y]

## pratice

defining a schema is schem is cumbersome, keeping it up to date is cumbersome

CUE is JSON superset

## install

brew install cue-lang/tap/cue

CUE from go
CUE from yaml

cue import ./... -p kube -l '"\(string.Camel"'


## configuration

cue export json.cue
cue eval dupe.cue