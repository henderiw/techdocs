# css feaatures

[css working groups](https://www.w3.org/TR/tr-groups-all#tr_Cascading_Style_Sheets__CSS__Working_Group)

## css variables

[variables](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_variables)

pro: only defines once and change will go everywhere
con : browser support IE

```
:root {
	--dark-green: #0e4f11f;
	--highlight-color: #ff1b68;
}


.button {
	background: var(--dark-green, #0e4f1f);
	color: white;
	font: inherit; /* required to override browser default*/
	border: 1.5px solid var(--dark-green, #0e4f1f);
	padding: 0.5rem;
	border-radius: 8px;
	font-weight: bold;
	cursor: pointer;
}
```

## vendor prefixes

[vendor prefixes](https://developer.mozilla.org/en-US/docs/Glossary/Vendor_Prefix)
[which vendor prefix shoulf i use](http://shouldiprefix.com/)


when browser are implementing different code

```
display: --webkit-box
display: flex
```

[css autoprefixer tool](https://autoprefixer.github.io)

## support queries

[support queries](https://developer.mozilla.org/en-US/docs/Web/CSS/%40supports)

if the browser does not support this it will not execute

@supports (display: grid) {
	.container {
		display: grid;
	}
}

## polyfills

[polyfills](https://github.com/Modernizr/Modernizr/wiki/HTML5-Cross-Browser-Polyfills)

js pkg which enables certain css features in browsers which would not support it otherwise

## eliminating cross-browser inconsistencies

- browsers use different defaaults
  - different margins, paddings
  - different box-sizing

use rest library e.g. Normalize.css -> overhead might be too high
or do it manually like our

* {
	box-sizing: border-box;
}

## name CSS classes

- use kebab-case -> CSS is case insensitive
- name by feature -> .page-title
  - NOT by style

[BEM: block element modifier](http://getbem.com/introduction/)

.<block>__<element>--<modifier>

.menu-main__item--size-big

## CSS vs frameworks

component frameworks
- foundation
- bootstrap

utility frameworks
- tailwind css
  - no components, layout, utility css classes

pro/con:
- full control 
- unneccessary code
- name as you like + follow best practices
- build everthign from scratch
- danger of bad code
