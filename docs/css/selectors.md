# css selector

## element selectors

```
h1 {
	color: red;
}
```

## class selectors
- add a class 
- use kebab naming
- classes can be reused

. {
	color
}

## * seclector

not performant

```
* {
	color: red;
}
```

## id selector

select 1 becuase an id should only occur once
used for navigation mainly

```
# {
	color: red;
}
```

## attribute selector

<button disabled>
	Click
</button>

[disabled] {
	color: red;
}

## style selectors and specifities

specifities:
- in-line style
- #id selctors
- .class selectors
- <tag> and ::pseudo-elements


if there are multiple selectors in the same file -> the last one in the file wins

## inheritance

the more specific selector wins -> inheritance has the lowest priortiy

## combinators

one option is font-family: inherit;

## combinators

#product-overview h1 {

}

this is more specific


