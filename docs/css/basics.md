# css styles

## adding css code to the page

### option 1: in-line styling

declaration -> what you want to style and how you want to stylt
- what: property
- how: value -> red or hex or rgb

<section style="background: #ff1b68">

hard to update and debug the code

### option 2: selectors

css rule
- selector: to which element to assign the declaration
- declaration:
  - property
  - value

in head section

index.html file
```
<head>
	<style>
		section {
			background: #ff1b68
		}
	</style>
</head>
```

### otion 3: css style sheet -> recommended way

main.css

```
section {
			background: #ff1b68
		}
```

index.html
```
<head>
	<link rel="stylesheet" href="main.css>
</head>
```

## fonts

- font-families:
  - standard
  - serif
  - sand-serif

google fonts

# shorthand properties

```
border-width: 2px
border-style: dashed | solid
border-color: orange
```

-> shorthand properties

```
border: 2px dashed orange
```

```
margin-top: 5px
margin-right: 10px
margin-bottom: 5px
margin-left: 10px
```

-> shorthand properties

```
margin: 5px 10px 5px 10px (top, right, bottom, left)
margin: 5px 10px (top/bottom, left/right)
margin: 10px
```

