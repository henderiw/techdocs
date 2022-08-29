# background & images

[styling images](https://www.w3schools.com/css/css3_images.asp)

## background
- [background-property]( https://developer.mozilla.org/en-US/docs/Web/CSS/background)
- background-image
- background-size:
  - cover -> 
  - contain -> keeps the aspect-ratio of the image
  - 100%
- background-position: (x-axis, y-axis)
  - 0% 100%
  - center -> like 50% 50%
  - left top
- background-origin: border-box
- background-clip: border-box
- background-attachement: scroll, fixed

```
background: url("freedom.jpg");
	background-size: cover;
	background-position: left 10% bottom 20%;
	background-repeat: no-repeat;
	background-origin: border-box;
	background-clip: border-box;
	background-attachment: scroll;
```

shortcut

```
background: url("freedom.jpg") left 10% bottom 20%/cover no-repeat border-box;
```

## styling images

```
.main-header__brand {
	color:  #0e4f1f;
	text-decoration: none;
	font-weight: bold;
	font-size: 22px;

	height: 22px;
	display: inline-block;
}

.main-header__brand img {
	height: 100%;
}
```

we need to define the a -> display in-line-block

## linear gradient

treated as images

```
background-image: linear-gradient(red, blue);
```

## radial gradient

```
background-image: linear-gradient(red, blue);
```

## stacking multiple backgrounds

use transaparancy
only 1 color can be used

	background: linear-gradient(to top, rgba(80,68,18,0.6) 10%, transparent), url("images/freedom.jpg") left 10% bottom 20%/cover no-repeat border-box, #ff1b68;


## filters

[filter](https://developer.mozilla.org/en-US/docs/Web/CSS/filter)

filter: blue(10px);

change the appearance 

## styling svgs

scalable vector graphics


fill: #f09b24;
	stroke: black;
	/*stroke-width: */

[styling svgs](https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/SVG_and_CSS)