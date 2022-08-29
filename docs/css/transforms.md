# transform

- rotatating
- 3d

[transforms](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Transforms/Using_CSS_transforms)
[3d transforms](https://desandro.github.io/3dtransforms/)

## practial packages package_bagde

```
.package__badge {
  position: absolute;
  top: 0;
  right: 0;
  margin: 0;
  font-size: 0.8rem;
  color: white;
  background: #ff5454;
  padding: 0.5rem;
	/* hW accelerated */
	transform: rotateZ(45deg);
	transform-origin: left top;
}
```

## practical customers 

```
.testimonial__image-container {
	width: 60%;
	max-width: 40rem;
	box-shadow: 3px 3px 3px 3px rgba(0,0,0,0.3);
	transform: skew(20deg);
	overflow: hidden;
}

.testimonial__image {
	width: 100%;
	vertical-align: top;
	transform: skew(-20deg) scale(1.4);
}	
```

## 3d transformations

perspective property should be applied on the container
perspective: 1000px


child element
-> perspective is to be set on the parent
transform: rotateX(30deg) rotateY(30deg)

